import pyqrcode
import os
import imageio
from PIL import Image, ImageTk
import tkinter as tk

def animate(i, frames, label):
        # Loop over the frames
        frame = frames[i % len(frames)]
        label.config(image=frame)
        label.image = frame
        label.after(100, animate, i+1, frames, label)

def create_qr_code(key, max_size=2953, size=5, duration=1,v=40):
        # Divida a chave em partes menores
        chunks = [key[i:i+max_size] for i in range(0, len(key), max_size)]
        
        qr_codes = []
        for i, chunk in enumerate(chunks):
                # Gere um QR Code para cada parte
                qr_code = pyqrcode.create(chunk, error='L', version=v)
                filename = f'qrcode{i}.png'
                qr_code.png(filename, scale=size)
                qr_codes.append(filename)
        
        # Crie um GIF animado a partir dos QR Codes
        images = []
        for filename in qr_codes:
                images.append(imageio.imread(filename))
        gif_filename = 'animated_qr.gif'
        imageio.mimsave(gif_filename, images, duration=duration)

        # Remova os arquivos de imagem do QR Code
        for filename in qr_codes:
                os.remove(filename)

        # Exiba o GIF animado em uma janela Tkinter
        top = tk.Toplevel()
        img = Image.open(gif_filename)
        frames = [ImageTk.PhotoImage(img)]
        try:
                while True:
                        img.seek(img.tell()+1)
                        frames.append(ImageTk.PhotoImage(img))
        except EOFError:
                pass  # We have read all frames of the gif
        label = tk.Label(top)
        label.pack()
        animate(0, frames, label)

        return top



