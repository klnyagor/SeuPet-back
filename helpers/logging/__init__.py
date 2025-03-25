import logging
from logging.handlers import RotatingFileHandler

# Filtro personalizado para capturar somente um nível específico de log
class LogLevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

# Cria o logger com um nome único
logger = logging.getLogger('example_logger')
logger.setLevel(logging.INFO)

# Formatação padrão para os logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Handler para console (todas as mensagens)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Handler para mensagens INFO (rotaciona o arquivo)
info_handler = RotatingFileHandler('info.log', maxBytes=10000, backupCount=3)
info_handler.setFormatter(formatter)
info_handler.addFilter(LogLevelFilter(logging.INFO))
logger.addHandler(info_handler)

# Handler para mensagens WARNING (rotaciona o arquivo)
warning_handler = RotatingFileHandler('warning.log', maxBytes=10000, backupCount=3)
warning_handler.setFormatter(formatter)
warning_handler.addFilter(LogLevelFilter(logging.WARNING))
logger.addHandler(warning_handler)

# Handler para mensagens ERROR (rotaciona o arquivo)
error_handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=3)
error_handler.setFormatter(formatter)
error_handler.addFilter(LogLevelFilter(logging.ERROR))
logger.addHandler(error_handler)
