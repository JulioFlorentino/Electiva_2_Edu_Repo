# Imagen base
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la app
COPY app.py .

# Exponer el puerto 5000
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
