import subprocess

class sgbd:
    #constructor
    def __init__(self,basededatos):
        self.basededatos = basededatos
    #metodos
    def insert(self):
        self.operacion = "insert"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido

        comando = '"C:\\Users\\claud\\OneDrive\\Documentos\\IMF\\2 DAM\\Acceso a datos\\Prácticas\\005-Creación de un conector de BD\\sgbd.exe" '+operacion+' '+basededatos+' '+coleccion+' '+documento+' "'+contenido+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            return("ok insert")
        else:
            return("ko insert")
