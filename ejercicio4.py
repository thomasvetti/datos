from lxml import etree

def validar_xml_xsd(archivo_xml, archivo_xsd):

    try:
        with open(archivo_xsd, 'rb') as schema_file:
            schema_root = etree.XML(schema_file.read())
            schema = etree.XMLSchema(schema_root)
    except etree.XMLSyntaxError as e:
        print(f"Error de sintaxis en el archivo XSD: {e}")
        return
    except Exception as e:
        print(f"Error al abrir el archivo XSD: {e}")
        return

   
    xmlparser = etree.XMLParser(schema=schema)
    try:
        with open(archivo_xml, 'rb') as xml_file:
            etree.fromstring(xml_file.read(), xmlparser)
        print("El archivo XML es válido según el esquema XSD.")
    except etree.XMLSyntaxError as e:
        print(f"Error en la validación del XML: {e}")
    except Exception as e:
        print(f"Error al abrir el archivo XML: {e}")


validar_xml_xsd("empleados.xml", "empleados.xsd")
