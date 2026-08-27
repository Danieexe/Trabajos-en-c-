import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

pantalla = tk.Entry(ventana, font=("Arial", 20), justify="right")
pantalla.pack(fill="both", padx=10, pady=10)

def click_boton(valor):
    pantalla.insert(tk.END, valor)

def borrar():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except Exception:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

frame_botones = tk.Frame(ventana)
frame_botones.pack()

botones = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]
for fila in botones:
    frame_fila = tk.Frame(frame_botones)
    frame_fila.pack()
    for texto in fila:
        if texto == 'C':
            cmd = borrar
        elif texto == '=':
            cmd = calcular
        else:
            cmd = lambda t=texto: click_boton(t)
            
        btn = tk.Button(frame_fila, text=texto, font=("Arial", 14), width=5, height=2, command=cmd)
        btn.pack(side="left", padx=2, pady=2)

ventana.mainloop()