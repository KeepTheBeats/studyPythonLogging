import logging
import func1
import func2

logFile = "logfile.log"
FORMAT = '%(asctime)s, %(levelname)s, %(filename)s:%(lineno)d, %(funcName)s(), %(message)s'
logging.basicConfig(filename=logFile,
                    filemode='a',
                    format=FORMAT,
                    level=logging.INFO)

if __name__ == "__main__":
    logging.info("This is in main.py.")
    func1.function1()
    func2.function2()

    try:
        func1.raiseException()
    except Exception as e:
        logging.exception(e)
        logging.error("Exception: {}".format(e))
