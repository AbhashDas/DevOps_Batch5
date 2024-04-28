import json  # Import the json module for JSON handling
import configparser  # Import the configparser module for reading configuration files
from flask import Flask, jsonify  # Import Flask for creating the web server and jsonify for JSON responses

app = Flask(__name__)  # Create a Flask application instance

def parse_configuration_file(file_path):
    """
    Parse the configuration file and return the data as a dictionary.   
    Args:
        file_path (str): Path to the configuration file.    
    Returns:
        dict: Parsed configuration data.
    """
    parsed_data = {}  # Initialize an empty dictionary to store parsed data
    try:
        config = configparser.ConfigParser()  # Create a ConfigParser instance
        config.read(file_path)  # Read the configuration file
        for section in config.sections():  # Iterate over sections in the configuration file
            parsed_data[section] = {}  # Create a dictionary for each section
            for key, value in config.items(section):  # Iterate over key-value pairs in each section
                parsed_data[section][key] = value  # Add key-value pair to the section dictionary
        return parsed_data  # Return the parsed data
    except FileNotFoundError as e:  # Catch FileNotFoundError
        print(f"Configuration file '{file_path}' not found.")  # Print error message
        return None  # Return None
    except Exception as e:  # Catch other exceptions
        print(f"Error reading configuration file: {e}")  # Print error message
        return None  # Return None

def save_to_json(data, output_file):
    """
    Save data to a JSON file.   
    Args:
        data (dict): Data to be saved.
        output_file (str): Path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:  # Open the output JSON file in write mode
            json.dump(data, json_file, indent=4)  # Write the data to the JSON file with indentation
        print(f"Data saved to {output_file}")  # Print success message
    except Exception as e:  # Catch any exceptions
        print(f"Error saving data to JSON file: {e}")  # Print error message

@app.route('/config_data.json')  # Define a route for fetching configuration data
def get_config_data():
    """
    Handle GET request for fetching configuration data.    
    Returns:
        JSON: Configuration data in JSON format.
    """
    config_data = parse_configuration_file('ansible.cfg')  # Parse the configuration file
    if config_data:  # If configuration data is successfully parsed
        return jsonify(config_data)  # Return the configuration data as JSON
    else:  # If there was an error parsing the configuration file
        print("Failed to fetch configuration data")  # Print error message
        return jsonify({"error": "Failed to fetch configuration data"})  # Return error message as JSON

if __name__ == "__main__":  # Check if the script is executed directly
    config_file = 'ansible.cfg'  # Set the path to the configuration file
    output_file = 'config_data.json'  # Set the path to the output JSON file
    parsed_data = parse_configuration_file(config_file)  # Parse the configuration file
    if parsed_data:  # If configuration data is successfully parsed
        print("Configuration File Parser Results:")  # Print section headers
        for section, data in parsed_data.items():  # Iterate over sections and data
            print(f"\n{section}:")  # Print section header
            for key, value in data.items():  # Iterate over key-value pairs in each section
                print(f"- {key}: {value}")  # Print key-value pairs
        save_to_json(parsed_data, output_file)  # Save parsed data to JSON file
    else:  # If there was an error parsing the configuration file
        print("Error: Configuration file not found or could not be read.")  # Print error message
    
    app.run(port=8080)  # Run the Flask application on port 8080
