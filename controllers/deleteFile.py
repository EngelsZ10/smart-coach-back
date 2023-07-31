from ftplib import FTP

def deleteFile(dir):
    try:
        # Conectarse al servidor FTP
        ftp = FTP("ftp.smartcoach.top")
        ftp.login("df3artco4sf@smartcoach.top", "9de6AGnZ0!k*9Tus")

        # Eliminar el archivo en el servidor
        ftp.delete(dir)

        # Cerrar la conexión FTP
        ftp.quit()

        return "Archivo eliminado con éxito del servidor FTP."
    except Exception as e:
        return f"Error al eliminar el archivo del servidor FTP: {e}"