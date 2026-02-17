from getpass import getpass

# Diccionario con datos de usuarios
usuarios = {
    "juan": {
        "contraseña": "password123",
        "nombre_completo": "Juan Pérez",
        "carrera": "Ingeniería en Sistemas"
    },
    "maria": {
        "contraseña": "pass456",
        "nombre_completo": "María García",
        "carrera": "Administración"
    },
    "carlos": {
        "contraseña": "pass789",
        "nombre_completo": "Carlos López",
        "carrera": "Ingeniería Industrial"
    }
}

def login():
    print("\n╔════════════════════════════════════════╗")
    print("║  SISTEMA DE CRÉDITO UNIVERSITARIO     ║")
    print("╚════════════════════════════════════════╝")
    
    intentos = 3
    
    while intentos > 0:
        usuario = input("\n👤 Usuario: ")
        contraseña = getpass("🔐 Contraseña: ")
        
        if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
            datos = usuarios[usuario]
            print(f"\n✓ ¡Bienvenido {datos['nombre_completo']}!")
            return True, usuario, datos
        else:
            intentos -= 1
            if intentos > 0:
                print(f"\n✗ Credenciales incorrectas. Intentos restantes: {intentos}")
            else:
                print("\n✗ Acceso denegado. Demasiados intentos fallidos.")
                return False, None, None
    
    return False, None, None

def mostrar_dashboard(usuario, datos):
    while True:
        print(f"\n╔════════════════════════════════════════╗")
        print(f"║  Usuario: {datos['nombre_completo']:<29}║")
        print(f"║  Carrera: {datos['carrera']:<28}║")
        print("╚════════════════════════════════════════╝")
        print("\n1. Ver mis créditos")
        print("2. Ver materias disponibles")
        print("3. Registrarme en una materia")
        print("4. Ver mis materias")
        print("5. Cerrar sesión")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            print("\n📊 CRÉDITOS")
            print("  - Créditos totales: 120")
            print("  - Créditos cursados: 45")
            print("  - Créditos disponibles: 75")
        
        elif opcion == "2":
            print("\n📚 MATERIAS DISPONIBLES:")
            print("  1. Programación (3 créditos) - Semestre 1")
            print("  2. Matemáticas (4 créditos) - Semestre 1")
            print("  3. Bases de Datos (3 créditos) - Semestre 2")
            print("  4. Algoritmos (4 créditos) - Semestre 2")
        
        elif opcion == "3":
            materia = input("\nIngresa el nombre de la materia: ")
            print(f"✓ Te has registrado en '{materia}'")
        
        elif opcion == "4":
            print("\n✅ MIS MATERIAS:")
            print("  - Programación (En curso)")
            print("  - Matemáticas (Aprobada - 4.2)")
        
        elif opcion == "5":
            print("\n✓ Sesión cerrada. ¡Hasta luego!")
            break
        
        else:
            print("\n⚠️ Opción no válida")

def main():
    exitoso, usuario, datos = login()
    
    if exitoso:
        mostrar_dashboard(usuario, datos)

if __name__ == "__main__":
    main()