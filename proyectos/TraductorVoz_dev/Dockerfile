# Usamos una imagen oficial de Python ligera
FROM python:3.10-slim

# Instalamos dependencias del sistema necesarias para audio y compilación
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero el archivo de dependencias y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de nuestro código (main.py, index.html) al contenedor
COPY . .

# Exponemos el puerto 7860 (Hugging Face Spaces requiere y expone por defecto este puerto)
EXPOSE 7860

# Comando para arrancar el servidor FastAPI con Uvicorn en el puerto 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]