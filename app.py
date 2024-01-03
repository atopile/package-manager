import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Path to your service account key
service_account_path = 'atopile-880ca67acfe2.json'

# Initialize Firestore
if not firebase_admin._apps:  # Check if already initialized to prevent reinitialization
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()
modules_collection = db.collection('packages')  # Replace 'modules' with your actual collection name

# Function to query modules based on selected types using 'AND' logic
def query_modules(selected_types, numeric_filters):
    results = []

    # Start with a reference to the collection
    query_ref = modules_collection

    # Execute the initial query
    snapshot = query_ref.stream()
    for doc in snapshot:
        module = doc.to_dict()

        # Check if all selected types are present in the module's types
        if selected_types and not all(t in module.get('types', []) for t in selected_types):
            continue

        # Check numeric properties
        properties_satisfied = True
        for prop, (min_val, max_val) in numeric_filters.items():
            # Loop through each interface and check if it satisfies numeric constraints
            for interface in module.get('interfaces', []):
                prop_value = interface.get(prop)
                if prop_value:
                    if not (min_val <= prop_value['min'] <= max_val and min_val <= prop_value['max'] <= max_val):
                        properties_satisfied = False
                        break

            if not properties_satisfied:
                break

        if properties_satisfied:
            results.append(module)

    return results


def analyze_property_types_and_ranges(selected_types):
    property_details = {}

    # Initialize query_ref with a reference to the collection
    query_ref = modules_collection

    # Query Firestore for documents of the selected types
    if selected_types:
        # Properly initialize query_ref before using it
        query_ref = query_ref.where(field_path='types', op_string='array_contains_any', value=selected_types)
        docs = query_ref.stream()

        # Analyze properties of each document
        for doc in docs:
            properties = doc.to_dict().get('properties', {})
            for prop, details in properties.items():
                # Assume numerical properties have a 'min' and 'max'
                if 'min' in details and 'max' in details:
                    # Update property details with min and max values seen
                    if prop not in property_details:
                        property_details[prop] = {'type': 'range', 'min': float('inf'), 'max': float('-inf')}
                    property_details[prop]['min'] = min(property_details[prop]['min'], float(details['min']))
                    property_details[prop]['max'] = max(property_details[prop]['max'], float(details['max']))
                else:
                    # Handle non-numerical properties
                    pass  # Add logic as needed for other property types

    return property_details

# Streamlit UI setup
st.set_page_config(page_title="Component Selection Interface", layout="wide")

# Title of the app
st.title('Component Selection Interface')

# Sidebar for search filters
st.sidebar.header('Search Filters')

# Get unique types from the database and initialize filters
unique_types = set()
numeric_filters = {}
selected_types = []

# Fetching unique types from Firestore and adding them individually
docs = modules_collection.stream()
for doc in docs:
    module = doc.to_dict()
    # print(module.get('types', []))
    for type_ in module.get('types', []):  # Iterate over individual types
        unique_types.add(type_)
        print(type_)


type_options = list(unique_types)
print(type_options)
selected_types = st.sidebar.multiselect('Type', type_options)

# Based on the selected types, create dynamic numeric filters
if selected_types:
    # Analyze available numeric properties
    property_details = analyze_property_types_and_ranges(selected_types)
    for prop, details in property_details.items():
        min_val, max_val = st.sidebar.slider(f'{prop} Range', details['min'], details['max'], (details['min'], details['max']))
        numeric_filters[prop] = (min_val, max_val)

# Search button
if st.sidebar.button('Search'):
    # Query the database
    results = query_modules(selected_types, numeric_filters)

    # Convert the results to a Pandas DataFrame for better display
    if results:
        # Flatten the interfaces for display purposes while preserving the original structure for sorting
        for r in results:
            r['interfaces_flat'] = '; '.join([f"{intf['name']}: {intf['voltage']['min']}V-{intf['voltage']['max']}V"
                                              for intf in r.get('interfaces', []) if intf['type'] == 'Power'])
        # Sort the results based on a custom logic, if needed

        df = pd.DataFrame(results)
        # Include only relevant columns for display
        df_display = df[['name', 'interfaces_flat', 'price']]  # Add more columns as needed
        # Display the results as an interactive table
        st.dataframe(df_display, use_container_width=True)
    else:
        st.write("No results found.")
