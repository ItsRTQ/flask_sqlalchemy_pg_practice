# Flask SQLAlchemy Setup Guide(Whats going on)

## Instrucciones Paso a Paso

### Crear la Aplicación Flask

Inicializa tu aplicación Flask.

### Crear una Instancia de SQLAlchemy

- Importa `SQLAlchemy` desde `flask_sqlalchemy`.
- Crea una instancia de `SQLAlchemy`.

### Configurar la URI de la Base de Datos

Configura la aplicación Flask con la URI de la base de datos utilizando `app.config['SQLALCHEMY_DATABASE_URI']`.

### Configurar Otros Ajustes de SQLAlchemy (Opcional)

Establece `app.config['SQLALCHEMY_TRACK_MODIFICATIONS']` en `False` para desactivar el seguimiento de modificaciones.

### Iniciar la Conexión con Flask

Inicializa la instancia de SQLAlchemy con la aplicación Flask utilizando `db.init_app(app)`.

### Crear Tablas con `app_context`

Usa `app.app_context()` para crear las tablas definidas por tus modelos con `db.create_all()`.

### Definir un Modelo

- Define una clase que represente una tabla en la base de datos.
- Esta clase debe heredar de `db.Model`.
- Define las columnas y sus propiedades en la clase.

### Añadir un Método de Guardado al Modelo

Añade un método a la clase del modelo para guardar una instancia en la base de datos utilizando `db.session.add(self)` y `db.session.commit()`.

### Crear un Objeto y Guardarlo

Usa `app.app_context()` para crear una instancia del modelo y llama al método de guardado para almacenarla en la base de datos.

## Ejemplo de Instrucciones

### Crear la Aplicación Flask

Crea una instancia de aplicación Flask llamada `app`.

### Crear una Instancia de SQLAlchemy

- Importa `SQLAlchemy` desde `flask_sqlalchemy`.
- Crea una instancia de `SQLAlchemy` y llámala `db`.

### Configurar la URI de la Base de Datos

Establece `app.config['SQLALCHEMY_DATABASE_URI']` en la URI de tu base de datos (por ejemplo, `'sqlite:///example.db'`).

### Configurar Otros Ajustes de SQLAlchemy (Opcional)

Establece `app.config['SQLALCHEMY_TRACK_MODIFICATIONS']` en `False`.

### Iniciar la Conexión con Flask

Llama a `db.init_app(app)` para inicializar la instancia de SQLAlchemy con la aplicación Flask.

### Crear Tablas con `app_context`

Usa `app.app_context()` para crear las tablas con `db.create_all()`.

### Definir un Modelo

Define una clase `User` que herede de `db.Model`.

- Añade columnas: `id`, `username`, `email`, `password_hash`.

### Añadir un Método de Guardado al Modelo

Define un método `save` en la clase `User` que añada la instancia a la sesión y la confirme.

### Crear un Objeto y Guardarlo

Usa `app.app_context()` para crear una instancia de `User` y llama a su método `save` para almacenarla en la base de datos.
