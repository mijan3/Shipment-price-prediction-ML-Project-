import sys
import numpy as np
import yaml
from shipment.exception import ShipmentException
from shipment.logger import logging

class MainUtils:
    def read_yaml_file(self,file_path:str)->dict:
        """
        Reads a YAML file and returns its contents as a dictionary.

        Args:
            file_path (str): The path to the YAML file.
        Returns:
            dict: The contents of the YAML file as a dictionary.
        Raises:
            ShipmentException: If there is an error reading the YAML file.
        """
        logging.info(f"Reading YAML file from path: {file_path}")
        try:
            with open(file_path, 'r') as yaml_file:
                content = yaml.safe_load(yaml_file)
            logging.info(f"Successfully read YAML file from path: {file_path}")
            return content
        except Exception as e:
            logging.error(f"Error occurred while reading YAML file from path: {file_path}")
            raise ShipmentException(str(e), sys.exc_info())
        
    def write_json_to_yaml_file(self,json_file:dict, yaml_file_path:str)->yaml:
        """
        Writes a JSON-like dictionary to a YAML file.

        Args:
            json_file (dict): The JSON-like dictionary to be written to the YAML file.
            yaml_file_path (str): The path where the YAML file will be saved.
        Returns:
            yaml: The YAML file object.
        Raises:
            ShipmentException: If there is an error writing the YAML file.
        """
        logging.info(f"Writing JSON to YAML file at path: {yaml_file_path}")
        try:
            with open(yaml_file_path, 'w') as yaml_file:
                yaml.dump(json_file, yaml_file)
            logging.info(f"Successfully wrote JSON to YAML file at path: {yaml_file_path}")
            return yaml_file
        except Exception as e:
            logging.error(f"Error occurred while writing JSON to YAML file at path: {yaml_file_path}")
            raise ShipmentException(str(e), sys.exc_info())
        
    def save_numpy_array_data(self, file_path: str, array: np.ndarray) -> None:
        """
        Saves a NumPy array to a file.

        Args:
            file_path (str): The path where the NumPy array will be saved.
            array (np.ndarray): The NumPy array to be saved.
        Returns:
            None
        Raises:
            ShipmentException: If there is an error saving the NumPy array.
        """
        logging.info(f"Saving NumPy array to file at path: {file_path}")
        try:
            np.save(file_path, array)
            logging.info(f"Successfully saved NumPy array to file at path: {file_path}")
        except Exception as e:
            logging.error(f"Error occurred while saving NumPy array to file at path: {file_path}")
            raise ShipmentException(str(e), sys.exc_info())
        
    def load_numpy_array_data(self, file_path: str) -> np.ndarray:
        """
        Loads a NumPy array from a file.

        Args:
            file_path (str): The path to the file where the NumPy array is saved.
        Returns:
            np.ndarray: The loaded NumPy array.
        Raises:
            ShipmentException: If there is an error loading the NumPy array.
        """
        logging.info(f"Loading NumPy array from file at path: {file_path}")
        try:
            array = np.load(file_path)
            logging.info(f"Successfully loaded NumPy array from file at path: {file_path}")
            return array
        except Exception as e:
            logging.error(f"Error occurred while loading NumPy array from file at path: {file_path}")
            raise ShipmentException(str(e), sys.exc_info())