import tkinter as tk
from tkinter import PhotoImage
import requests
from PIL import Image, ImageTk
from io import BytesIO

class FoxImageGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор картинок с лисами")

        self.button = tk.Button(root, text="Показать следующую картинку", command=self.load_new_image)
        self.button.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.load_new_image()

    def load_new_image(self):
        response = requests.get("https://randomfox.ca/floof/")
        data = response.json()

        image_url = data['image']

        image_response = requests.get(image_url)
        image_data = Image.open(BytesIO(image_response.content))

        self.photo = ImageTk.PhotoImage(image_data)

        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo

if __name__ == "__main__":
    root = tk.Tk()
    app = FoxImageGenerator(root)
    root.mainloop()