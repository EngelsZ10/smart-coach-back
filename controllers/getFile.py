import requests
import json
from flask import request

token = "cpanel df3artco4sf:82D3MJ2G4DTK5G5FYAAPKW8XASRNOT6Z"


def getVideos():
    # Datos de acceso a cPanel
    url = 'https://ftp.smartcoach.top:2083/execute/Fileman/list_files'

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
            nombres_archivos.append(archivo["file"])

        return nombres_archivos

    else:
        return f"[!] Error: {response.status_code} {response.reason} returned."


def getThumbnails():
    url = 'https://ftp.smartcoach.top:2083/execute/ImageManager/create_thumbnails'

    # Configuración de los parámetros
    params = {
        'dir': request.args.get("dir"),
        "height_percentage": 50,
        "width_percentage": 50,
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

        return info_video

    else:
        return f"[!] Error: {response.status_code} {response.reason} returned."
