# Proyecto de Información de Sismos en Chile
- [Sismos en Chile en tiempo real](https://sismoschile.com/)
Este proyecto, desarrollado con Django, Bootstrap, CSS, HTML, JavaScript y mapas Leaflet, es una plataforma sin fines de lucro que tiene como objetivo proporcionar información precisa sobre los sismos ocurridos en Chile.

## Características

- La plataforma se actualiza periódicamente cada 5 minutos.
- Utiliza colores para resaltar la magnitud de los sismos:
  - Información en verde para sismos menores a 3.0 ML.
  - Información en morado para sismos entre 3.0 ML y 5.0 ML.
  - Información en rojo para sismos mayores a 5.0 ML.
- La fuente de datos proviene de una API externa [https://xor.cl/api/sismo/](https://xor.cl/api/sismo/), la cual no fue desarrollada por el autor de esta página.
- Este proyecto se ha creado con fines educativos e informativos y lleva la autoría de Emanuel Bustos.

## Tecnologías Utilizadas

- Django
- Bootstrap
- CSS
- HTML
- JavaScript
- Mapas Leaflet

## Instalación

1. Clona este repositorio
2. Ve al directorio del proyecto: `cd nombre-del-proyecto`
3. Crea un entorno virtual: `python -m venv venv`
4. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En macOS y Linux: `source venv/bin/activate`
5. Instala las dependencias: `pip install -r requirements.txt`
6. Ejecuta el servidor: `python manage.py runserver`

## Contribución

Si deseas contribuir a este proyecto, ¡serás bienvenido! Siéntete libre de crear un "pull request" con tus mejoras.

## Contacto

Si tienes preguntas o comentarios sobre este proyecto, puedes contactar al autor:

Emanuel Bustos
Correo electrónico: contact@emanuelbustos.com

## Importante

Cabe destacar que este repositorio no es la versión final de produccion, pero si tiene toda la logica desarrollada.
