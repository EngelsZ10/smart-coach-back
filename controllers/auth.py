from ftplib import FTP
from flask import request, jsonify

def login():
    email = request.args.get("email")
    pas = request.args.get("pass")
    ftp = FTP("ftp.smartcoach.top")
    try:
        r = ftp.login(f"{email}", pas)
    except Exception as e:
        r = e
    resp = {
        "response": True if r.__str__()[:3] == '230' else False,
        "Admin": True if r.__str__()[:3] == '230' and email == "df3artco4sf" else False,
        "mensaje": r.__str__()
    }
    ftp.quit()
    return jsonify(resp)

