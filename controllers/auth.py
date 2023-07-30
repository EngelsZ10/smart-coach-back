from ftplib import FTP
from flask import request, jsonify
import requests


def login():
    email = request.args.get("email")
    pas = request.args.get("pass")
    equipo = request.args.get("equipo")

    response = requests.get(
        f"https://smartcoach.top:2083/execute/Email/verify_password?email={email}@{equipo}.smartcoach.top&password={pas}",
        headers={
            "Authorization": "cpanel df3artco4sf:82D3MJ2G4DTK5G5FYAAPKW8XASRNOT6Z"}
    )

    resp = {
        "response": response.json()['data'],
        "Admin": True if email == "df3artco4sf" else False,
        "response": response
    }

    return jsonify(resp)
