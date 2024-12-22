import logging
import colorlog
from django.db.backends.signals import connection_created
from django.dispatch import receiver

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
))

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.propagate = False  # Не передавать сообщение родительским логгерам

@receiver(connection_created)
def log_db_connection(sender, connection, **kwargs):
    logger.info(f'Successful DB connection established: {connection.alias}')