import os
basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.join(basedir,'img')
images = os.listdir(basedir)

for index,img in enumerate(images):
    src = os.path.join(basedir,img)
    dst = os.path.join(basedir,str(index)+img[-4:])
    print(f"Renaming {src} to {dst}...")
    try:
        os.rename(src,dst)
        print("Successful")
    except:
        print('error for this image')
    
print('Finished')
    