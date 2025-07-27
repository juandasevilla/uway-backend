# UWay Backend - Django API

## Dockerización

Este proyecto Django ha sido dockerizado para facilitar el desarrollo y despliegue.

### Requisitos previos

- Docker
- Docker Compose

### Configuración y ejecución

#### 1. Construir y ejecutar con Docker Compose

```bash
# Construir las imágenes y ejecutar los contenedores
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d --build
```

#### 2. Comandos útiles

```bash
# Ver logs
docker-compose logs

# Ver logs solo del servicio web
docker-compose logs web

# Parar los contenedores
docker-compose down

# Parar y eliminar volúmenes
docker-compose down -v

# Ejecutar comandos dentro del contenedor
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py shell
```

#### 3. Estructura de servicios

- **web**: Aplicación Django corriendo en el puerto 8000
- **db**: Base de datos PostgreSQL en el puerto 5432

#### 4. Variables de entorno

El proyecto utiliza las siguientes variables de entorno:

- `DEBUG`: Modo debug (1 para activado, 0 para desactivado)
- `USE_POSTGRES`: Usar PostgreSQL en lugar de SQLite (1 para activado)
- `POSTGRES_DB`: Nombre de la base de datos
- `POSTGRES_USER`: Usuario de PostgreSQL
- `POSTGRES_PASSWORD`: Contraseña de PostgreSQL
- `DB_HOST`: Host de la base de datos
- `DB_PORT`: Puerto de la base de datos

#### 5. Acceso a la aplicación

Una vez ejecutado, la aplicación estará disponible en:
- API: http://localhost:8000
- Admin: http://localhost:8000/admin (después de crear un superusuario)

#### 6. Desarrollo local

Para desarrollo local, puedes seguir usando SQLite ejecutando el proyecto sin Docker:

```bash
python manage.py runserver
```

El proyecto detectará automáticamente si debe usar PostgreSQL (con Docker) o SQLite (desarrollo local).

### Notas

- Los archivos estáticos se recolectan automáticamente al iniciar el contenedor
- Las migraciones se ejecutan automáticamente al iniciar el contenedor
- Los volúmenes de Docker mantienen los datos persistentes entre reinicios
