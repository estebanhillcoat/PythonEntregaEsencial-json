import json

productos = []

try:
    with open("datos.json", "r") as archivo:
        productos = json.load(archivo)

except FileNotFoundError:
    with open("datos.json", "w") as archivo:
        json.dump([], archivo)

def actualizar():
    with open("datos.json","w") as archivo:
        json.dump(productos,archivo)
    
    

            


while True:
    opciones = input("A - Agregar\nR - Remover\nL - Listar\nS - Salir\n").strip().upper()
    
    match opciones:
        case "S":
            break
        case "A":
            agregar = input("\nagregar: ")
            productos.append(agregar.strip().title())
            
            actualizar()
            
            
        case "R":
            remover = input("\nRemover: ")
            productos.remove(remover.strip().title())
            
            actualizar()
        
        case "L":
            print(productos)


        
