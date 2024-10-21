import xml.etree.ElementTree as ET
import json


def crear_catalogo_xml(archivo_xml):

    root = ET.Element('catalogo')

    productos = [
        {'id': '1', 'nombre': 'Laptop', 'descripcion': 'Laptop de 15 pulgadas', 'precio': '800', 'stock': '10'},
        {'id': '2', 'nombre': 'Mouse', 'descripcion': 'Mouse inalámbrico', 'precio': '20', 'stock': '50'},
        {'id': '3', 'nombre': 'Teclado', 'descripcion': 'Teclado mecánico', 'precio': '60', 'stock': '30'},
        {'id': '4', 'nombre': 'Monitor', 'descripcion': 'Monitor 24 pulgadas', 'precio': '150', 'stock': '20'},
        {'id': '5', 'nombre': 'Impresora', 'descripcion': 'Impresora multifuncional', 'precio': '120', 'stock': '15'}
    ]

   
    for producto in productos:
        producto_element = ET.SubElement(root, 'producto')
        ET.SubElement(producto_element, 'id').text = producto['id']
        ET.SubElement(producto_element, 'nombre').text = producto['nombre']
        ET.SubElement(producto_element, 'descripcion').text = producto['descripcion']
        ET.SubElement(producto_element, 'precio').text = producto['precio']
        ET.SubElement(producto_element, 'stock').text = producto['stock']

    tree = ET.ElementTree(root)
    tree.write(archivo_xml, encoding='utf-8', xml_declaration=True)
    print(f"Catálogo creado en {archivo_xml}")

def modificar_stock(archivo_xml, producto_id, nuevo_stock):
    try:
        tree = ET.parse(archivo_xml)
        root = tree.getroot()

        for producto in root.findall('producto'):
            id_producto = producto.find('id').text
            if id_producto == producto_id:
                producto.find('stock').text = str(nuevo_stock)
                break
        else:
            print(f"No se encontró el producto con ID {producto_id}.")

        tree.write(archivo_xml, encoding='utf-8', xml_declaration=True)
        print(f"Stock del producto con ID {producto_id} actualizado a {nuevo_stock}.")
    except FileNotFoundError:
        print(f"Archivo {archivo_xml} no encontrado.")

def exportar_a_json(archivo_xml, archivo_json):
    try:
        tree = ET.parse(archivo_xml)
        root = tree.getroot()

        productos = []
        for producto in root.findall('producto'):
            productos.append({
                'id': producto.find('id').text,
                'nombre': producto.find('nombre').text,
                'descripcion': producto.find('descripcion').text,
                'precio': producto.find('precio').text,
                'stock': producto.find('stock').text
            })

        with open(archivo_json, 'w', encoding='utf-8') as archivo:
            json.dump(productos, archivo, indent=4, ensure_ascii=False)

        print(f"Catálogo exportado a {archivo_json}.")
    except FileNotFoundError:
        print(f"Archivo {archivo_xml} no encontrado.")

def buscar_producto(archivo_json, producto_id):
    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            productos = json.load(archivo)

        for producto in productos:
            if producto['id'] == producto_id:
                print("Producto encontrado:", producto)
                break
        else:
            print(f"No se encontró el producto con ID {producto_id}.")
    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")

def menu():
    archivo_xml = "catalogo.xml"
    archivo_json = "catalogo.json"

    crear_catalogo_xml(archivo_xml)

    while True:
        
        print("1. Modificar stock de un producto")
        print("2. Exportar catálogo a JSON")
        print("3. Buscar producto por ID en JSON")
        print("4. Salir")
        
        opcion = input("Elige una opcion: ")

        if opcion == '1':
            producto_id = input("Ingresa el ID del producto cuyo stock deseas modificar: ")
            nuevo_stock = int(input("Ingresa el nuevo stock: "))
            modificar_stock(archivo_xml, producto_id, nuevo_stock)
        
        elif opcion == '2':
            exportar_a_json(archivo_xml, archivo_json)
        
        elif opcion == '3':
            producto_id = input("Ingresa el ID del producto que deseas buscar: ")
            buscar_producto(archivo_json, producto_id)
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("opcion no valida. Intentalo de nuevo.")

menu()