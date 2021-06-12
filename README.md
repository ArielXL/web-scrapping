# Web Scrapping

## Sobre los autores

**Nombre y Apellidos** | **Correo** | **GitHub**
--|--|--
Ariel Plasencia Díaz | arielplasencia00@gmail.com | [@ArielXL](https://github.com/ArielXL)
Adriana Plasencia Díaz | adricivilpd@gmail.com | [@fcadrianapladia](https://github.com/fcadrianapladia)

## Sobre el Scrapper

El objetivo de esta pequeña tarea es proporcionar un scrapper para páginas web con el objetivo de poder descargar todo su contenido. También con esta técnica podemos extraer información y transformarla en información estructurada que podemos analizar y almacenar.

## Sobre la implementación

La implementación se encuentra totalmente en [python 3](https://es.wikipedia.org/wiki/Python). Pensamos que es una implementación legible y fácil de entender donde no hace falta tener conocimientos profundos de este lenguaje de programación. Nos apoyamos fundamentalmente en la librería [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html) para la implementación.
La clase Scrapper recibe la url en forma de string y un entero que representa el nivel de profundidad a realizar el web scrapping. Los resultados se muestran en la carpeta [src/downloads](src/downloads/).

Para la instalación de la misma ejecutamos el siguiente comando:

```bash
pip install -r requirements.txt
```

## Sobre la ejecución

En el archivo [`makefile`](src/makefile) proveemos una manera fácil, sencilla y rápida para correr nuestra implementación.

Para la ejecución, escriba las siguientes líneas en una terminal abierta en este directorio:

```bash
cd src/
make run
```
