import inspect
import logging
import datetime
import os.path as path

def customLogger(logLevel=logging.DEBUG):
    # Get the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logLevel)
    if not logger.handlers:
        filename = 'log\\automation_{}.log'.format(datetime.datetime.now().strftime("%Y%m%dT%H%M%S"))
        LOG_PATH = path.normpath(path.join(path.dirname(path.abspath(__file__)), '..', filename))

        fileHandler = logging.FileHandler(LOG_PATH, mode='a')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter("%(asctime)s.%(msecs)03d [%(levelname)-8s] [%(name)s]: %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

    return logger