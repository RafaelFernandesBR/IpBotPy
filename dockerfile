FROM python:3.11-slim-buster

# Copia os arquivos da aplicação para o contêiner
COPY . /app

# Define o diretório de trabalho do contêiner
WORKDIR /app

# Instala as dependências da aplicação
RUN pip install -r requirements.txt
ENV tokem=xxxxxxx

# Define o comando que será executado quando o contêiner for iniciado
CMD ["python", "main.py"]
