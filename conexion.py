from sgbd_conector import Sgbd #importar la clase Sgbd del fichero sgbd_conector.py

'''
METODOS
- insert(coleccion,documento,contenido)
- select(coleccion,documento)
- create_collection(coleccion)
- where(coleccion,documento,busqueda)
'''

Conexion1 = Sgbd("miempresa") #objeto conexion
Conexion1.insert("clientes2","cliente23","Pato Donald")


