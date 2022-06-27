# demoquick
Proyecto conocimientos basicos
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1. Descripción general del proyecto.
El presente proyecto se desarrola como pruena de conocimientos tecnicos de Django y DRF
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
2. Estado actual del proyecto, que es particularmente importante si el proyecto está todavía en desarrollo. En él se mencionan los cambios planeados y la dirección de desarrollo del proyecto, y se especifica directamente si un proyecto está terminado.
El proyecto es una DEMO que se encuentra en desarrollo e implementa los requerimientos solicitados y unas cuantas funcionalidades mas.
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
3. Requisitos del entorno de desarrollo para la integración.
Requiere los siguientes paquetes o programas
- python 3.8
- PIP
- VENV
- OS Linux
- Conexion a Internet (Clonar el repositorio)
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
4. Instalación de la Aplicacion o Demo.

-- Proceso de Instalacion de la Aplicacion 

a. Validar que se tenga instalado y actualizado del paquete pip.
b. Validar que se tenga instalado el paquete VENV
c. Clonar el repositorio
	$ git clone https://github.com/andreszucod/demoquick.git
d. Ingresar a la carpeta clonada 'demoquick'. Debemos quedar a la altura de manage.py.
e. Crear el entorno virtual
f. Activar el entorno virtual.
g. Instalar las dependencias o los requerimientos.
	$ pip install -r ../requirements/local.txt
h. Ejecutar el proyecto
	$ python manage.py runserver
i. En caso de requerirse aplicar las migraciones
	$ python manage.py makemigrations
	$ python manage.py migrate
j. Ejecutar el proyecto
	$ python manage.py runserver

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
5. Requerimeintos implementados.
x--------------------------------------------------------------------------------------------------------------------
xxxxxxx Solucion de Requerimientos xxxxxxx

A. Requerimiento: Implementar CRUD de cada entidad.
-- Respuesta: Se implementa el CRUD mediante Api Rest_Framework para cada una de las entidades. Se implementa listar todos los objetos, crear un objeto, detalle de objeto por id(pk), Borrado de objeto por id(pk), modificar (editar) de objeto por id(pk). 
NOTA: Al eliminar la proyeccion de url JWT se puede ingresar directamente a los crud desde rest framework
Se puede ingresar a los CRUD mediante las siguientes url
a. Para Clientes:
- http://127.0.0.1:8000/api/clients/list/ (Protegida con JWT)
- http://127.0.0.1:8000/api/clients/create/
- http://127.0.0.1:8000/api/clients/detail/<pk>/   (pk es el id del objeto o registro)
- http://127.0.0.1:8000/api/clients/delete/<pk>/
- http://127.0.0.1:8000/api/clients/modify/<pk>/

b. Para Productos:
- http://127.0.0.1:8000/api/products/list/  (Protegida con JWT)
- http://127.0.0.1:8000/api/products/create/
- http://127.0.0.1:8000/api/products/detail/<pk>/   (pk es el id del objeto o registro)
- http://127.0.0.1:8000/api/products/delete/<pk>/
- http://127.0.0.1:8000/api/products/modify/<pk>/

c. Para Facturas:
- http://127.0.0.1:8000/api/bills/list/  (Protegida con JWT)
- http://127.0.0.1:8000/api/bills/create/
- http://127.0.0.1:8000/api/bills/detail/<pk>/   (pk es el id del objeto o registro)
- http://127.0.0.1:8000/api/bills/delete/<pk>/
- http://127.0.0.1:8000/api/bills/modify/<pk>/

x----------------------------------------- ---------------------------------------------------------------------------
B. Requerimiento: Un endpoint que permita registrar a un usuario con correo electrónico y contraseña.
Respuesta: Se implementa el registro de nuevos usuarios.
a. Ingresar al sistema (http://127.0.0.1:8000/)
b. Hacer click en "1. Registro en el sistema"
c. Ingresar Correo Electronico y password (confirmado y validado)
d. Hacer click en Registrar. El sistema lo redireccionara al endpoint de "Ingrespo al sistema".

x--------------------------------------------------------------------------------------------------------------------
C. Requerimiento: Un endpoint que permita iniciar sesión con el correo electrónico y contraseña previamente creados, generando un JSON Web Token (Ver punto E para el JWT).
-- Respuesta: 
a. Una vez registrado en el sistema. ingresar a la pagina de "Ingreso Usuario" (Login)
b. Ingresar la credenciales regustradas e "Ingresar"
c. El sistema lo direccionara a la "Pagina de llegada". Alli se incluiran funcionalidades. (http://127.0.0.1:8000/menu1/)
d. Si se intenta llegar a la "Pagina de llegada", el sistema le solicitara el "Ingreso al Sistema" o Login.
e. Para hacer logout se hace click en "Salir"

x--------------------------------------------------------------------------------------------------------------------
D. Requerimiento: Que los endpoints de entidades estén asegurados por un JSON Web Token recibido desde la cabecera de la petición.
-- Respuesta: Se protegen los end point mediante JWT. Las url creadas son:
a. Para Clientes:
- http://127.0.0.1:8000/api/clients/list/

b. Para Productos:
- http://127.0.0.1:8000/api/products/list/

c. Para Facturas:
- http://127.0.0.1:8000/api/bills/list/

x--------------------------------------------------------------------------------------------------------------------
E. Registro e ingreso a la API mediante JWT
Requerimiento: (Editado) Acceder a la API con las credenciales, generando un JSON Web Token.
-- Respuesta: Usando "POSTMAN"
a. Crear una nueva conexion de tipo "POST" a la URL "http://127.0.0.1:8000/api/token/"
b. Seleccionar la Opcion "Body" t tipo de texto "JSON"
c. En el cuadro de texto ingresar.
{
    "email": "quick1@gmail.com",
    "password": "demo1prop#"
}
d. Enviar la solicitud y obtener los token "refresh", "access"
e. Ahora, crear una conexion tipo "GET" a la URL  "http://127.0.0.1:8000/api/clients/list/"
f. Seleccionar la opcion "Headers"
g. En la opcion "KEY" escribir "Authorization" y en la opcion "VALUE" ingresar sin comillas "Bearer Token-access" y "Send".


x--------------------------------------------------------------------------------------------------------------------
F. Requerimiento: Un endpoint que permita realizar la descarga de un archivo CSV con la lista de registros de Cliente: mostrando documento, nombre completo y la cantidad facturas relacionadas.
-- Respuesta: Pendiente

x--------------------------------------------------------------------------------------------------------------------
G. Requerimiento: Un endpoint que permita realizar el cargue de un archivo CSV con resgitros para la creacion de Clientes.
-- Respuesta: No se Implemento

x--------------------------------------------------------------------------------------------------------------------
H. Requerimiento: Usar el ORM de Django para las consultas de Productos y para el resto usar SQL plano en lo posible
-- Respuesta: Se implementa consulta con salida json serializada desde la interface del sistema.
a. Ingresar al sistema mediante en boton "Ingreso al siatema" (http://127.0.0.1:8000/)
b. Ingresar las credenciales pertinentes
c. Seleccionar el link "Consulta ORM Products - URL/Json". Se desplegara un Json con la consulta de los productos de la base.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
6. Bugs conocidos y posibles correcciones de errores.
A. No se implementa el cargue de archivo CSV

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
7. Preguntas frecuentes.
No Aplica

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
8. Derechos de autor y licencias.
Libre uso
