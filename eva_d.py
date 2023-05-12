#Lista original 
nombres = ["Harry Houdini","Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

#Lista por grupos
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = []

# Grupo de los otros 
for item in nombres: 
        if item not in magos and item not in cientificos:
             otros.append(item)
             #print("Otros: " + item)   

print("-----------------------------------------")


# Segunda función

def imprimir_nombres(nombres):
    for item in nombres:       
        print(item)    
    
lista = imprimir_nombres(nombres)
print(lista)

print("-----------------------------------------")


# Tercera función
def imprimir_todos():
    for mago in magos:
        print("Magos: " + mago)

    for cientifico in cientificos:
        print("Científicos: " + cientifico)

    for otro in otros:
        print("Otros: " + otro)

lista_grupos = imprimir_todos()
print(lista_grupos)  

print("-----------------------------------------")

# Primera función 

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]
            
hacer_grandioso(magos)    
print(f"Estos son los magos mas famosos: {magos}")

print("-----------------------------------------")

















