# PRÀCTICA 7 - PYTHON AMB JSON, XML I CSV

1. Crear una funció que retorni un XML (crear arxiu .xml i mostra per consola l’XML). La funció
ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:

  a. Un root de nom students.

  b. Cinc childs (del root) amb nom student.

  c. Cada child student ha de tindre 4 subchilds

    i. name

    ii. surname
  
    iii. email

    iv. dni

d. Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child
“student”.

e. El text de cada etiqueta serà a la vostra elecció

2. Crear una funció que mostri, per consola i guardi en un arxiu extern, un JSON amb una key
de nom book que contindrà titel, cover, year i pages. Dintre del JSON hi hauran 4 de cada
book.

Crear una funció que llegeixi el JSON de l’exercici 2 i surti el resultat (en format json) per
consola.

3. Crear una funció que escrigui un csv (a un arxiu i per consola) i una altra funció que llegeixi el
csv i mostri per consola el contingut (caldrà importar paquet csv) NO UTILITZAR PAQUET
PANDAS. Cal explicar linea per linea (amb comentaris) què està passant en el codi.

El text a escriure al csv ha de ser el següent:

data = [["Name", "Surname", "Age"], ["XXXX", "XXXXXX", "XXXXX"]]

Crear una funció que escrigui un arxiu excel i una altra funció que llegeixi un excel (caldrà
importar el paquet openpyxl). Cal explicar linea per linea (amb comentaris) què està passant
en el codi.

(Cal que quedi emplenat, com a mínim, una casella)

Pista per csv ⇒ mirar els mètodes writer() i reader()

Pista per openpyxl ⇒ mirar el mètode load_workbook(), workbook(), worksheets(), save() i
active.


## Repository Authors✒️

-   Joel Felipe Díaz Carissimi - [joeldiazcc](https://github.com/joeldiazcc)

-   Luis Andres Castillo Ensinas - [lcastienc](https://github.com/lcastienc)

-   Ivan Nikola Petrov Perchev - [ipetrov20](https://github.com/ipetrov20)
