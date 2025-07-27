@echo off
REM Script de inicio para el proyecto Django con Docker (Windows)

echo 🚀 Iniciando UWay Backend con Docker...

REM Verificar si Docker está corriendo
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Docker no está corriendo. Por favor, inicia Docker primero.
    pause
    exit /b 1
)

REM Construir y ejecutar los contenedores
echo 📦 Construyendo y ejecutando contenedores...
docker-compose up --build -d

REM Esperar a que la base de datos esté lista
echo ⏳ Esperando a que la base de datos esté lista...
timeout /t 10 /nobreak >nul

REM Ejecutar migraciones
echo 🔄 Ejecutando migraciones...
docker-compose exec web python manage.py migrate

REM Recolectar archivos estáticos
echo 📁 Recolectando archivos estáticos...
docker-compose exec web python manage.py collectstatic --noinput

echo ✅ ¡Proyecto iniciado correctamente!
echo 🌐 La aplicación está disponible en: http://localhost:8000
echo 🛠️  Para crear un superusuario, ejecuta: docker-compose exec web python manage.py createsuperuser
echo 📝 Para ver los logs, ejecuta: docker-compose logs -f
echo 🛑 Para parar el proyecto, ejecuta: docker-compose down
pause
