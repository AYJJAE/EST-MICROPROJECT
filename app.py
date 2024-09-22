import tkinter as tk
from PIL import Image, ImageTk
import requests
import time
from tkinter import messagebox

def getWeather(event=None):
    city = textField.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=06c921750b9a82d8f5d1294e1586276f"
    
    try:
        json_data = requests.get(api).json()
        
        if json_data.get('cod') != 200:
            messagebox.showerror("Error", "City not found!")
            return
        
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = f"{condition}\n{temp}°C"
        final_data = (f"Min Temp: {min_temp}°C\nMax Temp: {max_temp}°C\n"
                      f"Pressure: {pressure}\nHumidity: {humidity}\n"
                      f"Wind Speed: {wind} m/s\nSunrise: {sunrise}\nSunset: {sunset}")
        
        label1.config(text=final_info)
        label2.config(text=final_data)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to retrieve data: {e}")

canvas = tk.Tk()
canvas.geometry("1080x1920")
canvas.title("Weather App - Group 4")

background_image_path = r"C:\Users\aarya\Desktop\EST MICROPROJECT\weather.jpg"
try:
    bg_image = Image.open(background_image_path)
    bg_image = bg_image.resize((1920, 1080), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load background image: {e}")
    bg_photo = None

if bg_photo:
    background_label = tk.Label(canvas, image=bg_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_font = ("Outfit Bold", 30)
weather_font = ("Outfit SemiBold", 17)
input_font = ("Outfit SemiBold", 37)

transparent_color = "#FFFFFF"

group_label = tk.Label(canvas, text="EST MICROPROJECT GROUP 4 TYEJ", font=title_font, fg="black", bg=transparent_color)
group_label.pack(pady=10)

names_label = tk.Label(canvas, text="Names: Aarya Joshi, Monish Shah, Krish Salian, Yash Vyas", font=("Outfit SemiBold", 20), fg="black", bg=transparent_color)
names_label.pack(pady=10)

frame = tk.Frame(canvas, bg="#D3D3D3", bd=5, padx=20, pady=20, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor='center')

textField = tk.Entry(frame, justify='center', width=20, font=input_font, bd=3)
textField.grid(row=0, column=0, pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(frame, font=input_font, bg="#D3D3D3", fg="black")
label1.grid(row=1, column=0, pady=10)

label2 = tk.Label(frame, font=weather_font, bg="#D3D3D3", fg="black")
label2.grid(row=2, column=0, pady=10)

exit_button = tk.Button(frame, text="Exit", command=canvas.quit, font=weather_font, bg="#FF6347", fg="white")
exit_button.grid(row=3, column=0, pady=20)

canvas.mainloop()
