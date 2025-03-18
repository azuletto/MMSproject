FROM python:3.10

# Instalar Chrome e ChromeDriver
RUN apt-get update && apt-get install -y wget unzip curl
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

# Criar diretório da aplicação
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar código e rodar o servidor
COPY . .
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
