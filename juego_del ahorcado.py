import random
import sys

# =====================================================
# BIENVENIDA AL JUEGO
# =====================================================
print("=====================================================")
print("        ¡Bienvenido al juego del ahorcado!")
print("=====================================================")
print("Intenta adivinar la palabra antes de perder todas tus oportunidades 😊.")
print("¡Buena suerte! 🍀\n")

# Corrección del input: Guardamos la respuesta en una variable primero
opcion = input("Escribe 'start' para empezar o 'close' para cerrar: ").lower()

if opcion == "start":
    print("\n¡Comencemos el juego!")
elif opcion == "close":
    print("¡Hasta luego! 👋")
    sys.exit()
else:
    print("Opción no reconocida. Cerrando el juego... 🚪")
    sys.exit()



# =====================================================
# CONFIGURACIÓN Y FUNCIONES
# =====================================================

def elegir_palabra(dificultad):
    palabras_faciles = ["gato", "perro", "casa", "sol", "luna"]
    palabras_intermedias = ["elefante", "mariposa", "computadora", "avión", "teléfono"]
    palabras_dificiles = ["hipopótamo", "paralelepípedo", "anticonstitucionalmente", "otorrinolaringólogo", "desoxirribonucleico"]


    if dificultad == 1:
        print("\n¡Has elegido la dificultad fácil! 💚")
        return random.choice(palabras_faciles)
    elif dificultad == 2:
        print("\n¡Has elegido la dificultad intermedia! 💛")
        return random.choice(palabras_intermedias)
    elif dificultad == 3:
        print("\n¡Has elegido la dificultad difícil! 🧡")
        return random.choice(palabras_dificiles)
    else:
        print("❌ Dificultad no válida. Elige entre 1, 2 o 3.")
        sys.exit()


# =====================================================
# SELECCIÓN DE DIFICULTAD
# =====================================================
print("\nSelecciona la dificultad:")
print("1. Fácil")
print("2. Intermedio")
print("3. Difícil")

try:
    dificultad_elegida = int(input("Introduce el número: "))
    palabra_juego = elegir_palabra(dificultad_elegida)
except ValueError:
    print("❌ Por favor, introduce un número válido.")
    sys.exit()


# =====================================================
# LÓGICA PRINCIPAL DEL JUEGO (NUEVO)
# =====================================================

# Lista para guardar las letras que el usuario va adivinando
letras_adivinadas = []
intentos_restantes = 6
#len me ayuda a medir cuantas letras tiene la palabra, para mostrar al usuario cuantos guiones bajos debe adivinar
print(f"\nLa palabra secreta elegida tiene {len(palabra_juego)} letras. ¡A jugar!")

# El juego corre mientras queden intentos
while intentos_restantes > 0:
    
    equivalencias = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u"
}

    # 1. Mostrar la palabra oculta 
    palabra_oculta = ""
    for letra in palabra_juego:
        letra_comparar = equivalencias.get(letra,letra)
        if letra_comparar in letras_adivinadas:
            palabra_oculta += letra + " "
        else:
            palabra_oculta += "_ "
            
    print(f"\nPalabra: {palabra_oculta}")
    print(f"Intentos restantes: {intentos_restantes}")
    
    # 2. Verificar si el usuario ya ganó (si ya no quedan guiones bajos)
    if "_" not in palabra_oculta:
        print("\n🎉 ¡Felicidades! ¡Has adivinado la palabra y ganado el juego! 🏆")
        break

    # 3. Pedir una letra al usuario
    letra_usuario = input("Introduce una letra: ").lower()

    # Validaciones rápidas de la entrada
    #.insalpha encontre que sirve para verificar si el input es una letra, y len() para asegurarnos que solo se introduzca una letra
    if len(letra_usuario) != 1 or not letra_usuario.isalpha():
        print("❌ Por favor, introduce solo una letra válida.")
        continue
        
    if letra_usuario in letras_adivinadas:
        print("⚠️ Ya habías intentado con esa letra. Prueba otra.")
        continue

    # 4. Procesar la letra
    letras_adivinadas.append(letra_usuario)
equivalencias = {
    "a": ["a", "á"],
    "e": ["e", "é"],
    "i": ["i", "í"],
    "o": ["o", "ó"],
    "u": ["u", "ú"]
}
if letra_usuario in equivalencias:
    letras_a_buscar = equivalencias[letra_usuario]
else:
    letras_a_buscar = [letra_usuario]
    if letra_usuario in palabra_juego:
        print("✨ ¡Bien hecho! La letra está en la palabra.")
    else:
        print("😢 Lo siento, esa letra no está en la palabra.")
        intentos_restantes -= 1

# Si sale del bucle porque se quedó sin vidas
if intentos_restantes == 0:
    print(f"\n💥 ¡Te has quedado sin intentos! Perdiste.")
    print(f"La palabra secreta era: {palabra_juego}")