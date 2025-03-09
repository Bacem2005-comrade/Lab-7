import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# Твой API-ключ от NASA (можно получить бесплатно на https://api.nasa.gov)
API_KEY = "3j1ygBXflcLOmQcANRvLaHEJYUFc0HYQqtcddHsv"
NASA_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

# Функция для загрузки фото дня
def load_nasa_image():
    response = requests.get(NASA_URL)
    if response.status_code == 200:
        data = response.json()
        img_url = data["url"]
        explanation = data.get("explanation", "No description available.")

        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.resize((600, 400), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img_data)

            label_img.config(image=img_tk)
            label_img.image = img_tk
            label_text.config(text=explanation[:200] + "...")  # Обрезаем текст для компактности
    else:
        label_text.config(text="❌ Error loading image.")

# Создаём GUI окно
window = tk.Tk()
window.title("NASA APOD Viewer 🚀")
window.geometry("650x550")

label_img = tk.Label(window)
label_img.pack()

label_text = tk.Label(window, text="Loading image...", wraplength=600, justify="center")
label_text.pack(pady=10)

btn_load = tk.Button(window, text="🔄 Load New Image", command=load_nasa_image)
btn_load.pack(pady=10)

# Загружаем первое изображение
load_nasa_image()

window.mainloop()
