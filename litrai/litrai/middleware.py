import logging
from django.db.backends.signals import connection_created
from django.dispatch import receiver

logger = logging.getLogger(__name__)

@receiver(connection_created)
def log_db_connection(sender, connection, **kwargs):
    logger.info(f'Successful DB connection established: {connection.alias}')