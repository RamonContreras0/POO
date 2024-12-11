'''Desarrollar un sistema de gestión de contactos, en el cual se debe crear dos clases,
Contacto y Agenda, para gestionar los contactos de una agenda. El objetivo es permitir al
usuario realizar operaciones básicas como añadir, buscar, editar y listar contactos. Además,
el programa debe nalizar correctamente cuando el usuario lo solicite.
'''

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

    def __str__(self):
        return f"Nombre: {self.__nombre}, Teléfono: {self.__telefono}, Email: {self.__email}"

    def modificar_contacto(self, nombre=None, telefono=None, email=None):
        if nombre:
            self.__nombre = nombre
        if telefono:
            self.__telefono = telefono
        if email:
            self.__email = email

    def obtener_nombre(self):
        return self.__nombre

class Agenda:
    def __init__(self):
        self.contactos = []

    def anadir_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nombre}' añadido correctamente.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.obtener_nombre().lower() == nombre.lower():
                return contacto
        return None

    def editar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            print(f"Editando contacto: {contacto}")
            nuevo_nombre = input("Nuevo nombre (presiona Enter para dejar igual): ")
            nuevo_telefono = input("Nuevo teléfono (presiona Enter para dejar igual): ")
            nuevo_email = input("Nuevo email (presiona Enter para dejar igual): ")
            contacto.modificar_contacto(
                nombre=nuevo_nombre if nuevo_nombre else None,
                telefono=nuevo_telefono if nuevo_telefono else None,
                email=nuevo_email if nuevo_email else None,
            )
            print("Contacto actualizado.")
        else:
            print(f"Contacto con nombre '{nombre}' no encontrado.")

    def cerrar_agenda(self):
        print("Cerrando la agenda. Hasta luego.")
        exit()

# Menú principal
agenda = Agenda()

while True:
    print("\n--- Menú Agenda ---")
    print("1. Añadir contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        agenda.anadir_contacto(nombre, telefono, email)

    elif opcion == "2":
        agenda.listar_contactos()

    elif opcion == "3":
        nombre = input("Nombre del contacto a buscar: ")
        contacto = agenda.buscar_contacto(nombre)
        if contacto:
            print(contacto)
        else:
            print(f"Contacto con nombre '{nombre}' no encontrado.")

    elif opcion == "4":
        nombre = input("Nombre del contacto a editar: ")
        agenda.editar_contacto(nombre)

    elif opcion == "5":
        agenda.cerrar_agenda()

    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
