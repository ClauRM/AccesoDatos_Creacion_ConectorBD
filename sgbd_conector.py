import subprocess

class Sgbd:
    
    #constructor
    def __init__(self,sgbd,basededatos):
        self.sgbd = sgbd
        self.basededatos = basededatos
        
    #metodos
    def insert(self,coleccion,documento,contenido):
        self.operacion = "insert"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido

        comando = ''+self.sgbd+' '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' "'+self.contenido+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

        if resultado.returncode == 0:
            print("Registro insertado correctamente")
            return("ok insert")
            
        else:
            print("Error al ejecutar insert")
            print(resultado)
            return("ko insert")
            

    def select(self,coleccion,documento):
        self.operacion = "select"
        self.coleccion = coleccion
        self.documento = documento

        comando = ''+self.sgbd+' '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+''
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        print(resultado.stdout) #mostrar salida
        
        if resultado.returncode == 0:
            return("ok select")
        else:
            return("ko select")

    def create_collection(self,coleccion):
        self.operacion = "create_collection"
        self.coleccion = coleccion

        comando = ''+self.sgbd+' '+self.operacion+' '+self.basededatos+' '+self.coleccion+''
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        
        if resultado.returncode == 0:
            return("ok create_collection")
        else:
            return("ko create_collection")

    def where(self,coleccion,documento,busqueda):
        self.operacion = "where"
        self.coleccion = coleccion
        self.documento = documento
        self.busqueda = busqueda

        comando = ''+self.sgbd+' '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' "'+busqueda+'"'
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        print(resultado.stdout) #mostrar salida
        
        if resultado.returncode == 0:
            return("ok where")
        else:
            return("ko where")


        
