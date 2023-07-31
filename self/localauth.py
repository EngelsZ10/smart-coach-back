import requests
from ftplib import FTP

def auth(email,pas,equipo ):
    if equipo.lower() != 'admin':
        temp = email.split("@")
        email = temp[0] + f"@{equipo}." + temp[1]
    
        response = requests.get(
            f"https://smartcoach.top:2083/execute/Email/verify_password?email={email}&password={pas}",
            headers={
                "Authorization": "cpanel df3artco4sf:82D3MJ2G4DTK5G5FYAAPKW8XASRNOT6Z"}
        )
        
        
        return bool(response.json()['data'])
    else:
        ftp = FTP("ftp.smartcoach.top")
        try:
            r = ftp.login(email, pas)
        except Exception as e:
            r = e
        return  r.__str__()[:3] == '230'