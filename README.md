# Backend test

Explicación de la solución:

He utilizado python + flask ya que es el lenguaje que utilizaría después y me quería enfrentar a ello aunque no haya hecho más que scripts sencillos y ejercicios tipo leetCode en este lenguaje. He optado por usar docker ya que así sería mucho más sencillo todo el set up del proyecto. 

Librerías utilizadas:
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
psycopg2-binary==2.9.9
marshmallow==3.22.0
marshmallow-sqlalchemy==1.1.0

SQLAlchemy, un ORM que facilita la interacción con la base de datos.
psycopg2-binary para utilizar postgres. 
mashmallow para validación y serialización.

Estructura y organización del código:
- /invoices -> aquí se guardarán los archivos subidos
- Dockerfile y docker-compose.yaml --> ficheros para la dockerización
- requirements.txt --> Librerías que hay que se instalan
- /src --> código del proyecto
  -  app.py --> archivo principal donde se lanza la aplicación
  -  config.py --> Fichero de configuración donde se define información de la base de datos y la ruta de subida de archivos
  -  /routes --> Aquí tenemos los Blueprints que contienen los endpoints
  -  /services --> Aquí tenemos toda la lógica de negocio necesaria. Conecta los endpoints con la base de datos
  -  /repositories --> Aquí encontramos las operaciones con la base de datos
  -  /models --> Modelos que representan las tablas de la base de datos
  -  /schema --> Utilizado para validar y serializar los datos

 Un ejemplo de flujo de la aplicación sería el siguiente.

Puedes hacer una petición POST, teniendo en cuenta la especificación del ejercicio y las validaciones que tenemos en nuestro Schema. Una vez se ha realizado correctamente, recibiremos una respuesta en formato json con la información de la invoice que hemos subido. El fichero se guardará en la carpeta /invoices con formato <uuid4>.<extensión>. Podemos utilizar la petición GET para recibir en la respuesta la información de todas las invoices. En esta respuesta encontraremos una URL para acceder al fichero correspondiente. Esta URL es otro endpoint (GET) que se ha añadido a la especificación de forma extra para acceder al fichero subido anteriormente.

 Se ha intentado estructurar el código de la forma más mantenible y escalable posible dentro de mis conocimientos.
