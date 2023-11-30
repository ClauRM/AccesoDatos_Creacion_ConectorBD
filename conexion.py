from sgbd_conector import Sgbd #importar la clase Sgbd del fichero sgbd_conector.py

'''
METODOS
- insert(coleccion,documento,contenido)
- select(coleccion,documento)
- create_collection(coleccion)
- where(coleccion,documento,busqueda)
'''

Conexion1 = Sgbd('"C:\\Users\\claud\\OneDrive\\Documentos\\IMF\\2 DAM\\Acceso a datos\\Prácticas\\005-Creación de un conector de BD\\sgbd.exe"',"miempresa") #objeto conexion
Conexion1.where("clientes4","cliente41","Claudi")


