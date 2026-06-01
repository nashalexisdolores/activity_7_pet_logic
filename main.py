import tkinter as tk
from pet_logic import pet_logic

class pet_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Registry v1.0")
        self.root.geometry("400x500")

    def __init__(self, root):
        self.root = root
        self.my_pet = pet_logic()
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="PET NAME:").pack(pady=5)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()

        tk.Label(self.root, text="ANIMAL TYPE (Dog, Cat, etc):").pack(pady=5)
        self.entry_type = tk.Entry(self.root)
        self.entry_type.pack()

        tk.Label(self.root, text="PET AGE:").pack(pady=5)
        self.entry_age = tk.Entry(self.root)
        self.entry_age.pack()

        self.btn_reg = tk.Button(self.root, text="REGISTER PET", command=self.handle_reg)
        self.btn_reg.pack(pady=20)

        self.display_card = tk.Label(self.root, text="Waiting for entry...", font=("Arial", 10))
        self.display_card.pack(pady=20)

    def handle_reg(self):
        self.my_pet.set_name(self.entry_name.get())
        self.my_pet.set_animal_type(self.entry_type.get())
        self.my_pet.set_age(self.entry_age.get())
        self.update_id_card()
