"# AP_OPENAI" 

El objetivo del proyecto es un lab de integracion entre Open AI y diferentes servicios. 

integraremos Open AI con cuenta corporativa y usaremos GeneXus Enterpise AI

#Primeros Pasos

python -m venv venv

#Luego, activa el entorno virtual:

##En Windows:

.\venv\Scripts\activate

##En macOS y Linux:

source venv/bin/activate

##Instalación

pip install -r requirements.txt  

pip install openai


##es buena practica instalar el pip-tools Usando pip-tools

#Instala pip-tools:

pip install pip-tools

#Genera el archivo requirements.txt desde pyproject.toml:

pip-compile pyproject.toml

#Instala las dependencias desde requirements.txt:

pip install -r requirements.txt

