import tkinter as tk
from tkinter import filedialog
import qrcode
import time

def generate_qr_code():
    data = entry.get()
    if data:
        qr = qrcode.QRCode(version=15, box_size=20, border=6)  # Increase box_size and border
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="turquoise")  # Change fill color
        img = img.resize((300, 300))  # Resize the image for a larger QR code

        # Generate a unique filename based on current timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"qr_code_{timestamp}.png"
        img.save(filename)

        result_label.config(text=f"QR code generated successfully! Saved as {filename}")
    else:
        result_label.config(text="Please enter some data!")


def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            entry.delete(0, tk.END)
            entry.insert(tk.END, file.read())


# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create the input elements
label = tk.Label(window, text="Enter text or choose a file:", fg="blue", font=("Arial", 12))
label.pack()

entry = tk.Entry(window, width=40, bg="lightgray", font=("Arial", 12))
entry.pack()

# file_button = tk.Button(window, text="Choose File", command=choose_file, bg="lightgreen", fg="white",
#                         font=("Arial", 12))
# file_button.pack()

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code, bg="orange", fg="white",
                            font=("Arial", 12, "bold"))
generate_button.pack()

result_label = tk.Label(window, text="", fg="purple", font=("Arial", 12))
result_label.pack()

# Start the main event loop
window.mainloop()
