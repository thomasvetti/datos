import json
import xml.etree.ElementTree as ET


def agregar_empleado_terminal(archivo_json, archivo_xml):
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    departamento = input("Ingrese el departamento del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))

    nuevo_empleado = {
        'nombre': nombre,
        'edad': edad,
        'departamento': departamento,
        'salario': salario
    }

    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            empleados_json = json.load(archivo)
    except FileNotFoundError:
        empleados_json = []

    empleados_json.append(nuevo_empleado)

    with open(archivo_json, 'w', encoding='utf-8') as archivo:
        json.dump(empleados_json, archivo, indent=4, ensure_ascii=False)

    try:
        tree = ET.parse(archivo_xml)
        root = tree.getroot()
    except FileNotFoundError:
        root = ET.Element('empleados')

    empleado = ET.SubElement(root, 'empleado')
    ET.SubElement(empleado, 'nombre').text = nombre
    ET.SubElement(empleado, 'edad').text = str(edad)
    ET.SubElement(empleado, 'departamento').text = departamento
    ET.SubElement(empleado, 'salario').text = str(salario)

    tree = ET.ElementTree(root)
    tree.write(archivo_xml, encoding='utf-8', xml_declaration=True)

    print(f"Empleado {nombre} agregado con éxito.")



def actualizar_salario(nombre_empleado, nuevo_salario, archivo_json, archivo_xml):
    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            empleados_json = json.load(archivo)
        
        for empleado in empleados_json:
            if empleado['nombre'] == nombre_empleado:
                empleado['salario'] = nuevo_salario
                break
        
        with open(archivo_json, 'w', encoding='utf-8') as archivo:
            json.dump(empleados_json, archivo, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print("Archivo JSON no encontrado.")

    try:
        tree = ET.parse(archivo_xml)
        root = tree.getroot()
        
        for empleado in root.findall('empleado'):
            nombre = empleado.find('nombre').text
            if nombre == nombre_empleado:
                empleado.find('salario').text = str(nuevo_salario)
                break
        
        tree.write(archivo_xml, encoding='utf-8', xml_declaration=True)
    except FileNotFoundError:
        print("Archivo XML no encontrado.")

    print(f"Salario de {nombre_empleado} actualizado a {nuevo_salario}.")



def consultar_empleado(nombre_empleado, archivo_json, archivo_xml):
    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            empleados_json = json.load(archivo)
        
        for empleado in empleados_json:
            if empleado['nombre'] == nombre_empleado:
                print("Empleado encontrado en JSON:", empleado)
                break
        else:
            print(f"No se encontró el empleado {nombre_empleado} en el archivo JSON.")
    except FileNotFoundError:
        print("Archivo JSON no encontrado.")
    
    try:
        tree = ET.parse(archivo_xml)
        root = tree.getroot()
        
        for empleado in root.findall('empleado'):
            nombre = empleado.find('nombre').text
            if nombre == nombre_empleado:
                datos = {
                    'nombre': nombre,
                    'edad': empleado.find('edad').text,
                    'departamento': empleado.find('departamento').text,
                    'salario': empleado.find('salario').text
                }
                print("Empleado encontrado en XML:", datos)
                break
        else:
            print(f"No se encontró el empleado {nombre_empleado} en el archivo XML.")
    except FileNotFoundError:
        print("Archivo XML no encontrado.")



archivo_json = "empleados_ejercicio1.json"
archivo_xml = "empleados_ejercicio1.xml"


def menu():
    while True:
        print("\n1. Agregar empleado")
        print("2. Actualizar salario de empleado")
        print("3. Consultar empleado")
        print("4. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == '1':
            agregar_empleado_terminal(archivo_json, archivo_xml)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del empleado cuyo salario desea actualizar: ")
            nuevo_salario = float(input("Ingrese el nuevo salario: "))
            actualizar_salario(nombre, nuevo_salario, archivo_json, archivo_xml)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del empleado que desea consultar: ")
            consultar_empleado(nombre, archivo_json, archivo_xml)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("opcion no válida, intenta de nuevo.")


menu()
