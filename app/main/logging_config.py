import logging

import daiquiri
import daiquiri.formatter

daiquiri.setup(outputs=(
    daiquiri.output.STDOUT,
    daiquiri.output.Stream(formatter=daiquiri.formatter.ColorFormatter(
        fmt="%(asctime)s, %(msecs)d Level: %(levelname)-8s in file %(filename)s at line %(lineno)d"
        ))
))
