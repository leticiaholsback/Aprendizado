# import logging

# # logging.basicConfig(filename='app.log')
# # log= logging.getLogger()
# # log.info('Leticia')
# # log.level


# #OLHAR COMENTARIO, USO DE NIVEL DE LOGGER
# #logging.basicConfig(filename='app.log', level=logging.DEBUG)
# log= logging.getLogger()
# log.info('Leticia')
# log.critical('Leticia')
# log.error('Leticia')
# log.warning('Leticia')


# #logging.basicConfig(filename='app.log', level=logging.DEBUG, filemode='w')
# #se executar com filemode='w', ele apaga valores anteriores e só salva o atual
# log.level


import logging
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=LOG_FORMAT)
log= logging.getLogger()
log.info('testando com informacoes de logs')
