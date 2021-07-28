# Write your code here. Good luck!
import json


def save_data(data, path):
    """Save data given path in JSON format."""
    with open(path, 'w') as json_file:
        json.dump(data, json_file)


def load_data(path):
    """Load data from file and return native Python object."""
    with open(path) as json_file:
        return json.load(json_file)
