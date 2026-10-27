productos = []

def actualizar():
    with open("stock.txt","w") as archivo:
        for producto in productos:
            archivo.write(producto + "\n")
            

while True:
    opciones = input("S - Salir\nA - Agregar\nR - Remover\nL - Listar productos\nB - Buscar\n").upper()
    
    match opciones:
        
        case "S":
            break
        
        case "A":
            agregar = input("Producto a agregar:\n")
            productos.append(agregar)
            print(f"\n{agregar} se agregó con exito!\n")
            actualizar()
            
        case "R":
            remover = input("Producto a remover:\n")
            productos.remove(remover)
            print(f"{remover} removido con exito!")
            actualizar()
            
        case "L":
            for producto in productos:
                print(producto)
        case "B":
            buscar = input("Producto a buscar: ")
            if buscar in productos:
                print(f"\n{buscar} esta en stock.\n")
            else:
                print(f"\n{buscar} NO esta en stock.\n")
               
