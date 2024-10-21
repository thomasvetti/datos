import json
import xml.etree.ElementTree as ET

def crear_encuestas_json(archivo_json):
    encuestas = [
        {
            "ciudad": "Ciudad A",
            "personas_encuestadas": 1200,
            "transporte_mas_utilizado": "Autobús"
        },
        {
            "ciudad": "Ciudad B",
            "personas_encuestadas": 850,
            "transporte_mas_utilizado": "Metro"
        },
        {
            "ciudad": "Ciudad C",
            "personas_encuestadas": 950,
            "transporte_mas_utilizado": "Bicicleta"
        }
    ]

    with open(archivo_json, 'w', encoding='utf-8') as archivo:
        json.dump(encuestas, archivo, indent=4, ensure_ascii=False)
    print(f"Archivo {archivo_json} creado con éxito.")


def generar_resumen_xml(archivo_json, archivo_xml):
    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            encuestas = json.load(archivo)

        root = ET.Element("resumen_encuestas")

        for encuesta in encuestas:
            ciudad_element = ET.SubElement(root, 'ciudad')
            ET.SubElement(ciudad_element, 'nombre').text = encuesta['ciudad']
            ET.SubElement(ciudad_element, 'personas_encuestadas').text = str(encuesta['personas_encuestadas'])
            ET.SubElement(ciudad_element, 'transporte_mas_utilizado').text = encuesta['transporte_mas_utilizado']

        tree = ET.ElementTree(root)
        tree.write(archivo_xml, encoding='utf-8', xml_declaration=True)
        print(f"Resumen generado en {archivo_xml}.")

    except FileNotFoundError:
        print(f"Archivo {archivo_json} no encontrado.")


def visualizar_resumen(archivo_xml):
    try:
        tree = ET.parse(archivo_xml)
        root = tree.getroot()

        print("\nResumen de encuestas de transporte público:\n")
        for ciudad in root.findall('ciudad'):
            nombre = ciudad.find('nombre').text
            personas_encuestadas = ciudad.find('personas_encuestadas').text
            transporte_mas_utilizado = ciudad.find('transporte_mas_utilizado').text
            print(f"Ciudad: {nombre}")
            print(f"Personas encuestadas: {personas_encuestadas}")
            print(f"Transporte más utilizado: {transporte_mas_utilizado}\n")

    except FileNotFoundError:
        print(f"Archivo {archivo_xml} no encontrado.")


archivo_json = "encuestas.json"
archivo_xml = "resumen_encuestas.xml"

crear_encuestas_json(archivo_json)

generar_resumen_xml(archivo_json, archivo_xml)

visualizar_resumen(archivo_xml)
