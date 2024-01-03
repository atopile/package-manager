import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('atopile-880ca67acfe2.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

regulator_data = [
    # Flyback Regulator Example
    {
        "github-url": "https://example.com/packages/FB500",
        "name": "FB500",
        "version": "1.0.0",
        "description": "High-Efficiency Flyback Converter",
        "types": ["flyback", "regulator", "isolated"],
        "interfaces": [
            {
                "type": "Power",
                "name": "power_in",
                "direction": "input",
                "voltage": {"min": 85, "max": 265, "units": "V"},
                "current": {"min": 0, "max": 0.5, "units": "A"}
            },
            {
                "type": "Power",
                "name": "power_out",
                "direction": "output",
                "voltage": {"min": 12, "max": 12, "units": "V"},
                "current": {"min": 0, "max": 2, "units": "A"}
            }
        ],
        "price": 4.5,
        "image": "https://example.com/uploads/flyback_converter.png"
    },
    # Buck Regulator Example
    {
        "github-url": "https://example.com/packages/BK100",
        "name": "BK100",
        "version": "0.9.0",
        "description": "Compact Synchronous Buck Regulator",
        "types": [
            "type": "buck",
            "parent_types": ["regulator","adjustable-regulator"],
            "name": "buck1"
        "interfaces": [
            {
                "type": "Power",
                "name": "power_in",
                "direction": "input",
                "voltage": {"min": 4.5, "max": 28, "units": "V"},
                "current": {"min": 0, "max": 3, "units": "A"},
                "parent_types": ["buck1"]
            },
            {
                "type": "Power",
                "name": "power_out",
                "direction": "output",
                "voltage": {"min": 0.8, "max": 5, "units": "V"},
                "current": {"min": 0, "max": 5, "units": "A"},
                "parent_types": ["buck1"]
            }
        ],
        "price": 2.2,
        "image": "https://example.com/uploads/buck_regulator.png"
    },
    # Boost Regulator Example
    {
        "github-url": "https://example.com/packages/BS300",
        "name": "BS300",
        "version": "1.2.0",
        "description": "High-Voltage Boost Converter",
        "types": ["boost", "regulator"],
        "interfaces": [
            {
                "type": "Power",
                "name": "power_in",
                "direction": "input",
                "voltage": {"min": 2.7, "max": 4.2, "units": "V"},
                "current": {"min": 0, "max": 1, "units": "A"}
            },
            {
                "type": "Power",
                "name": "power_out",
                "direction": "output",
                "voltage": {"min": 5, "max": 12, "units": "V"},
                "current": {"min": 0, "max": 0.6, "units": "A"}
            }
        ],
        "price": 3.1,
        "image": "https://example.com/uploads/boost_converter.png"
    },
    # LDO Regulator Example
    {
        "github-url": "https://example.com/packages/LD200",
        "name": "LD200",
        "version": "0.8.5",
        "description": "Low Dropout Linear Regulator",
        "types": ["LDO", "regulator"],
        "interfaces": [
            {
                "type": "Power",
                "name": "power_in",
                "direction": "input",
                "voltage": {"min": 2.5, "max": 5.5, "units": "V"},
                "current": {"min": 0, "max": 0.5, "units": "A"}
            },
            {
                "type": "Power",
                "name": "power_out",
                "direction": "output",
                "voltage": {"min": 1.8, "max": 3.3, "units": "V"},
                "current": {"min": 0, "max": 0.3, "units": "A"}
            }
        ],
        "price": 0.5,
        "image": "https://example.com/uploads/ldo_regulator.png"
    },
    # LLC Resonant Converter Example
    {
        "github-url": "https://example.com/packages/LLC700",
        "name": "LLC700",
        "version": "1.1.0",
        "description": "Efficient LLC Resonant Converter",
        "types": ["llc", "regulator", "isolated"],
        "interfaces": [
            {
                "type": "Power",
                "name": "power_in",
                "direction": "input",
                "voltage": {"min": 100, "max": 240, "units": "V"},
                "current": {"min": 0, "max": 2, "units": "A"}
            },
            {
                "type": "Power",
                "name": "power_out",
                "direction": "output",
                "voltage": {"min": 12, "max": 12, "units": "V"},
                "current": {"min": 0, "max": 10, "units": "A"}
            }
        ],
        "price": 6.7,
        "image": "https://example.com/uploads/llc_converter.png"
    },
    # PMIC with multiple regulators Example
    {
        "github-url": "https://example.com/packages/TPS65313-Q1",
        "name": "TPS65313-Q1",
        "version": "2.0.0",
        "description": "Power Management IC with Multiple Buck and Boost Regulators",
        "types": ["PMIC", "regulator"],
        "interfaces": [
            {
                "type": "Power",
                "name": "buck1_power_in",
                "direction": "input",
                "voltage": {"min": 4, "max": 36, "units": "V"},
                "current": {"min": 0, "max": 3.1, "units": "A"}
            },
            {
                "type": "Power",
                "name": "buck1_power_out",
                "direction": "output",
                "voltage": {"min": 3.3, "max": 3.6, "units": "V"},
                "current": {"min": 0, "max": 3.1, "units": "A"}
            },
            # ... Additional buck and boost regulators
        ],
        "price": 7.9,
        "image": "https://example.com/uploads/TPS65313-Q1_pmic.png"
    }
    # Additional regulators can be added here...
]

# upload the regulator data to the database
for data in regulator_data:
    db.collection("packages").document(data["name"]).set(data)