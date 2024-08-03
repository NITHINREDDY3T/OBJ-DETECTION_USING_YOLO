import cv2  
import tkinter as tk
from PIL import Image, ImageTk

def run_gui(detect_objects):
    cap = None  # Inisialisasi objek VideoCapture

    def open_camera():
        nonlocal cap  # Tambahkan nonlocal keyword untuk mengubah nilai variabel cap di luar fungsi open_camera()

        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        while True:
            success, img = cap.read()
            detect_objects(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (640, 480))
            photo = ImageTk.PhotoImage(Image.fromarray(img))
            canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            canvas.image = photo
            window.update()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        window.quit()

    def exit_program():
        if cap is not None:
            cap.release()  # Hentikan VideoCapture jika sedang berjalan
        window.quit()

    window = tk.Tk()
    window.title("Blind Assistant")
    window.geometry("640x560")
    window.configure(bg="white")  # Set the background color of the window

    label = tk.Label(window, text="Blind Assistant", bg="white", fg="black")  # Set the background and foreground color of the label
    label.pack()

    canvas = tk.Canvas(window, width=640, height=480, bg="black")  # Set the background color of the canvas
    canvas.pack()

    # Tampilkan foto pada awal program
    initial_img = Image.open("ii.jpg")  # Ganti dengan path ke foto Anda
    initial_img = initial_img.resize((640, 480))  # Sesuaikan ukuran foto dengan ukuran canvas
    initial_photo = ImageTk.PhotoImage(initial_img)
    canvas.create_image(0, 0, image=initial_photo, anchor=tk.NW)
    canvas.image = initial_photo

    open_camera_button = tk.Button(window, text="Open Camera", command=open_camera, bg="blue", fg="white")  # Set the background and foreground color of the button
    open_camera_button.pack()

    exit_button = tk.Button(window, text="Exit", command=exit_program, bg="red", fg="white")  # Set the background and foreground color of the button
    exit_button.pack()

    window.mainloop()
