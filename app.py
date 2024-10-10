import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Recoger datos del formulario
        artist_name = request.form.get('artist-name')
        track_name = request.form.get('track-name')
        type_of_release = request.form.get('type')
        description = request.form.get('description')
        
        # Recoger archivos (imagen de portada y archivo de audio)
        cover_image = request.files['cover-image']
        audio_file = request.files['audio-file']

        # Crear directorios si no existen
        os.makedirs('static/images', exist_ok=True)
        os.makedirs('static/audio', exist_ok=True)

        # Definir la ruta de la imagen predeterminada
        default_image_path = 'noImage/no-image.png'
        
        # Nombre del archivo para almacenar
        cover_image_filename = cover_image.filename if cover_image and cover_image.filename else 'no-image.png'

        # Guardar la imagen de portada
        if cover_image and cover_image.filename:
            cover_image.save(f'static/images/{cover_image_filename}')
        else:
            # Si no se subió imagen, copiar la imagen predeterminada
            os.rename(default_image_path, f'static/images/{cover_image_filename}')

        # Guardar el archivo de audio
        if audio_file and audio_file.filename:
            audio_file.save(f'static/audio/{audio_file.filename}')

        # Imprimir los datos en la consola
        print("Artista:", artist_name)
        print("Tema:", track_name)
        print("Tipo:", type_of_release)
        print("Descripción:", description)

        # Pasar la URL de la imagen
        image_url = cover_image_filename
        
        return render_template('completed.html', image_url=image_url)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
