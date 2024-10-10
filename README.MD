Necesitamos una web que reciba informacion (audio imagen texto) y la mande a la api de openai
    para entonces mostrar la respuesta y almacenarla en una base de datos 

para analizar el audio --  Windows AsemblyAI  libreria de python (`pip install assemblyai`)

para analizar la imagen -- se installa manualmente (tesseract)

para analizar el tempo -- Essentia (libreria de python)

analizar toda esta informacion en conjunto con OPENAI (otra opciones : IBM Watson Natural Language Understanding |||| Google Cloud Natural Language AP )





(((((En resumen, la estrategia consiste en conectar servicios de transcripcion y analisis musical a traves de un flujo automatizado que se dispara con la subida de una cancion. Esta aproximacion ofrece flexibilidad y un proceso optimizado sin requerir programacion avanzada.
WEB - Nombre artista, nombre tema, si es album , EP o single, descripción del tema, Portada y WAV del tema  )))))


que necesita nuestro formulario : 
    nombre del artista 
    nombre del tema
    si es album EP o single 
    descripcion del tema 
    una imagen para la portada 
    y la posibilidad de subir un archivo de audio 