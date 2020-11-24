import logging


def set_logger():
    logging.basicConfig(filename='app.log',
                        filemode='w',
                        format='[%(levelname)s] - %(asctime)s - %(message)s',
                        level=logging.INFO)

    formatter = logging.Formatter('[%(levelname)s] - %(asctime)s - %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)

    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
