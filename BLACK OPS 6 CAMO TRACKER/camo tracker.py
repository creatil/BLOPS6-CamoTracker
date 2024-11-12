import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for handling images
from tkinter import ttk
import json
import os

weapon_data = {
    "assault rifles": {
        "XM4": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Muddled", "Machina"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
            },
        "AK-74": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Whitecap", "Vengeance"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
            },
        "AMES 85": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Heatstroke", "Burial"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
            },
        "GPR 91": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Ambush", "Cacti Cathode"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
            },
        "Model L": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"],
            "special": ["Cherry Blossom", "Cedar"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
            },
        "Goblin Mk2" : {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Astral Cry", "Hammerhead"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
            },
        "AS VAL": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Crimson Steppes", "Elk"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
            },
    },
    "smgs": {
        "C9": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Heatwave", "Panther"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"],
        },
        "KSV": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Kakapo", "Throwback"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"],
        },
        "Tanto .22": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Amorphous", "Go Bananas"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "PP-919": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Radiant Bath", "Midnight Prowl"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "Jackal PDW": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Deep End", "Dread"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "Kompakt 92": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Kingfisher", "Blackthorn"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        }
    },
    "Shotguns": {
        "Marine SP": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Blueberry Lime", "Chromed Out"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "ASG-89": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Night Terror", "Drive-In"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        }
    },
    "LMGs": {
        "PU-21": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Neon Bath", "Vigilance"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "XMG": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Buzz", "Snakebite"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "GPMG-7": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Brush Stroke", "Idyllic"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        }
    },
    "Marksman Rifles": {
        "SWAT 5.56": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Ectoplasm", "Lumberjack"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "Tsarkov 7.62": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Clear Water", "Concrete Jungle"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "AEK-973": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Ablaze", "Mirage"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "DM-10": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Mellowbloom", "Cobalt"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        }
    },
    "Sniper Riles": {
        "LW3A1 Frostline": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Copper", "Permafrost"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "SVD": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Pixelized", "Patchwork"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "LR 7.62": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Chaparral", "Nimbus"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        }
    },
    "Pistols": {
        "9mm PM": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Exabyte", "Blue Ring"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "Grekhova": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Spin", "Demeter"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "GS45": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Thistlevine", "Ragamuffin"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "Stryder .22": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Ritual", "Transcend"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        }
    },
    "Launchers": {
        "CIGMA 2B": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Policia", "Abstract"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "HE-1": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Reboot", "Dreamer"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        }
    },
    "Melee": {
        "Knife": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Dying Envy", "Tropical Leopard"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        },
        "Baseball Bat": {
            "military": ["Granite", "Woodland", "Savanna", "Splinter", "Moss", "Shade", "Digital", "Tide", "Red Tiger"], 
            "special": ["Torment", "Slip"], 
            "mastery": ["Gold", "Diamond", "Dark Spine", "Dark Matter"]
        }
    }
}

def get_save_file(mode):
    return f"camo_tracker_state_{mode.lower()}.json"

class CamoTracker:
    def __init__(self, root):
        # Set color properties as instance variables
        self.background_color = "#333333"        # Dark gray background color
        self.text_color = "#ff5500"              # Orange text color
        self.button_background_color = "#3e3e3e" # Lighter gray background for buttons

        self.title_image_path =  "images/blackops6logo.png"
        self.page_titles = {
            "Multiplayer": "images/multiplayer.png",
            "Zombies" : "images/zombies.png",
            "Warzone" : "images/warzone.png"
        }
        self.weapon_images = {
            "XM4" : "images/weapons/assault/XM4.png",
            "AK-74" : "images/weapons/assault/AK-74.png",
            "AMES 85" : "images/weapons/assault/AMES-85.png",
            "GPR 91" : "images/weapons/assault/GPR-91.png",
            "Model L" : "images/weapons/assault/Model-L.png",
            "Goblin Mk2" : "images/weapons/assault/Goblin-MK2.png",
            "AS VAL" : "images/weapons/assault/AS-VAL.png",
            "C9" : "images/weapons/smgs/C9.png",
            "KSV" : "images/weapons/smgs/KSV.png",
            "Tanto .22" : "images/weapons/smgs/Tanto-.22.png",
            "PP-919" : "images/weapons/smgs/PP-919.png",
            "Jackal PDW" : "images/weapons/smgs/Jackal-PDW.png",
            "Kompakt 92" : "images/weapons/smgs/Kompakt-92.png",
            "Marine SP" : "images/weapons/shotguns/Marine-SP.png",
            "ASG-89" : "images/weapons/shotguns/ASG-89.png",
            "PU-21" : "images/weapons/lmgs/PU-21.png",
            "XMG" : "images/weapons/lmgs/XMG.png",
            "GPMG-7" : "images/weapons/lmgs/GPMG-7.png",
            "SWAT 5.56" : "images/weapons/marksman/Swat-5.56.png",
            "Tsarkov 7.62" : "images/weapons/marksman/Tsarkov-7.62.png",
            "AEK-973" : "images/weapons/marksman/AEK-973.png",
            "DM-10" : "images/weapons/marksman/DM-10.png",
            "LW3A1 Frostline" : "images/weapons/snipers/Frostline.png",
            "SVD" : "images/weapons/snipers/SVD.png",
            "LR 7.62" : "images/weapons/snipers/LR-7.62.png",
            "9mm PM" : "images/weapons/pistols/9MM-PM.png",
            "Grekhova" : "images/weapons/pistols/Grekhova.png",
            "GS45" : "images/weapons/pistols/GS45.png",
            "Stryder .22" : "images/weapons/pistols/Stryder-.22.png",
            "CIGMA 2B" : "images/weapons/launchers/Cigma-2B.png",
            "HE-1" : "images/weapons/launchers/HE-1.png",
            "Knife" : "images/weapons/melee/Knife.png",
            "Baseball Bat" : "images/weapons/melee/Baseball-Bat.png",

         }

        self.title_img = Image.open(self.title_image_path)
        self.title_img = self.title_img.resize((400, 150), Image.Resampling.LANCZOS)
        self.title_photo = ImageTk.PhotoImage(self.title_img)

        self.root = root
        self.root.title("Black Ops 6 Camo Tracker")
        self.root.configure(bg=self.background_color)
        self.checkbox_states = {}
        self.button_width = 20
        self.main_menu()

    def calculate_progress(self, weapon_class):
        """Calculate the completion percentage for a weapon class."""
        completed = 0
        total = 0
        for weapon in weapon_data[weapon_class]:
            for camo_type, camos in weapon_data[weapon_class][weapon].items():
                for camo in camos:
                    total += 1
                    if self.checkbox_states.get(weapon_class, {}).get(weapon, {}).get(camo, False):
                        completed += 1
        return int((completed / total) * 100) if total > 0 else 0

    def save_checkbox_states(self, mode):
        save_file = get_save_file(mode)
        with open(save_file, "w") as file:
            json.dump(self.checkbox_states, file)

    def load_checkbox_states(self, mode):
        save_file = get_save_file(mode)
        if os.path.exists(save_file):
            with open(save_file, "r") as file:
                self.checkbox_states = json.load(file)
        else:
            self.checkbox_states = {}

    def main_menu(self):
        # Set a fixed size for the main menu
        window_width = max(self.title_photo.width(), 300)
        window_height = self.title_photo.height() + 400  # Increased height to accommodate Quit button
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)

        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Display the main menu title image
        title_label = tk.Label(self.root, image=self.title_photo, bg=self.background_color)
        title_label.image = self.title_photo
        title_label.pack(pady=20)

        # Display mode buttons
        for mode in ["Multiplayer", "Zombies", "Warzone"]:
            tk.Button(self.root, text=mode, width=self.button_width,
                    fg=self.text_color, bg=self.button_background_color, font=("Arial", 14),
                    command=lambda m=mode: self.show_weapon_classes(m)).pack(pady=10)
        
        # Settings button
        tk.Button(self.root, text="Settings", width=self.button_width,
                fg=self.text_color, bg=self.button_background_color, font=("Arial", 14),
                command=self.settings).pack(pady=10)

        # Quit button
        tk.Button(self.root, text="Quit", width=self.button_width,
                fg=self.text_color, bg=self.button_background_color, font=("Arial", 14),
                command=self.root.quit).pack(pady=10)

    def show_weapon_classes(self, mode):
        self.load_checkbox_states(mode)

        self.root.geometry("")
        self.root.resizable(True, True)

        for widget in self.root.winfo_children():
            widget.destroy()

        if mode in self.page_titles:
            try:
                title_img = Image.open(self.page_titles[mode])
                title_img = title_img.resize((400, 100), Image.Resampling.LANCZOS)
                title_photo = ImageTk.PhotoImage(title_img)
                title_label = tk.Label(self.root, image=title_photo, bg=self.background_color)
                title_label.image = title_photo
                title_label.pack(pady=20)
            except Exception as e:
                print(f"Error loading image for {mode}: {e}")
                tk.Label(self.root, text=f"{mode} - Select Weapon Class", font=("Arial", 20),
                         fg=self.text_color, bg=self.background_color).pack(pady=20)

        for weapon_class in weapon_data.keys():
            frame = tk.Frame(self.root, bg=self.background_color)
            frame.pack(pady=10)
            
            progress = self.calculate_progress(weapon_class)
            
            tk.Button(frame, text=weapon_class.title(), width=self.button_width,
                      fg=self.text_color, bg=self.button_background_color, font=("Arial", 14),
                      command=lambda wc=weapon_class: self.show_weapons(mode, wc)).pack(side="left", padx=5)
            
            progress_bar = ttk.Progressbar(frame, length=200, value=progress)
            progress_bar.pack(side="left", padx=10)

            tk.Label(frame, text=f"{progress}%", font=("Arial", 12),
                     fg=self.text_color, bg=self.background_color).pack(side="left")

        tk.Button(self.root, text="Back", width=self.button_width,
                  fg=self.text_color, bg=self.button_background_color, font=("Arial", 14),
                  command=self.main_menu).pack(pady=20)

    def show_weapons(self, mode, weapon_class):
        self.root.geometry("")
        self.root.resizable(True, True)

        for widget in self.root.winfo_children():
            widget.destroy()
        
        if mode in self.page_titles:
            try:
                title_img = Image.open(self.page_titles[mode])
                title_img = title_img.resize((400, 100), Image.Resampling.LANCZOS)
                title_photo = ImageTk.PhotoImage(title_img)
                title_label = tk.Label(self.root, image=title_photo, bg=self.background_color)
                title_label.image = title_photo
                title_label.pack(pady=20)
            except Exception as e:
                print(f"Error loading image for {mode}: {e}")
                tk.Label(self.root, text=f"{mode} - {weapon_class.title()} Weapons", font=("Arial", 20),
                         fg=self.text_color, bg=self.background_color).pack(pady=20)

        container = tk.Frame(self.root, bg=self.background_color)
        container.pack(fill="both", expand=True)
        
        canvas = tk.Canvas(container, height=400, width=600, bg=self.background_color)
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        frame = tk.Frame(canvas, bg=self.background_color)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        
        for weapon, camos in weapon_data[weapon_class].items():
            weapon_frame = tk.Frame(frame, bg=self.background_color)
            weapon_frame.pack(pady=5, padx=5, fill="x")
            tk.Label(weapon_frame, text=weapon, font=("Arial", 16), fg=self.text_color, bg=self.background_color).pack()
            
            if weapon in self.weapon_images:
                try:
                    weapon_img = Image.open(self.weapon_images[weapon])
                    weapon_img = weapon_img.resize((100, 100), Image.Resampling.LANCZOS)
                    weapon_photo = ImageTk.PhotoImage(weapon_img)
                    img_label = tk.Label(weapon_frame, image=weapon_photo, bg=self.background_color)
                    img_label.image = weapon_photo
                    img_label.pack(side="left", padx=10)
                except Exception as e:
                    print(f"Error loading image for weapon {weapon}: {e}")

            self.show_camos(mode, weapon_class, weapon, weapon_frame, camos)
        
        tk.Button(self.root, text="Back", width=self.button_width,
                  fg=self.text_color, bg=self.button_background_color, font=("Arial", 14),
                  command=lambda: self.show_weapon_classes(mode)).pack(pady=10)

    def show_camos(self, mode, weapon_class, weapon_name, parent, camos):
        military_frame = tk.Frame(parent, bg=self.background_color)
        military_frame.pack(side="left", padx=5, pady=5)

        special_frame = tk.Frame(parent, bg=self.background_color)
        special_frame.pack(side="left", padx=5, pady=5)

        mastery_frame = tk.Frame(parent, bg=self.background_color)
        mastery_frame.pack(side="left", padx=5, pady=5)
        
        tk.Label(military_frame, text="Military Camos", font=("Arial", 12), fg=self.text_color, bg=self.background_color).pack(anchor="w")
        tk.Label(special_frame, text="Special Camos", font=("Arial", 12), fg=self.text_color, bg=self.background_color).pack(anchor="w")
        tk.Label(mastery_frame, text="Mastery Camos", font=("Arial", 12), fg=self.text_color, bg=self.background_color).pack(anchor="w")
        
        military_complete = tk.BooleanVar(value=False)
        special_complete = tk.BooleanVar(value=False)
        
        for camo in camos["military"]:
            self.create_camo_checkbox(military_frame, mode, weapon_class, weapon_name, camo, military_complete, None)
        
        for camo in camos["special"]:
            self.create_camo_checkbox(special_frame, mode, weapon_class, weapon_name, camo, special_complete, lambda: military_complete.get())
        
        for camo in camos["mastery"]:
            self.create_camo_checkbox(mastery_frame, mode, weapon_class, weapon_name, camo, None, lambda: special_complete.get())

    def create_camo_checkbox(self, parent, mode, weapon_class, weapon_name, camo_name, complete_var, condition_fn):
        var = tk.BooleanVar(value=self.checkbox_states.get(weapon_class, {}).get(weapon_name, {}).get(camo_name, False))
        
        def on_check():
            if var.get() and condition_fn and not condition_fn():
                messagebox.showwarning("Locked", f"Complete previous camos to unlock {camo_name}")
                var.set(False)
            else:
                self.checkbox_states.setdefault(weapon_class, {}).setdefault(weapon_name, {})[camo_name] = var.get()
                self.save_checkbox_states(mode)
                if complete_var:
                    complete_var.set(var.get())
        
        checkbox = tk.Checkbutton(parent, text=camo_name, variable=var, onvalue=True, offvalue=False,
                                  command=on_check, fg=self.text_color, bg=self.background_color)
        checkbox.pack(anchor="w", padx=5, pady=2)

    def settings(self):
        # Clear the main window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display a title for the settings page
        tk.Label(self.root, text="Settings", font=("Arial", 20),
                 fg=self.text_color, bg=self.background_color).pack(pady=20)

        # Add a "Back" button to return to the main menu
        tk.Button(self.root, text="Back", width=self.button_width,
                  fg=self.text_color, bg=self.button_background_color, font=("Arial", 14),
                  command=self.main_menu).pack(pady=10)

root = tk.Tk()
app = CamoTracker(root)
root.mainloop()