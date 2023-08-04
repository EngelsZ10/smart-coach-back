import requests
from flask import request


def addUsuario():
    equipos = [
        'baby',
        'falcons',
        'flag',
        'hornets',
        'intermedia',
        'irons',
        'juvenil',
        'master',
        'ponys',
        'rabbits',
        'tauros'
    ]

    user = request.args.get("user")
    pas = request.args.get("pass")
    equipo = request.args.get("equipo").lower()

    if equipo in equipos:
        response = requests.get(
            f"https://smartcoach.top:2083/execute/Email/add_pop?email={user}&password={pas}&domain={equipo}.smartcoach.top",
            headers={
                "Authorization": "cpanel df3artco4sf:82D3MJ2G4DTK5G5FYAAPKW8XASRNOT6Z"}
        )
    else:
        response = {"status": 0, "error": ["equipo no valido"]}

    return response.json()
