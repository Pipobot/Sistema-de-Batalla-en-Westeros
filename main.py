import os
os.system ("cls")

#Actividad repasoooo

BONO_STARK = 2
BONO_LANNISTER = 3
BONO_TARGARYEN = 5
BONO_BARATHEON = 0
PODER_MIN = 1
PODER_MAX = 20

try:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    casa = input("Ingrese la casa que representa ( S  →  Stark, L  → Lannister, T → Targaryen, B → Baratheon): ").lower()
    import random
    poder_base = random.randint(PODER_MIN, PODER_MAX)
    if casa == "s":
        poder_total = poder_base + BONO_STARK
        casa = "Stark"
    elif casa == "l":
        poder_total = poder_base - BONO_LANNISTER
        casa = "Lannister"
    elif casa == "t":
        poder_total = poder_base +  BONO_TARGARYEN
        casa = "Targaryen"
    elif casa == "b":
        poder_total = poder_base + BONO_BARATHEON
        casa = "Baratheon"
    else:
        print("Casa no valida!!!")
        
    if poder_total >= 20:
        resultado = "Victoria epica!!"
    elif poder_total >= 10 and poder_total <= 19:
        resultado = "Victoria ajustada."
    elif poder_total < 10:
        resultado = "Derrota :("
except:
    print("Error! Respuesta no valida :(")


os.system("cls")
print(f"Su nombre es: {nombre}")
print(f"Su edad es: {edad}")
print(f"Su casa es: {casa}")
print(f"Poder base generado: {poder_base}")
print(f"Poder final: {poder_total}")
print(f"Resultado de la batalla: {resultado}")