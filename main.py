import tkinter as tk


def convert_to_km():
    in_mile = entry_mile.get()
    in_km = float(in_mile) * 1.609344
    label_converted_km.config(text=in_km.__round__(3))

# window(GUI)
window = tk.Tk()
window.title("Mile to km converter")
window.config(height=150, width=300)
window.minsize(height=150, width=300)

# labels
label_welcome = tk.Label(text="Welcome\n to\n converter", font=("Arial", 10, "bold"))
label_welcome.config(padx=30)
label_welcome.grid(column=0, row=0)

label_info = tk.Label(text="1 mile =\n 1.609344 km", font=("Arial", 10, "normal"))
label_info.config(pady=10)
label_info.grid(column=0, row=1)

label_mile = tk.Label(text="Mile('s)", font=("Arial", 10, "bold"))
label_mile.grid(column=2, row=0)

label_km = tk.Label(text="Km", font=("Arial", 10, "bold"))
label_km.grid(column=2, row=1)
label_converted_km = tk.Label(text="0", font=("Arial", 10, "normal"))
label_converted_km.grid(column=1, row=1)

# Entry
entry_mile = tk.Entry(borderwidth=3)
entry_mile.grid(column=1, row=0)

# Button
button = tk.Button(text="Convert", command=convert_to_km)
button.grid(column=1, row=2)

window.mainloop()
