import tkinter as tk
from tkinter import messagebox

# Datos de ejemplo del menú (corregidos con comas entre elementos)
menu = {
    "SANCOCHOS": [("Costilla", 18000), ("Gallina Criolla", 18000), ("Rabo", 18000), ("Mondongo", 18000)],
    "EJECUTIVOS": [
        ("Pechuga Asada", 16000), ("Carne Asada", 16000), ("Lomo de Cerdo", 16000), ("Chuleta", 16000),
        ("Milanesa", 16000), ("Carne Gulash", 16000), ("Pechuga Rellena", 16000), ("Pechuga a la BBQ", 16000)
    ],
    "PARRILLAS": [("Punta Gorda", 40000), ("Churrasco", 40000), ("Lomo Fino", 40000), ("Parrilladas", 40000)],
    "BEBIDAS": [("Agua", 3000), ("Gaseosa", 4000), ("Jugos", 6000), ("Cervezas", 4000)],
}

carrito = []

# Función para agregar al carrito
def agregar_al_carrito(nombre, precio):
    carrito.append((nombre, precio))
    actualizar_carrito()

# Actualizar lista del carrito
def actualizar_carrito():
    carrito_list.delete(0, tk.END)
    total = 0
    for item in carrito:
        carrito_list.insert(tk.END, f"{item[0]} - ${item[1]:,.0f}")
        total += item[1]
    total_label.config(text=f"Total: ${total:,.0f}")

# Confirmar pedido
def confirmar_pedido():
    if carrito:
        mensaje = "Pedido confirmado:\n" + "\n".join(f"{i[0]} - ${i[1]:,.0f}" for i in carrito)
        messagebox.showinfo("Pedido", mensaje)
        carrito.clear()
        actualizar_carrito()
    else:
        messagebox.showwarning("Vacío", "No hay productos en el carrito.")

# Interfaz principal
ventana = tk.Tk()
ventana.title("App de Restaurante")

frame_menu = tk.Frame(ventana)
frame_menu.pack(side="left", padx=10, pady=10)

frame_carrito = tk.Frame(ventana)
frame_carrito.pack(side="right", padx=10, pady=10)

# Mostrar menú
tk.Label(frame_menu, text="MENU", font=("Arial", 16, "bold")).pack()

for categoria, productos in menu.items():
    tk.Label(frame_menu, text=categoria, font=("Arial", 14)).pack(anchor="w")
    for nombre, precio in productos:
        b = tk.Button(frame_menu, text=f"{nombre} - ${precio:,.0f}", command=lambda n=nombre, p=precio: agregar_al_carrito(n, p))
        b.pack(anchor="w")

# Carrito de compras
tk.Label(frame_carrito, text="Carrito", font=("Arial", 16, "bold")).pack()
carrito_list = tk.Listbox(frame_carrito, width=50)
carrito_list.pack()

total_label = tk.Label(frame_carrito, text="Total: $0", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

btn_confirmar = tk.Button(frame_carrito, text="Confirmar Pedido", command=confirmar_pedido, bg="blue", fg="pink")
btn_confirmar.pack(pady=10)

ventana.mainloop()

