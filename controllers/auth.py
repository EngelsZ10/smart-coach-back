from ftplib import FTP
from flask import request, jsonify

def login():
    user = request.args.get("user")
    pas = request.args.get("pass")
    ftp = FTP("ftp.smartcoach.top")
    try:
        r = ftp.login(f"{user}@smartcoach.top", pas)
    except Exception as e:
        r = e
    resp = {
        "response": True if r.__str__()[:3] == '230' else False,
        "Admin": True if r.__str__()[:3] == '230' and user == "df3artco4sf" else False,
        "mensaje": r.__str__()
    }
    ftp.quit()
    return jsonify(resp)

