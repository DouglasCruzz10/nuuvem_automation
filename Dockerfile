# Xvfb - Servidor gráfico virtual que vai rodar na memória, sem precisar de uma tela física (headless=False)
FROM mcr.microsoft.com/playwright/python:v1.45.0-focal

# Criação do diretório de trabalho e cópia dos arquivos do projeto para dentro do container
WORKDIR /app
COPY . /app

# Instala o Xvfb 
RUN apt-get update && apt-get install -y xvfb && rm -rf /var/lib/apt/lists/*

# Instala dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Instala o Playwright e os navegadores necessários
RUN playwright install
# Define o comando padrão para iniciar o container, que executa o script main.py usando o Xvfb.
CMD xvfb-run -a python main.py
