#trabalhando o log
import logging

LOG_FORMAT = "%(levelname)s, %(asctime)s, %(message)s"
logging.basicConfig(filename="app.log", level=logging.DEBUG, filemode="w", format=LOG_FORMAT)

log = logging.getLogger()

log.info("Ola")
log.critical("Erro Grave")
log.error("Ola")
log.debug("Erro Grave")
log.warning("Erro Gravissimo")
log.level