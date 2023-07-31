from ftplib import FTP
from flask import request, jsonify, make_response
import requests


def login():
    email = request.args.get("email")
    pas = request.args.get("pass")
    equipo = request.args.get("equipo").lower()

    if equipo != 'Admin':
        temp = email.split("@")
        email = temp[0] + f"@{equipo}." + temp[1]
    
    response = requests.get(
        f"https://smartcoach.top:2083/execute/Email/verify_password?email={email}&password={pas}",
        headers={
            "Authorization": "cpanel df3artco4sf:82D3MJ2G4DTK5G5FYAAPKW8XASRNOT6Z"}
    )
    resp = {
        "response": response.json()['data'],
        "Admin": True if email == "df3artco4sf" else False,
        "mensaje": response.json()
    }
    return jsonify(resp)

