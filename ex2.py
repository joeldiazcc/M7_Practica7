import json
# Funció que mostri per consolai guardi en un arxiu JSON.
def showJson():
    # Hi hauran 4 de cada book amb una key de nom book
    # que contindrà title, cover, year i pages.
    datas = {
        'book': [
            {
                'title': 'aaa',
                'cover': 'a',
                'year': '2001',
                'pages': '121'
            },
            {
                'title': 'bbb',
                'cover': 'b',
                'year': '2002',
                'pages': '122'
            },
            {
                'title': 'ccc',
                'cover': 'c',
                'year': '2003',
                'pages': '123'
            },
            {
                'title': 'ddd',
                'cover': 'd',
                'year': '2004',
                'pages': '124'
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
