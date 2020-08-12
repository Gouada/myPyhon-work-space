
import logging
import logging.handlers
import logging.config
import inspect


class MyLogger():
    logFile = "C:\\MyWorkspace\\python_workspace\\myFrameWork\\server.log"

    def customConfigLogger(self):
        # logging.basicConfig('loggerConf.conf')
        logging.config.fileConfig('loggerConf.conf')
        logger = logging.getLogger()

        return logger

    def customLogger(self, logLevel):
        sourcename = inspect.stack()[1][3]
        #logger = logging.getLogger(sourcename)
        logger = logging.getLogger(sourcename)
        logger.setLevel(logging.DEBUG)

        rotatingFH = logging.handlers.RotatingFileHandler(self.logFile, "a", 3000, 5, None, False)
        formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s %(message)s', datefmt='%Y.%m.%d %H:%M:%S')
        rotatingFH.setFormatter(formatter)
        rotatingFH.setLevel(logLevel)

        logger.addHandler(rotatingFH)

        return logger
