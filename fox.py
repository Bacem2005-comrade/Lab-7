import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def get_image():
    """Fetches a random fox image from the API and displays it in the Tkinter window."""
    response = requests.get("https://randomfox.ca/floof/")
    if response.status_code == 200:
        data = response.json()
        image_url = data["image"]

        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.resize((400, 300), Image.Resampling.LANCZOS) # Resize the image for better display
            img_tk = ImageTk.PhotoImage(img_data)  # Convert to Tkinter-compatible image

            label_image.config(image=img_tk)  # Update the label with the new image
            label_image.image = img_tk # Keep a reference to the image to prevent garbage collection
        else:
            print("Error getting image data")
    else:
        print("Error to get image URL")

# --- Tkinter setup ---
window = tk.Tk()
window.title("Fox image generator 🦊")  # Set the window title
window.geometry("450x400")  # Set the window size

label_image = tk.Label(window)  # Create a Label to display the image
label_image.pack()  # Pack the label into the window

change_button = tk.Button(window, text="🔄 New image", command=get_image)  # Create a button to fetch a new image
change_button.pack(pady=10)  # Pack the button with some padding

get_image()  # Load an initial image when the program starts

window.mainloop()  # Start the Tkinter event loop