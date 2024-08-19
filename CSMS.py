import json
import os

class CropAndSoilManagementSystem:
    def __init__(self):
        self.data_file = 'farmer_data.json'
        self.farmer_data = self.load_data()

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.farmer_data, f, indent=4)
        print("Data saved successfully.")

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}

    def add_farmer_data(self):
        farmer_id = input("Enter Farmer ID: ")
        crop_type = input("Enter Crop Type: ")
        soil_type = input("Enter Soil Type: ")
        disease_history = input("Enter Disease History (if any): ")
        self.farmer_data[farmer_id] = {
            'crop_type': crop_type,
            'soil_type': soil_type,
            'disease_history': disease_history
        }
        self.save_data()

    def retrieve_farmer_data(self):
        farmer_id = input("Enter Farmer ID to retrieve data: ")
        if farmer_id in self.farmer_data:
            print(f"Data for Farmer ID {farmer_id}: {self.farmer_data[farmer_id]}")
        else:
            print("Farmer data not found.")

    def update_farmer_data(self):
        farmer_id = input("Enter Farmer ID to update data: ")
        if farmer_id in self.farmer_data:
            crop_type = input("Enter new Crop Type: ")
            soil_type = input("Enter new Soil Type: ")
            disease_history = input("Enter new Disease History (if any): ")
            self.farmer_data[farmer_id] = {
                'crop_type': crop_type,
                'soil_type': soil_type,
                'disease_history': disease_history
            }
            self.save_data()
        else:
            print("Farmer data not found.")

    def delete_farmer_data(self):
        farmer_id = input("Enter Farmer ID to delete data: ")
        if farmer_id in self.farmer_data:
            del self.farmer_data[farmer_id]
            self.save_data()
            print("Farmer data deleted successfully.")
        else:
            print("Farmer data not found.")
            
    def recommend_crops(self):
        soil_type = input("Enter Soil Type: ")
        climate = input("Enter Climate (e.g., tropical, temperate, arid): ")

        recommendations = {
            'loamy': {
                'tropical': ['Rice', 'Sugarcane', 'Maize'],
                'temperate': ['Wheat', 'Barley', 'Potatoes'],
                'arid': ['Millet', 'Sorghum', 'Chickpeas']
            },
            'clay': {
                'tropical': ['Paddy', 'Jute', 'Sugarcane'],
                'temperate': ['Oats', 'Potato', 'Barley'],
                'arid': ['Cotton', 'Sesame', 'Legumes']
            },
            'sandy': {
                'tropical': ['Coconut', 'Cashew', 'Groundnut'],
                'temperate': ['Carrots', 'Peppers', 'Tomatoes'],
                'arid': ['Millets', 'Cactus', 'Dates']
            },
            'silt': {
                'tropical': ['Paddy', 'Soybean', 'Bananas'],
                'temperate': ['Wheat', 'Maize', 'Peas'],
                'arid': ['Sorghum', 'Barley', 'Sunflower']
            },
            'peaty': {
                'tropical': ['Tea', 'Spices', 'Sugarcane'],
                'temperate': ['Berries', 'Root Vegetables', 'Cabbage'],
                'arid': ['None (Peaty soil is usually not found in arid climates)']
            }
        }

        if soil_type in recommendations and climate in recommendations[soil_type]:
            print(f"Recommended Crops: {', '.join(recommendations[soil_type][climate])}")
        else:
            print("No recommendations available for this combination.")
            
    def monitor_soil_health(self):
        ph_level = float(input("Enter Soil pH Level: "))
        nitrogen = float(input("Enter Nitrogen content (mg/kg): "))
        phosphorus = float(input("Enter Phosphorus content (mg/kg): "))
        potassium = float(input("Enter Potassium content (mg/kg): "))

        if ph_level < 5.5:
            print("Soil is too acidic. Consider adding lime.")
        elif ph_level > 7.5:
            print("Soil is too alkaline. Consider adding sulfur.")

        if nitrogen < 20:
            print("Low nitrogen content. Consider adding organic compost or nitrogen fertilizers.")
        if phosphorus < 30:
            print("Low phosphorus content. Consider adding bone meal or phosphate fertilizers.")
        if potassium < 200:
            print("Low potassium content. Consider adding potash or potassium-rich fertilizers.")
            
    def identify_disease(self):
        symptoms = input("Enter observed symptoms (e.g., yellowing leaves, stunted growth): ").lower()

        disease_database = {
            'yellowing leaves': 'Nitrogen Deficiency',
            'stunted growth': 'Phosphorus Deficiency',
            'black spots': 'Fungal Infection',
            'wilting': 'Verticillium Wilt',
            'leaf curl': 'Leaf Curl Virus',
            'root rot': 'Root Rot Disease',
            'white powdery spots': 'Powdery Mildew',
            'brown patches': 'Brown Patch Disease',
            'rust spots': 'Rust Disease'
        }

        management_tips = {
            'Nitrogen Deficiency': 'Apply nitrogen-rich fertilizers like urea or ammonium sulfate.',
            'Phosphorus Deficiency': 'Use phosphorus-rich fertilizers like superphosphate.',
            'Fungal Infection': 'Apply fungicides and ensure proper crop spacing for air circulation.',
            'Verticillium Wilt': 'Rotate crops and avoid planting in infected soil.',
            'Leaf Curl Virus': 'Control aphids, which are the primary carriers, using insecticides.',
            'Root Rot Disease': 'Improve drainage and avoid overwatering.',
            'Powdery Mildew': 'Use sulfur-based fungicides and remove affected plant parts.',
            'Brown Patch Disease': 'Improve air circulation and avoid excessive watering.',
            'Rust Disease': 'Apply appropriate fungicides and avoid overhead irrigation.'
        }

        if symptoms in disease_database:
            disease = disease_database[symptoms]
            print(f"Possible Disease: {disease}")
            print(f"Suggested Management: {management_tips[disease]}")
        else:
            print("No matching disease found. Consult an expert for further diagnosis.")
            
    def pest_control_advisory(self):
        crop_type = input("Enter Crop Type: ")

        pest_database = {
            'Wheat': ['Aphids', 'Armyworms', 'Wheat Stem Sawfly'],
            'Rice': ['Stem Borer', 'Leaf Folder', 'Rice Weevil'],
            'Maize': ['Fall Armyworm', 'Corn Earworm', 'Rootworm'],
            'Cotton': ['Bollworm', 'Whitefly', 'Aphids'],
            'Soybean': ['Soybean Aphid', 'Japanese Beetle', 'Cutworms'],
            'Potato': ['Potato Beetle', 'Wireworms', 'Leafhoppers'],
            'Tomato': ['Tomato Hornworm', 'Whiteflies', 'Spider Mites'],
            'Cabbage': ['Cabbage Worm', 'Aphids', 'Flea Beetles'],
            'Sugarcane': ['Sugarcane Borer', 'Termites', 'Sugarcane Aphid'],
            'Paddy': ['Brown Planthopper', 'Leafhopper', 'Stem Borer']
        }

        if crop_type in pest_database:
            print(f"Common pests for {crop_type}: {', '.join(pest_database[crop_type])}")
            print("Suggested Control Measures: Use recommended pesticides, practice crop rotation, and ensure proper field sanitation.")
        else:
            print("No pest data available for this crop type.")
            
    def economic_analysis(self):
        crop_type = input("Enter Crop Type: ")
        cost = float(input("Enter Total Cost of Production: "))
        expected_price = float(input("Enter Expected Market Price per Quintal: "))
        estimated_yield = float(input("Enter Estimated Yield (in quintals): "))

        profit = (expected_price * estimated_yield) - cost
        print(f"Expected Profit for {crop_type}: {profit}")
        if profit > 0:
            print("This crop is expected to be profitable.")
        else:
            print("This crop may not be profitable. Consider revising your plan.")

        
    def menu(self):
        while True:
            print("\nCrop and Soil Management System:")
            print("1. Add Farmer Data")
            print("2. Retrieve Farmer Data")
            print("3. Update Farmer Data")
            print("4. Delete Farmer Data")
            print("5. Recommend Crops")
            print("6. Monitor Soil Health")
            print("7. Identify Disease")
            print("8. Pest Control Advisory")
            print("9. Economic Analysis")
            print("10. Exit")

            choice = input("Enter your choice (1-10): ")

            if choice == '1':
                self.add_farmer_data()
            elif choice == '2':
                self.retrieve_farmer_data()
            elif choice == '3':
                self.update_farmer_data()
            elif choice == '4':
                self.delete_farmer_data()
            elif choice == '5':
                self.recommend_crops()
            elif choice == '6':
                self.monitor_soil_health()
            elif choice == '7':
                self.identify_disease()
            elif choice == '8':
                self.pest_control_advisory()
            elif choice == '9':
                self.economic_analysis()
            elif choice == '10':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

system = CropAndSoilManagementSystem()
system.menu()