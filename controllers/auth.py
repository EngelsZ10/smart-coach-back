import requests
from ftplib import FTP
from flask import request, jsonify


def login():
    email = request.args.get("email")
    pas = request.args.get("pass")
    equipo = request.args.get("equipo").lower()

    if equipo != 'admin':
        temp = email.split("@")
        email = temp[0] + f"@{equipo}." + temp[1]
    
        response = requests.get(
            f"https://smartcoach.top:2083/execute/Email/verify_password?email={email}&password={pas}",
            headers={
                "Authorization": "cpanel df3artco4sf:82D3MJ2G4DTK5G5FYAAPKW8XASRNOT6Z"}
        )
        
        
        resp = {
            "response": bool(response.json()['data']),
            "Admin": True if email == "df3artco4sf" else False,
            "mensaje": response.json(),
        }
    else:
        ftp = FTP("ftp.smartcoach.top")
        try:
            r = ftp.login(email, pas)
        except Exception as e:
            r = e
        resp = {
            "response": r.__str__()[:3] == '230',
            "Admin": r.__str__()[:3] == '230',
            "mensaje": r.__str__()
        }
        ftp.quit()
    return jsonify(resp)



