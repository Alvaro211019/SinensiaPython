import random

def play_game():
    print("🎯 Bienvenido al juego de adivinar el número")
    print("Voy a generar un número aleatorio entre 1 y 20...")

    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input("Introduce tu número: "))
            attempts += 1

            if guess < 1 or guess > 20:
                print(" El número debe estar entre 1 y 20.")
                continue

            if guess == secret_number:
                print(f" ¡Correcto! El número era {secret_number}. Lo adivinaste en {attempts} intentos.")
                break
            elif guess < secret_number:
                print("Demasiado bajo, prueba con un número más alto.")
            else:
                print("Demasiado alto, prueba con un número más bajo.")

        except ValueError:
            print(" Eso no es un número válido, inténtalo de nuevo.")

if __name__ == "__main__":
    play_game()
