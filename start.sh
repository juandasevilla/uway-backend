#!/bin/bash

# Script de inicio para el proyecto Django con Docker

echo "🚀 Iniciando UWay Backend con Docker..."

# Verificar si Docker está corriendo
if ! docker info > /dev/null 2>&1; then
    echo "❌ Error: Docker no está corriendo. Por favor, inicia Docker primero."
    exit 1
fi

# Construir y ejecutar los contenedores
echo "📦 Construyendo y ejecutando contenedores..."
docker-compose up --build -d

# Esperar a que la base de datos esté lista
echo "⏳ Esperando a que la base de datos esté lista..."
sleep 10

# Ejecutar migraciones
echo "🔄 Ejecutando migraciones..."
docker-compose exec web python manage.py migrate

# Recolectar archivos estáticos
echo "📁 Recolectando archivos estáticos..."
docker-compose exec web python manage.py collectstatic --noinput

echo "✅ ¡Proyecto iniciado correctamente!"
echo "🌐 La aplicación está disponible en: http://localhost:8000"
echo "🛠️  Para crear un superusuario, ejecuta: docker-compose exec web python manage.py createsuperuser"
echo "📝 Para ver los logs, ejecuta: docker-compose logs -f"
echo "🛑 Para parar el proyecto, ejecuta: docker-compose down"
