FROM python:3.9

WORKDIR /app

# Kopírování requirements.txt do pracovního adresáře
COPY requirements.txt .

# Instalace závislostí
RUN pip install --no-cache-dir -r requirements.txt

# Kopírování zdrojových souborů
COPY . .

# Exponování portu (FastAPI běží na portu 8000)
EXPOSE 8000

# Spuštění FastAPI aplikace pomocí uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
