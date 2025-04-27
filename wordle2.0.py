def verificar_palabra_valida(palabra):
    """Verifica si la palabra tiene exactamente 5 letras y solo contiene letras."""
    if len(palabra) != 5 or not palabra.isalpha():
        return False
    return True

def verificar_letras_y_posiciones(palabra_secreta, intento):
    """Verifica las letras correctas en la palabra y su posición."""
    resultado = []  # Usamos una lista vacía
    
    for i in range(5):
        if intento[i] == palabra_secreta[i]:
            resultado.append(f"[{intento[i]}] 👌")  # Letra correcta en la posición correcta
        elif intento[i] in palabra_secreta:
            resultado.append(f"({intento[i]}) 🤔")  # Letra correcta en la posición incorrecta
        else:
            resultado.append(f"{intento[i]} ⛔")  # Letra incorrecta
    
    # Concatenar la lista de resultados sin usar join
    resultado_completo = ""
    for res in resultado:
        resultado_completo += res  # Concatenamos cada elemento de la lista
    
    return resultado_completo

def jugar_wordle():
    """Función principal que ejecuta el juego de Wordle."""
    print("¡Bienvenido a Wordle!")
    palabra_secreta = input("Ingresa la palabra secreta de 5 letras: ").lower()

    # Asegurarse de que la palabra secreta es válida.
    while not verificar_palabra_valida(palabra_secreta):
        print("La palabra debe tener exactamente 5 letras y solo contener letras.")
        palabra_secreta = input("Ingresa la palabra secreta de 5 letras: ").lower()
    
    intentos = 6
    while intentos > 0:
        print(f"\nTe quedan {intentos} intentos.")
        intento = input("Ingresa tu palabra de 5 letras: ").lower()

        # Verificar que la palabra ingresada es válida.
        while not verificar_palabra_valida(intento):
            print("La palabra debe tener exactamente 5 letras y solo contener letras.")
            intento = input("Ingresa una palabra de 5 letras: ").lower()

        # Comprobar si el intento es correcto
        resultado = verificar_letras_y_posiciones(palabra_secreta, intento)
        print(f"Resultado: {resultado}")
        
        # Verificar si el jugador adivinó la palabra
        if intento == palabra_secreta:
            print(f"¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
            break

        intentos -= 1

    if intentos == 0:
        print(f"Lo siento, te quedaste sin intentos. La palabra secreta era: {palabra_secreta}")

# Iniciar el juego
jugar_wordle()