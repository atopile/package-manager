import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Path to your service account key
service_account_path = 'atopile-880ca67acfe2.json'

# Initialize Firestore
if not firebase_admin._apps:  # Check if already initialized to prevent reinitialization
    cred = credentials.Certificate(service_account_path)
    app = firebase_admin.initialize_app(cred)

db = firestore.client()
modules_collection = db.collection('packages')  # Replace 'modules' with your actual collection name

def query_modules(selected_types, properties_filters):
    results = []

    # Step 1: Fetch documents that match any of the selected types
    if selected_types:
        query_ref = modules_collection.where('types', 'array_contains_any', selected_types)
        potential_matches = query_ref.stream()

        # Step 2: Filter documents on the client side
        for doc in potential_matches:
            module = doc.to_dict()
            module_types = set(module.get('types', []))

            # Check if module contains all selected types
            if all(t in module_types for t in selected_types):
                # Apply additional property filters (client-side)
                matches_all_properties = True
                for prop, value_range in properties_filters.items():
                    # ... perform your range checks and set 'matches_all_properties' ...
                    pass

                if matches_all_properties:
                    results.append(module)

    return results

st.set_page_config(page_title='ato packages', layout='wide')

# Title of the app
st.title('Component Selection Interface')

st.sidebar.image('ato-logo.png', use_column_width=True)

# Sidebar for search filters
st.sidebar.header('Search Filters')

# Get unique types from the database and initialize filters
unique_types = set()
properties_filters = {}
selected_types = []

try:
    # Fetching all types from Firestore (you might want to cache this)
    docs = modules_collection.stream()
    for doc in docs:
        module = doc.to_dict()
        unique_types.update(module.get('types', []))
        # print(unique_types)

    type_options = list(unique_types)
    selected_types = st.sidebar.multiselect('Type', type_options)

    # Initialize filters based on selected types (this could be more dynamic)
    if selected_types:
        # Example of setting up a voltage range filter
        voltage_min = st.sidebar.number_input('Min Voltage', 0, 100, 0)
        voltage_max = st.sidebar.number_input('Max Voltage', 0, 100, 100)
        properties_filters['voltage'] = {'min': voltage_min, 'max': voltage_max}

except Exception as e:
    st.sidebar.write('Error fetching types or setting up filters:', e)

# Search button
if st.sidebar.button('Search'):
    # Query the database
    results = query_modules(selected_types, properties_filters)

    # Convert the results to a Pandas DataFrame for better display
    if results:
        # Flatten the properties into the top level of the JSON
        for r in results:
            r.update(r.get('properties', {}))
            r.pop('properties', None)  # Remove the nested properties dictionary

        df = pd.DataFrame(results)
        # Display the results as an interactive table
        st.dataframe(df, use_container_width=True)
    else:
        st.write("No results found.")
