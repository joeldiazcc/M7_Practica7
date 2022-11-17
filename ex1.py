import xml.etree.ElementTree as ET

#Funció on es gurda la creacio de la tabla
def llista():

    #Creacio del root del XML
    root = ET.Element('students')
    # creacio dels childs
    # Primer child
    child = ET.SubElement(root, 'student')
    # Afegim id al child
    child.set('id', '1')
    name = ET.SubElement(child, 'name')
    name.text = 'Luis'
    surname = ET.SubElement(child, 'surname')
    surname.text = 'Castillo'
    email = ET.SubElement(child, 'email')
    email.text = 'castilloluis166@gmail.com'
    dni = ET.SubElement(child, ' dni')
    dni.text = '22894657C'
    # Segon child
    child = ET.SubElement(root, 'student')
    # Afegim id al child
    child.set('id', '2')
    name = ET.SubElement(child, 'name')
    name.text = 'Gines'
    surname = ET.SubElement(child, 'surname')
    surname.text = 'Bueno'
    email = ET.SubElement(child, 'email')
    email.text = 'Gbueno142343@invodua.com'
    dni = ET.SubElement(child, ' dni')
    dni.text = '88313143C'
    # Tercer child
    child = ET.SubElement(root, 'student')
    # Afegim id al child
    child.set('id', '3')
    name = ET.SubElement(child, 'name')
    name.text = 'Maria Mar'
    surname = ET.SubElement(child, 'surname')
    surname.text = 'Agudo'
    email = ET.SubElement(child, 'email')
    email.text = 'mmar123@gufum.com'
    dni = ET.SubElement(child, ' dni')
    dni.text = '60831077X'
    # Cuart child
    child = ET.SubElement(root, 'student')
    # Afegim id al child
    child.set('id', '4')
    name = ET.SubElement(child, 'name')
    name.text = 'Eliseo'
    surname = ET.SubElement(child, 'surname')
    surname.text = 'Menendez'
    email = ET.SubElement(child, 'email')
    email.text = 'EliMendez@gmail.com'
    dni = ET.SubElement(child, ' dni')
    dni.text = '93522419A'
    # cinque child
    child = ET.SubElement(root, 'student')
    # Afegim id al child
    child.set('id', '5')
    name = ET.SubElement(child, 'name')
    name.text = 'Lúcia '
    surname = ET.SubElement(child, 'surname')
    surname.text = 'Barragan'
    email = ET.SubElement(child, 'email')
    email.text = 'Mbarragan@gmail.com'
    dni = ET.SubElement(child, ' dni')
    dni.text = '98736828J'

    # Escribim com queda el document XML en aquest o un altre arxiu,
    tree = ET.ElementTree(root)
    tree.write("Llista.xml")

    # Afegim un tabulador al root
    ET.indent(root)
    # Afegim una indentació al elements
    ET.indent(tree)
    # Mostrar per consola
    ET.dump(root)
#Cridem la funcio per veure el XML creat
llista()