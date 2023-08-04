import requests
from ftplib import FTP

def uploadFile(dir_local, dir_remoto):
    try:
        # Conectarse al servidor FTP
        ftp = FTP("ftp.smartcoach.top")
        ftp.login("df3artco4sf@smartcoach.top", "9de6AGnZ0!k*9Tus")

        # Subir el archivo al servidor
        with open(dir_local, 'rb') as file:
            ftp.storbinary('STOR ' + dir_remoto, file)

        # Cerrar la conexión FTP
        ftp.quit()

        return "Archivo subido con éxito al servidor FTP."
    except Exception as e:
        return f"Error al subir el archivo al servidor FTP: {e}"