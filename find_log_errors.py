import re
import logging


class MyExceptionError(Exception):
    def __init__(self, message):
        self.message = message
    pass


with open('data/gupdate.log') as file:
    logfile = file.readlines()
file.close()


def find_log_error(log):
    logging.basicConfig(filename='data/found_error.log', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    logger.addHandler(console)

    regex = re.compile('.*error.*', re.IGNORECASE)
    regex_critical = re.compile('.*critical.*', re.IGNORECASE)

    logging.info("Starting code")
    try:

        counter = 0

        for logline in log:
            try:
                if re.search(regex, logline):
                    counter += 1
                    if re.search(regex_critical, logline):
                        logger.warning(logline)
                        raise MyExceptionError('CRITICAL ERROR')
                    else:
                        logging.error(logline)

            except MyExceptionError:
                print('Watch Out!')

        logging.info("Finishing code")

        log_len = len(logfile)

        return log_len / counter

    except ZeroDivisionError:
        print('There is no errors in log file')



print(find_log_error(logfile))


