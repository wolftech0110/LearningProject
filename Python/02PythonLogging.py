#!/bin/env python3
import logging
# create a basic logging file with the date , error level and message in the log file 
logging.basicConfig(level=logging.DEBUG,filename="log.log",filemode="w",
format="%(asctime)s - %(levelname)s - %(message)s")


# basic logging alterts
logging.debug("Test")
logging.info("info")
logging.warning("warning")
logging.error("Error")
logging.critical("Criticial")
#log a variable
x= 2
logging.debug(f"the value of x is {x}")

#log a stack trace
try:
    1/0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError", exc_info=True) 
    #or use logging.exception("ZeroDivisionError")


# Custom logger to og individual module
logger=logging.getLogger(__name__)
handler= logging.FileHandler("test.log")
formatter = logging.Formatter("%(asctime)s - %(name)s- %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Test")
print("Hello World Logging")