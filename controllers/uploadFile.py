from flask import request
from ftplib import FTP


def upload_file_to_cpanel():
    user = request.args["user"]
    pas = request.args["pas"]
    dir = request.form["dir"]
    filename = request.files

    try:
        # Crear una instancia del objeto FTP
        ftp = FTP().connect("ftp.smartcoach.top")

        # Iniciar sesión con el nombre de usuario y contraseña
        ftp.login(user, pas)

        # Cambiar al directorio remoto en el servidor (si es necesario)
        ftp.cwd(dir)

        # Abrir el archivo local en modo binario
        with open(filename, "rb") as file:
            # Subir el archivo al servidor
            ftp.storbinary(f"STOR {filename}", file)

        # Cerrar la conexión FTP
        ftp.quit()

        print(
            f"Archivo {filename} subido exitosamente a {ftp_server}/{remote_directory}")
    except Exception as e:
        print(f"Error al subir el archivo: {e}")
