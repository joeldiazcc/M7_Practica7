import json
# Funció que mostri per consolai guardi en un arxiu JSON.
def showJson():
    # Hi hauran 4 de cada book amb una key de nom book
    # que contindrà title, cover, year i pages.
    datas = {
        'book': [
            {
                'title': 'Odisea, de Homero',
                'cover': 'blanda',
                'year': '2005',
                'pages': '224'
            },
            {
                'title': 'Lolita, de Vladimir Nabokov',
                'cover': 'dura',
                'year': '1996',
                'pages': '392'
            },
            {
                'title': 'El código Da Vinci, de Dan Brown',
                'cover': 'dura',
                'year': '2016',
                'pages': '656'
            },
            {
                'title': 'Robinson Crusoe, de Daniel Defoe',
                'cover': 'blanda',
                'year': '1719',
                'pages': '608'
            }
        ]
    }
    # Guardem el JSON en books.json
    with open("books.json", 'w') as write:
        json.dump(datas, write)
    print(json.dumps(datas))
#Crear una funció que llegeixi el JSON de l’exercici 2 i surti el resultat (en format json) per consola.
def readJson():
    # Llegim el arxiu books.json
    with open("books.json", 'r') as read:
        result = json.load(read)
        # Ho mostrem per pantalla
        print(result)

#Provem les funcions
print("\nMostrar per consola i guardar json en books.json:")
showJson()
print("\nMostrar per consola el contingut del ariux books.json:")
readJson()
