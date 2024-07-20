import secrets
import string
from colorama import init, Fore, Style

# Inicializar colorama para que funcione en diferentes plataformas
init()

# Función para generar una contraseña segura
def generar_contrasena(longitud, usar_mayusculas=True, usar_numeros=True, usar_especiales=True):
    caracteres = string.ascii_lowercase
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiales:
        caracteres += string.punctuation
    
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

# Función para obtener las preferencias del usuario
def obtener_opciones():
    print(Fore.CYAN + "Configuración de contraseña:" + Style.RESET_ALL)
    while True:
        try:
            longitud = int(input("Longitud de la contraseña: "))
            if longitud <= 0:
                print("Error: La longitud debe ser un número positivo.")
                continue
            usar_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
            usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
            usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
            if not (usar_mayusculas or usar_numeros or usar_especiales):
                print("Error: Debes seleccionar al menos una opción.")
                continue
            return longitud, usar_mayusculas, usar_numeros, usar_especiales
        except ValueError:
            print("Error: Introduce un número válido para la longitud.")


# Función principal para generar una contraseña personalizada
def generar_contrasena_personalizada():
    longitud, usar_mayusculas, usar_numeros, usar_especiales = obtener_opciones()
    contrasena_generada = generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_especiales)
    print("\n" + Fore.GREEN + "¡Contraseña generada exitosamente!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Contraseña:" + Style.RESET_ALL, contrasena_generada)

# Ejecutar el programa principal
if __name__ == "__main__":
    generar_contrasena_personalizada()

