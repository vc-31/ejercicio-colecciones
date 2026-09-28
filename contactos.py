# ===================================================
# Programa: Agenda de Contactos Telefónicos
# Descripción: Permite agregar, buscar, mostrar y
#              eliminar contactos usando un diccionario.
# ===================================================

def mostrar_menu():
    print("\n" + "="*35)
    print("      GESTIÓN DE CONTACTOS")
    print("="*35)
    print("1. Agregar un nuevo contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar un contacto por nombre")
    print("4. Eliminar un contacto")
    print("5. Salir")
    print("="*35)


def main():
    # 1. Creación de la colección de datos (Diccionario)
    contactos = {
        "Sara López": "0991234567",
        "Miguel Zambrano": "0987654321"
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        # 2. Agregar/Insertar datos a la colección
        if opcion == "1":
            nombre = input("\nIngrese el nombre del contacto: ").strip()
            if nombre in contactos:
                print(f"⚠️ El contacto '{nombre}' ya existe.")
            else:
                telefono = input("Ingrese el número de teléfono: ").strip()
                contactos[nombre] = telefono
                print(f"✓ Contacto '{nombre}' agregado exitosamente.")

        # 3. Mostrar la información almacenada
        elif opcion == "2":
            print("\n--- LISTA DE CONTACTOS ---")
            if not contactos:
                print("La agenda está vacía.")
            else:
                for nombre, telefono in contactos.items():
                    print(f"• Nombre: {nombre:<20} | Teléfono: {telefono}")

        # 4. Operación adicional: Buscar elementos
        elif opcion == "3":
            nombre = input("\nIngrese el nombre a buscar: ").strip()
            if nombre in contactos:
                print(f"✓ Encontrado: {nombre} -> Teléfono: {contactos[nombre]}")
            else:
                print(f"❌ El contacto '{nombre}' no existe en la agenda.")

        # 5. Operación adicional: Eliminar elementos
        elif opcion == "4":
            nombre = input("\nIngrese el nombre del contacto a eliminar: ").strip()
            if nombre in contactos:
                del contactos[nombre]
                print(f"✓ Contacto '{nombre}' eliminado correctamente.")
            else:
                print(f"❌ El contacto '{nombre}' no existe.")

        elif opcion == "5":
            print("\n¡Gracias por usar la agenda de contactos! Hasta luego.")
            break

        else:
            print("\n⚠️ Opción no válida, por favor intente de nuevo.")


# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    main()