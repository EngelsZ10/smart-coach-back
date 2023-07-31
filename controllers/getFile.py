import requests
from ftplib import FTP
from PIL import Image
from io import BytesIO
from flask import jsonify, request
import base64
import mimetypes


downloaded_data = b""


def getFiles():
    # Datos de acceso a cPanel
    url = 'https://ftp.smartcoach.top:2083/execute/Fileman/list_files'
    token= "cpanel df3artco4sf:82D3MJ2G4DTK5G5FYAAPKW8XASRNOT6Z"

    # Configuración de los parámetros
    params = {
        'dir': request.args.get("dir"),
    }
 
    # Configuración de la cabecera de autenticación
    headers = {
        'Authorization': f'{token}',
    }

    # Realizar la solicitud a la API
    response = requests.get(url, params=params, headers=headers, verify=False)

    # Procesar la respuesta JSON
    if response.status_code == 200:
        info_video = response.json()
        datos = info_video["data"]
        nombres_archivos = []
        
        for archivo in datos:
            if archivo["type"] != 'file':
                continue
            if not mimetypes.guess_type(archivo["file"])[0].startswith('video'):
                continue
            nombres_archivos.append(archivo["file"].split(".")[:-1])
            
        return nombres_archivos
        
    else:
        return f"[!] Error: {response.status_code} {response.reason} returned."
    
def getImageBi(dir):
    ftp = FTP("ftp.smartcoach.top")
    ftp.login(user="df3artco4sf@smartcoach.top", passwd="9de6AGnZ0!k*9Tus")

    flo = BytesIO()
    ftp.retrbinary('RETR ' + dir, flo.write)
    flo.seek(0)
    img = Image.open(flo)
    
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    imagen_binaria = buffer.getvalue()
    
    imagen_base64 = base64.b64encode(imagen_binaria).decode("utf-8")
    
    # Cerrar la conexión FTP
    ftp.quit()
    flo.close()
    buffer.close()
    
    return jsonify({"imagen_base64": imagen_base64})

