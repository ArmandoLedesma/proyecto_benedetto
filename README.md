### Crear Login con PYTHON - FLASK y MYSQL

Este proyecto proporciona un sistema de inicio de sesión implementado con Python Flask y MySQL.

### PASO 1: Crear entorno virtual
	python -m venv env


### PASO 2: Activar el entorno virtual
	. env/Scripts/activate

### PASO 3: Instalar Flask
	pip install flask

### PASO 4: Instalar Python MySQL Connector
	pip install mysql-connector-python

### Crear/Actualizar el archivo requirements.txt
pip freeze > requirements.txt

## IMPORTANTE: Para ejecutar el proyecto, instalar dependencias desde requirements.txt

pip install -r requirements.txt

#### Correr el proyecto
	python app.py

Visitar la url: http://127.0.0.1:8000

## Colores

border-lime-600 bg-lime-500



####
## CONFIGURACION INICIAL

# Configuracion

1. Primero se debe instalar un entorno virtual y luego activarlo
2. Se instalan los requerimientos de python
    pip install -r requirements.txt
3. Se instalan los modulos de node
    npm install 

# Creacion de la estructura del proyecto

# Adiciones y actualizaciones

Carpeta molules > Para separar con modulos con estructura modelo, repositorio, servicio controlador
Carpeta database para instanciar sqlalchemy, con el archivo db.py, create_db.py para inicializar la db
Carpeta Schema para futuras actualizaciones con pydantic


.env
.env.exameple
requirements.txt



mkdir modules schemas static views templates database

mkdir -p static/{js,css,img}
mkdir -p modules/{users,clients,products,sales,categories} 
touch schemas/{users.py,clients.py,products.py,sales.py,categories.py} 
mkdir -p templates/{dashboard,auth,main,users,clients,products,sales,categories}

touch database/db.py
touch views/routes.py
touch create_db.py

touch modules/users/{model.py,repositories.py,services.py,routes.py}
touch modules/clients/{model.py,repositories.py,services.py,routes.py}
touch modules/products/{model.py,repositories.py,services.py,routes.py}
touch modules/sales/{model.py,repositories.py,services.py,routes.py}
touch modules/categories/{model.py,repositories.py,services.py,routes.py}

