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
