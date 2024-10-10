import os
import shutil

def clear_static():
    # Define las rutas de las carpetas
    images_dir = 'static/images'
    audio_dir = 'static/audio'

    # Vaciar la carpeta images
    if os.path.exists(images_dir):
        shutil.rmtree(images_dir)
        os.makedirs(images_dir)  # Recreate the directory

    # Vaciar la carpeta audio
    if os.path.exists(audio_dir):
        shutil.rmtree(audio_dir)
        os.makedirs(audio_dir)  # Recreate the directory

    print("Folders 'images' and 'audio' have been cleared.")

if __name__ == '__main__':
    clear_static()