# prepared import of enumerations
from model import Color, FuelType, Manufacturer, Transmission, Vehicle
# prepared csv module import
import csv
from typing import List

class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path



    def import_vehicles_from_file(self, file_path):
        # TODO read vehicle-list.csv and transform to String array
        return 

    def rewrite_file(self, vehicle_list):
        # TODO write back into vehicle-list.csv and transform to String array
	    # TODO call method prepare_the_vehicle_for_rewriting(String, Vehicle)
        return

    def prepare_the_vehicle_for_rewriting(self, vehicle_string_for_rewrite, vehicle):
        #  TODO add vehicle attribute information to vehicle_string_for_rewrite
		# Hint: vehicle_string_for_rewrite.join(String)
        return vehicle_string_for_rewrite


class VehicleShopPrinter:
    
    def print_available_vehicles(self, vehicle_list):
        # TODO Implement print available vehicles
        pass
    
    def print_vehicle_sold_message(self, vehicle_chosen_id):
        print("\nVehicle with ID", vehicle_chosen_id, "was sold.")
    
    def print_vehicle_id_to_sell_message(self):
        print("\n\n Please enter the number (ID) of the vehicle you want to sell: ")



class VehicleShopProcessor:

    # responsible to sell a specified vehicle by id

    def sell_vehicle(self, vehicle_list, selected_vehicle_id):
    # TODO selling a vehicle means to remove it from the available vehicle list
        pass

class VehicleTransformer:

    # transforms a data array into a {@link Vehicle} list 
	# @param vehicle data array
	# @return list of {@link Vehicle} objects

    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_string_array: List[str]) -> List[Vehicle]:
        # TODO take data from String list and transform to list of vehicle objects
        # TODO call method transformToVehicleObject
        # Hint: use for loop
        pass

    # transforms a vehicle data record as String into a {@link Vehicle} object
	# @param vehicle data record as String 
	# @return {@link Vehicle} object 
    
    def transform_to_vehicle_object(self, vehicle_as_string_array: str) -> Vehicle: 
        # TODO transform the vehicle as string into a vehicle object
        vehicle_list = []
        vehicle_id = int(vehicle_as_string_array[0])
        manufacturer = self.get_manufacturer_from_string(vehicle_as_string_array[1])

        vehicle = Vehicle(vehicle_id, manufacturer)
        return vehicle
    
    # Example for Enumeration processing to use for all other Enumerations
    def get_manufacturer_from_string(self, manufacturer_as_string):
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer
            
        raise ValueError("Manufacturer not supported: " + manufacturer_as_string)


