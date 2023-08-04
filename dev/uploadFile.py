from flask import request
from ftplib import FTP
from moviepy.editor import VideoFileClip
from PIL import Image
from os.path import splitext
from self.localauth import auth

def create_thumbnail(file_path, time_in_seconds=0):
    try:
        clip = VideoFileClip(file_path)
        thumbnail = clip.get_frame(time_in_seconds)
        img = Image.fromarray(thumbnail)
        img.save(splitext(file_path)[0] +".jpg")
        return splitext(file_path)[0] +".jpg"
    except Exception as e:
        return f"Error creating thumbnail: {e}"
        

def upload_file_to_cpanel():
    email = request.args.get("user")
    pas = request.args.get("pas")
    equipo = request.args.get("equipo")
    if not auth(email,pas,equipo ):
        return "Error de autenticación"
    
    dir = request.args.get("dir")
    file = request.files['video']
    filename = file.filename
    name = lambda dir, p:  "" if dir[p] == "/" else "/"
    file.save(".."+ name(dir, 0) + dir + name(dir, -1)  + filename)
    img = create_thumbnail(".."+ name(dir, 0) + dir + name(dir, -1)  + filename)
    return img
 
