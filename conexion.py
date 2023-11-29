import subprocess

comando = '"C:\\Users\\claud\\OneDrive\\Documentos\\IMF\\2 DAM\\Acceso a datos\\Prácticas\\005-Creación de un conector de BD\\sgbd.exe" insert miempresa clientes1 cliente3 "Oscar Rodriguez"'
resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

if resultado.returncode == 0:
    print("ok")
else:
    print("ko")
