import os
import json


def get_data(file_name: str) -> dict:
    """
    Opens a JSON file from the data directory of the project.
    :param file_name: The name of the configuration file (without extension)
    :return: A dictionary containing the parsed JSON data
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    data_file_path = os.path.join(current_dir, 'data', f'{file_name}.json')

    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        return json.load(data_file)  # Returns a dictionary
