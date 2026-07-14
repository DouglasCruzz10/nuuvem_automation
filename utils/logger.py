import logging
import os
from datetime import datetime

"""
Configuração do logger para registrar informações, avisos e erros durante a execução do programa.
O logger cria uma pasta "logs" (se não existir) e gera arquivos de log com timestamp no nome, 
armazenando mensagens de log em diferentes níveis (INFO, WARNING, ERROR, DEBUG, CRITICAL).
"""

# Criação da pasta para armazenar os logs
if not os.path.exists("logs"):
    os.makedirs("logs")
log_filename = f"logs/log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

# Funções de log
def info_log(msg):
    logging.info(msg)

def warning(msg):
    logging.warning(msg)

def error(msg, exc: Exception = None):
    if exc:
        logging.exception(msg)
    else:
        logging.error(msg)
def debug(msg):
    logging.debug(msg)

def critical(msg, exc: Exception = None):
    if exc:
        logging.critical(msg, exc_info=True)
    else:
        logging.critical(msg)