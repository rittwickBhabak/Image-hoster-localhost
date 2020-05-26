import os

# Prepare the folder structure
#   img
#   app.py
#   prepareSetup.py
#   templates
#       index.html
#   static
#       img

os.mkdir('templates')
os.mkdir('static')
os.mkdir('static/img')
basedir = os.path.abspath(os.path.dirname(__file__))

# Get the list of all images from 'img' folder
images = os.listdir('img')

# Move the image to the static/img folder
for img in images:
    src = os.path.join(basedir,'img', img)
    dst = os.path.join(basedir,'static','img',img)
    os.rename(src,dst)

# Delete the blank 'img' folder
try:
    os.rmdir('img')
except:
    print('Permission denied. Cannot delete blank image folder')

# Get the list of all images from static/img folder
images = os.listdir(os.path.join(basedir,'static','img'))

with open('templates/index.html','w') as f:
    data = '''<!doctype html>
    <html lang='en'>

    <head>
        <!-- Required meta tags -->
        <meta charset='utf-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>
        <title>Image Hoster</title>
        <style>
            #imageset{
                display: flex;
                justify-content: start;
                flex-wrap: wrap;
            }
            .image{
                display: inline-block;
                width: auto;
                height: auto;
                margin: 20px auto;
            }
            img{
                border: 5px solid black;
                height: 200px;
            }
        </style>
    </head>

    <body>
        <div class="container" id="imageset">'''
    for img in images:
        herf = f"static/img/{img}"
        src = "{{ url_for('static', filename='img/" + img + "') }}"
        temp =  f'<div class="image"><a href="/{herf}" target="_blank"><img src="{src}" alt=""></a></div>'
        data = data + temp
    data = data + '</div></body></html>'
    f.write(data)