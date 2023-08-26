import tkinter as tk
from tkinter import filedialog

def agregar_enlace():
    enlace = enlace_entry.get()
    if enlace:
        with open(archivo_m3u, 'a') as archivo:
            archivo.write(enlace + '\n')
        enlace_entry.delete(0, tk.END)
        status_label.config(text=f"Enlace agregado: {enlace}")

def seleccionar_archivo():
    global archivo_m3u
    archivo_m3u = filedialog.askopenfilename(defaultextension=".m3u", filetypes=[("Archivos M3U", "*.m3u")])
    archivo_label.config(text=f"Archivo M3U seleccionado: {archivo_m3u}")

# Crear ventana
ventana = tk.Tk()
ventana.title("Generador de Lista M3U")

# Etiquetas
archivo_label = tk.Label(ventana, text="No se ha seleccionado archivo M3U")
archivo_label.pack()

# Botón para seleccionar archivo
archivo_button = tk.Button(ventana, text="Seleccionar archivo M3U", command=seleccionar_archivo)
archivo_button.pack()

# Campo de entrada para enlace
enlace_entry = tk.Entry(ventana, width=50)
enlace_entry.pack()

# Botón para agregar enlace
agregar_button = tk.Button(ventana, text="Agregar Enlace", command=agregar_enlace)
agregar_button.pack()

# Etiqueta de estado
status_label = tk.Label(ventana, text="")
status_label.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
