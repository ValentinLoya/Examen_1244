# Clase_Cliente.py
# Valeburguer
# Definimos la clase Cliente1244
class Cliente1244:
    Id_Cliente1244 = " "
    Nombre1244 = " "
    Id_Venta1244 = " "
    Edad1244 = " "
    Sexo1244 = " "
    Correo1244 = " "
    Presupuesto1244 = " "
    
    def mostrar_datosCliente(self):
        print(f"Id_Cliente: {self.Id_Cliente1244}")
        print(f"Nombre: {self.Nombre1244}")
        print(f"Id_Venta: {self.Id_Venta1244}")
        print(f"Edad: {self.Edad1244}")
        print(f"Sexo: {self.Sexo1244}")
        print(f"Correo: {self.Correo1244}")
        print(f"Presupuesto: {self.Presupuesto1244}")
    # Lista de los nombres de los clientes
    def Lista_Clientes(self):
        lista_Clientes1244 = [
        "Luis","Valentin","Ali","Jan","Angel","Juan","Anahi"
        ]
        print(lista_Clientes1244)
        for lista in lista_Clientes1244:
            print(lista)
    # Tupla de las edades de los clientes
    def Tupla_Edad(self):
        tupla_edad = (
        "22","25","18","35","17","19","25"
        )
        print(tupla_edad)
        for tupla in tupla_edad:
            print(tupla)

    # Diccionario del Id de los clientes
    def Dicionario_Id_Cliente(self):
        diccionario_Id1244 = {
            "Luis": 1595,
            "Valentin": 1244,
            "Ali": 1783,
            "Jan": 1356,
            "Angel": 1197,
            "Juan": 1457,
            "Anahi": 1245
        }
        print(diccionario_Id1244)
        for dicc in diccionario_Id1244:
            print(dicc)

    # Función para dar de alta a un cliente
    def altas(self):
        print("La operación de alta se realizó correctamente para datos del cliente.")

    # Función para dar de baja a un cliente
    def bajas(self):
        print("La operación de baja se realizó correctamente para los datos del cliente.")

# Creación del objeto cliente
cliente = Cliente1244()

# Asignación de datos a los atributos
cliente.Id_Cliente1244 = "1258"
cliente.Nombre1244 = "Valentin"
cliente.Id_Venta1244 = "18763"
cliente.Edad1244 = "25"
cliente.Sexo1244 = "Masculino"
cliente.Correo1244 = "a.22308051281244@cbtis128.edu.mx"
cliente.Presupuesto1244 = "2,0000"

# Mostrar datos del cliente
cliente.mostrar_datosCliente()

# Llamadas a las funciones
print("\nLista de Clientes:")
print(cliente.Lista_Clientes())

print("\nTupla de Edad de clientes:")
print(cliente.Tupla_Edad())

print("\nDiccionario de Id del cliente:")
print(cliente.Dicionario_Id_Cliente())

# Operaciones de alta y baja
cliente.altas()
cliente.bajas()