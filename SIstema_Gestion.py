import platform
import os
import time
def LimpiarPantalla():
    time.sleep(2)
    if platform.system()=='Windows':
        os.system('cls')
    else:
        os.system('clear')
    
class Cultivo():
    def __init__(self,nombre,tipo,areacultivo,rendimiento):
        self.nombre=nombre
        self.tipo=tipo
        self.areacultivo=areacultivo
        self.rendimiento=rendimiento
    def CalcularPC(self):
        produc = self.areacultivo + (self.rendimiento*(self.areacultivo/100))
        return produc
class Animal():
    def __init__(self,especie,raza,edad,peso):
        self.especie=especie
        self.raza=raza
        self.edad=edad
        self.peso=peso
        self.produccionA=[]
    def CalcularPA(self):
        produc = self.peso-self.edad
        return produc
class Granja:
    def __init__(self):
        self.Cultivos=[]
        self.Animales=[]
        self.Produccion=[]
    def Agregar(self):
        elec=int(input("¿Que deseas agregar?: \n1) Cultivo \n2) Animal \nRTA: "))
        LimpiarPantalla()
        if elec==1:
            try:
                nombre = input("Digite el nombre del cultivo: ")
                tipo = input("Digite el tipo de cultivo: ")
                areacultivo = float(input("Digite el área de cultivo: "))
                rendimiento = float(input("Digite el rendimiento del cultivo: "))
                cultivo = Cultivo(nombre, tipo, areacultivo, rendimiento)
                self.Cultivos.append(cultivo)
                print("El cultivo ha sido agregado.")
                self.Produccion.append(cultivo.CalcularPC())
            except ValueError:
                print("Ha ocurrido un error. Favor ingresar valores válidos para el área y el rendimiento.")
        elif elec==2:
            try:
                especie = input("Digite la especie del animal: ")
                raza = input("Digite la raza del animal: ")
                edad = int(input("Digite la edad del animal: "))
                peso = float(input("Digite el peso del animal: "))
                animal = Animal(especie, raza, edad, peso)
                self.Animales.append(animal)
                self.Produccion.append(animal.CalcularPA())
                print("Animal agregado exitosamente.")
            except ValueError:
                print("Ha ocurrido un error. Favor ingresar valores válidos para la edad y el peso.")
        else:
            print("Esa opción no existe")
    def Eliminar(self):
        elec=int(input("¿Que deseas eliminar?: \n1) Cultivo \n2) Animal \nRTA: "))
        LimpiarPantalla()
        if elec==1:
            nombre = input("Digite el nombre del cultivo a eliminar: ")
            encontrado = False
            for cultivo in self.Cultivos:
                if cultivo.nombre == nombre:
                    self.Cultivos.remove(cultivo)
                    print(f"El cultivo {nombre} ha sido eliminado exitosamente.")
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se ha logrado encontrar el cultivo con nombre {nombre}.")
        elif elec==2:
            especie = input("Digite la especie del animal a eliminar: ")
            encontrado = False
            for animal in self.Animales:
                if animal.especie == especie:
                    self.Animales.remove(animal)
                    print(f"El animal con especie {especie} ha sido eliminado exitosamente.")
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se ha logrado encontrar el animal de especie {especie}.")
    def CalcularProduccionT(self):
        produccion_total=sum(self.Produccion)
        print(f"La produccion total es de: {produccion_total}")

def Menu():
    print("MENU PRINCIPAL:")
    print("1) Agregar cultivos o animales")
    print("2) Eliminar cultivos o animales")
    print("3) Generar reporte de la producción total")

def main():
    G=Granja()
    print("Bienvenido a la Granja UCundinamarca")
    UserName=str(input("Digite su nombre de usuario: "))
    print(f"Genial {UserName} has ingresado exitosamente a tu base de datos")
    LimpiarPantalla()
    n=0
    while n==0:
        Menu()
        elec=int(input("Selecciona la opción requerida: "))
        if elec==1:
            G.Agregar()
        elif elec==2:
            G.Eliminar()
        elif elec==3:
            G.CalcularProduccionT()
        else:
            print("Opción inválida intente de nuevo. Presione enter")
            input("")
            LimpiarPantalla()
        stad=str.upper((input(f"¿Desea continuar en la base de datos? S(Sí)/N(No)?: ")))
        if stad=="S":
            n=0
            LimpiarPantalla()
        elif stad=="N":
            n=2
            LimpiarPantalla()
        else:
            print("Esa opción no existe, vuelve a intentarlo")
            LimpiarPantalla()
if __name__=="__main__":
    main()
