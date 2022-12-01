# CPU=Es la parte de una computadora en la que se encuentran los elementos que sirven para procesar datos.
# Importar librerias
import tkinter as tk
import random


# Lista de variables
lista = ["Piedra", "Papel", "Tijera"]

#---------------------------
# Funciones operaciones
# --------------------------

def calcular_ganador_piedra():
    eleccion_cpu = random.randint(0, 2)

    if eleccion_cpu == 0:
        imagen_respuesta.configure(image=imagen_piedra)
        resultado = "Empate"

    elif eleccion_cpu == 1:
        imagen_respuesta.configure(image=imagen_papel)
        resultado = "Derrota"
        label_puntaje_cpu.configure(text=int(label_puntaje_cpu.cget("text")) + 1)

    elif eleccion_cpu == 2:
        imagen_respuesta.configure(image=imagen_tijera)
        resultado = "Victoria"
        label_puntaje_jugador.configure(text=int(label_puntaje_jugador.cget("text")) + 1)

    label_resultado.configure(text=resultado)


def calcular_ganador_papel():
    eleccion_cpu = random.randint(0, 2)

    if eleccion_cpu == 0:
        imagen_respuesta.configure(image=imagen_piedra)
        resultado = "Victoria"
        label_puntaje_jugador.configure(text=int(label_puntaje_jugador.cget("text")) + 1)

    elif eleccion_cpu == 1:
        imagen_respuesta.configure(image=imagen_papel)
        resultado = "Empate"

    elif eleccion_cpu == 2:
        imagen_respuesta.configure(image=imagen_tijera)
        resultado = "Derrota"
        label_puntaje_cpu.configure(text=int(label_puntaje_cpu.cget("text")) + 1)
    label_resultado.configure(text=resultado)


def calcular_ganador_tijera():
    eleccion_cpu = random.randint(0, 2)

    if eleccion_cpu == 0:
        imagen_respuesta.configure(image=imagen_piedra)
        resultado = "Derrota"
        label_puntaje_cpu.configure(text=int(label_puntaje_cpu.cget("text")) + 1)

    elif eleccion_cpu == 1:
        imagen_respuesta.configure(image=imagen_papel)
        resultado = "Victoria"
        label_puntaje_jugador.configure(text=int(label_puntaje_jugador.cget("text")) + 1)

    elif eleccion_cpu == 2:
        imagen_respuesta.configure(image=imagen_tijera)
        resultado = "Empate"

    label_resultado.configure(text=resultado)

# Esta función es para es para reiniciar el juego 
def reiniciar_contadores():
    label_resultado.configure(text="")
    label_puntaje_jugador.configure(text="0")
    label_puntaje_cpu.configure(text="0")
    imagen_respuesta.configure(image="")

# Esta función es para salir de la ventana, destroy() es eliminar la ventana.
def salir_ventana():
    ventana_principal.destroy()

# Interfaz

# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------

# creacion objeto Tk (ventana principal)
ventana_principal = tk.Tk()

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("400x540")

# deshabilitar boton maximizar
ventana_principal.resizable(0,0)

# colores de la  ventana principal (color de la ventana "color piker" --, color de fondo , ancho del color)
ventana_principal.configure(bg="#db03fc", highlightbackground="black", highlightthickness=10)


# Etiquetas par el titulo de app (color fondo, color de la funete, tipo de letra y bold=negrita )
label_titulo = tk.Label(text="¡Piedra, papel o tijera!",bg="#db03fc",fg="#090909",font=("Verdana", 18, "bold"),)
label_titulo.place(x=50, y=18)

# Etiqueta para el jugador cpu resultado de cada juego
label_puntaje_cpu = tk.Label(text=0, bg="#db03fc", fg="#090909", font=("Consolas", 30, "bold"))
label_puntaje_cpu.place(x=280, y=70)

# Etiqueta para el jugador jugador
label_puntaje_jugador = tk.Label(text=0, bg="#db03fc", fg="#090909", font=("Consolas", 30, "bold"))
label_puntaje_jugador.place(x=100, y=70)


#boton
# Etiqueta para la imagen "piedra" (Modificación del boton de la imagen)
imagen_piedra = tk.PhotoImage(file="piedra.png")
boton_piedra = tk.Button(ventana_principal, bg="white", image=imagen_piedra,borderwidth=5,relief="raised",command=calcular_ganador_piedra,)
boton_piedra.place(x=65, y=135)

#  Etiqueta para la imagen "papel" 
imagen_papel = tk.PhotoImage(file="papel.png")
boton_papel = tk.Button(ventana_principal,bg="white",image=imagen_papel,borderwidth=5,relief="raised",command=calcular_ganador_papel,)
boton_papel.place(x=65, y=245)

# Etiqueta para la imagen "tijera"
imagen_tijera = tk.PhotoImage(file="tijera.png")
boton_tijera = tk.Button(ventana_principal,bg="white",image=imagen_tijera,borderwidth=5,relief="raised",command=calcular_ganador_tijera,)
boton_tijera.place(x=65, y=380)


# Etiqueta para el boton de reinicio
boton_reinicio = tk.Button(ventana_principal,bg="white",text="REINICIAR",command=reiniciar_contadores,)
boton_reinicio.place(x=256, y=400)

# Etiqueta para el boton de salir
boton_salir = tk.Button(ventana_principal, bg="white",text="SALIR",command=salir_ventana,)
boton_salir.place(x=256, y=455)

# Etiqueta del el resultado  del juego depende a la instrucción. (TEXTO DONDE NOS DETERMINA QUIEN TIENE "VICTORIA-DERROTA-EMPATE")
label_resultado = tk.Label(text="", bg="#db03fc", fg="#090909", font=("Verdana", 15, "bold"))
label_resultado.place(x=167, y=70)

# Etiqueta del boton de respuesta cpu
imagen_respuesta = tk.Label(image="", bg="#db03fc")
imagen_respuesta.place(x=220, y=205)

#se ejecuta el metodo mainloop() de la clase Tk a través de la instancia (objeto) ventana_principal. 
# Este objeto despliega una ventana simple en pantalla y que a la espera de lo que el usuario haga
# (click en el boton, escribir, etc.) cada accion del usuario se conoce como un evento el metodo mainloop 
# es un bucle infinito.  

ventana_principal.mainloop()