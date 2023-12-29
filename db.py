import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('atopile-880ca67acfe2.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

regulator_data = [
    {
        "github-url": "https://gitlab.atopile.io/packages/LTR500",
        "name": "LTR500",
        "version": "0.1.0",
        "description": "Linear Regulator",
        "types": ["linear", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 2,
        "voltage_in_max": 6,
        "voltage_out_min": 1.5,
        "voltage_out_max": 5,
        "current_max_A": 0.5,
        "price": 0.3,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/1/linear.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/BCK100",
        "name": "BCK100",
        "version": "0.1.0",
        "description": "Buck Converter",
        "types": ["buck", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 4,
        "voltage_in_max": 20,
        "voltage_out_min": 1,
        "voltage_out_max": 15,
        "current_max_A": 1,
        "price": 0.7,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/2/buck.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/BST150",
        "name": "BST150",
        "version": "0.1.0",
        "description": "Boost Converter",
        "types": ["boost", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 0.9,
        "voltage_in_max": 5,
        "voltage_out_min": 5,
        "voltage_out_max": 12,
        "current_max_A": 1.5,
        "price": 0.6,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/3/boost.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/BB200",
        "name": "BB200",
        "version": "0.1.0",
        "description": "Buck-Boost Converter",
        "types": ["buck-boost", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 3,
        "voltage_in_max": 12,
        "voltage_out_min": 1,
        "voltage_out_max": 10,
        "current_max_A": 2,
        "price": 1,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/4/buck-boost.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/FLY300",
        "name": "FLY300",
        "version": "0.1.0",
        "description": "Flyback Converter",
        "types": ["flyback", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 10,
        "voltage_in_max": 50,
        "voltage_out_min": 5,
        "voltage_out_max": 45,
        "current_max_A": 3,
        "price": 1.5,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/5/flyback.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/LLC400",
        "name": "LLC400",
        "version": "0.1.0",
        "description": "LLC Converter",
        "types": ["llc", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 20,
        "voltage_in_max": 60,
        "voltage_out_min": 15,
        "voltage_out_max": 55,
        "current_max_A": 4,
        "price": 2,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/6/llc.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/LTR700",
        "name": "LTR700",
        "version": "0.1.0",
        "description": "Advanced Linear Regulator",
        "types": ["linear", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 3,
        "voltage_in_max": 7,
        "voltage_out_min": 1.8,
        "voltage_out_max": 6.5,
        "current_max_A": 0.7,
        "price": 0.5,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/7/advanced-linear.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/BCK500",
        "name": "BCK500",
        "version": "0.1.0",
        "description": "High Power Buck Converter",
        "types": ["buck", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 5,
        "voltage_in_max": 30,
        "voltage_out_min": 3,
        "voltage_out_max": 20,
        "current_max_A": 5,
        "price": 1.2,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/8/high-buck.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/BST250",
        "name": "BST250",
        "version": "0.1.0",
        "description": "High Efficiency Boost Converter",
        "types": ["boost", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 1,
        "voltage_in_max": 4,
        "voltage_out_min": 5,
        "voltage_out_max": 25,
        "current_max_A": 2.5,
        "price": 0.8,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/9/high-boost.png"
    },
    {
        "github-url": "https://gitlab.atopile.io/packages/BB300",
        "name": "BB300",
        "version": "0.1.0",
        "description": "Adjustable Buck-Boost Converter",
        "types": ["buck-boost", "regulator"],
        "interfaces": ["Power_in", "Power_out"],
        "voltage_in_min": 2,
        "voltage_in_max": 15,
        "voltage_out_min": 1.5,
        "voltage_out_max": 13,
        "current_max_A": 3,
        "price": 1.3,
        "image": "https://gitlab.atopile.io/uploads/-/system/project/avatar/10/adjust-buck-boost.png"
    }
]

# # Add a new doc in collection 'cities' with ID 'LA'
# db.collection("packages").document("nrf52840").set(data_nrf)
# db.collection("packages").document("ldk220M").set(data_ldo)

# upload the regulator data to the database
for data in regulator_data:
    db.collection("packages").document(data["name"]).set(data)