import inspect
import logging

class LoggenClass:

    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)

        logfile = logging.FileHandler("D:\\E Drive Data\\CREDENCE\\9. YUSUF SIR - Automation Testing\\0. PRACTICAL\\PRACTICALS\\NOP_Commerse\\logs\\nop_logs.log")
        log_format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")

        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)

        return logger

