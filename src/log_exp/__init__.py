import logging

# for simple trace-level logging (below logging.DEBUG)
# use e.g.
# logger.log(LOGGING_TRACE, "%d words are matching", n)
LOGGING_TRACE = 5
logging.addLevelName(LOGGING_TRACE, "TRACE")
