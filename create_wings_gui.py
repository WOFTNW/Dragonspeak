import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog, messagebox

class WingTextureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wing Texture and Model Generator")

        # Create labels and buttons for item file selection
        tk.Label(root, text="Select Item PNG File:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.item_path_entry = tk.Entry(root, width=50)
        self.item_path_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(root, text="Browse", command=self.select_item_file).grid(row=0, column=2, padx=10, pady=5)

        # Create labels and buttons for equipment file selection
        tk.Label(root, text="Select Equipment PNG File:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.equipment_path_entry = tk.Entry(root, width=50)
        self.equipment_path_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(root, text="Browse", command=self.select_equipment_file).grid(row=1, column=2, padx=10, pady=5)

        # Create entry for item name
        tk.Label(root, text="Enter Item Name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create entry for target subpath
        tk.Label(root, text="Enter Subpath (e.g., tribes/mud):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.subpath_entry = tk.Entry(root, width=50)
        self.subpath_entry.grid(row=3, column=1, padx=10, pady=5)

        # Create generate button
        tk.Button(root, text="Generate Files", command=self.generate_files).grid(row=4, column=1, pady=20)

    def select_item_file(self):
        item_file = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if item_file:
            self.item_path_entry.delete(0, tk.END)
            self.item_path_entry.insert(0, item_file)

    def select_equipment_file(self):
        equipment_file = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if equipment_file:
            self.equipment_path_entry.delete(0, tk.END)
            self.equipment_path_entry.insert(0, equipment_file)

    def generate_files(self):
        try:
            # Retrieve inputs
            item_file_path = self.item_path_entry.get().strip()
            equipment_file_path = self.equipment_path_entry.get().strip()
            name = self.name_entry.get().strip()
            target_subpath = self.subpath_entry.get().strip()

            if not all([item_file_path, equipment_file_path, name, target_subpath]):
                messagebox.showerror("Error", "All fields must be filled out.")
                return

            formatted_name = name.replace(" ", "_").lower()
            
            # Define target directories
            item_target_dir = f"./assets/minecraft/textures/item/wings/{target_subpath}/"
            equipment_target_dir = f"./assets/minecraft/textures/entity/equipment/wings/{target_subpath}/"
            item_model_def_target_dir = f"./assets/minecraft/items/wings/{target_subpath}/"
            item_model_target_dir = f"./assets/minecraft/models/item/wings/{target_subpath}/"
            equipment_model_target_dir = f"./assets/minecraft/equipment/wings/{target_subpath}/"
            
            # Create target directories if they don't exist
            os.makedirs(item_target_dir, exist_ok=True)
            os.makedirs(equipment_target_dir, exist_ok=True)
            os.makedirs(item_model_def_target_dir, exist_ok=True)
            os.makedirs(item_model_target_dir, exist_ok=True)
            os.makedirs(equipment_model_target_dir, exist_ok=True)
            
            # Move the item PNG file
            item_target_path = os.path.join(item_target_dir, f"{formatted_name}.png")
            shutil.copy(item_file_path, item_target_path)
            
            # Move the equipment PNG file
            equipment_target_path = os.path.join(equipment_target_dir, f"{formatted_name}.png")
            shutil.copy(equipment_file_path, equipment_target_path)
            
            # Create item model definition JSON content
            item_model_def_data = {
                "model": {
                    "type": "minecraft:model",
                    "layer0": f"minecraft:item/wings/{target_subpath}/{formatted_name}"
                }
            }

            # Create item model JSON content
            item_model_data = {
                "parent": "item/generated",
                "textures": {
                    "layer0": f"minecraft:item/wings/{target_subpath}/{formatted_name}"
                }
            }
            
            # Write item model definition JSON file
            item_model_def_file_path = os.path.join(item_model_def_target_dir, f"{formatted_name}.json")
            with open(item_model_def_file_path, "w") as json_file:
                json.dump(item_model_def_data, json_file, indent=4)

            # Write item model JSON file
            item_model_file_path = os.path.join(item_model_target_dir, f"{formatted_name}.json")
            with open(item_model_file_path, "w") as json_file:
                json.dump(item_model_data, json_file, indent=4)
            
            # Create equipment JSON content
            equipment_model_data = {
                "layers": {
                    "wings": [
                        {
                            "texture": f"minecraft:{target_subpath}/{formatted_name}"
                        }
                    ]
                }
            }
            
            # Write equipment JSON file
            equipment_model_file_path = os.path.join(equipment_model_target_dir, f"{formatted_name}.json")
            with open(equipment_model_file_path, "w") as json_file:
                json.dump(equipment_model_data, json_file, indent=4)

            messagebox.showinfo("Success", "Files generated successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WingTextureApp(root)
    root.mainloop()
