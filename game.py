from browser import document
import random

# Elementos del HTML
output = document["output"]
entrada = document["entrada"]
boton = document["btn"]

def print_linea(texto):
    output.text += str(texto) + "\n" #lo siguiente aparece en la siguiente línea

# Variables 
MINIMO = 1
maximo = None
numero_azar = None
intentos = 0
estado = "inicio"

def manejar_entrada(evento):
    global maximo, numero_azar, intentos, estado
    texto = entrada.value.strip()
    entrada.value = "" #borra lo que había escrito el usuario en el cuadro de texto después de leerlo

    if not texto:
        return

    if estado == "inicio":
        dificultad = texto.upper()
        if dificultad == "F":
            maximo = 10
        elif dificultad == "M":
            maximo = 50
        elif dificultad == "D":
            maximo = 100
        else:
            print_linea("ERROR, escoge la dificultad [F, M, D]")
            return

        numero_azar = random.randint(MINIMO, maximo)
        intentos = 0
        estado = "jugando"
        print_linea(f"Dificultad {dificultad} elegida. ¡Adivina el número entre {MINIMO} y {maximo}!")
        return

    if estado == "jugando":
        try:
            usuario_num = int(texto)
        except:
            print_linea("Por favor, escribe un número válido")
            return

        intentos += 1
        if usuario_num > numero_azar:
            print_linea("El número es más pequeño")
        elif usuario_num < numero_azar:
            print_linea("El número es más grande")
        else:
            print_linea(f"¡Felicidades, has acertado! El número era {numero_azar}")
            print_linea(f"Intentos: {intentos}")
            estado = "fin"

# Interacciones
# Cada vez que pulses el botón, tu juego leerá lo que escribiste en la entrada de texto y lo procesará
boton.bind("click", manejar_entrada)

print_linea("Elige la dificultad [F, M, D]:")

