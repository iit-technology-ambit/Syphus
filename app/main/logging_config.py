''' Logging info, debug with coloredlogs '''
import logging.config

import coloredlogs

coloredlogs.install()

CONFIG = {
    "version": 1,
    'disable_existing_loggers': False,
    "formatters": {
        "standard": '%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s in file %(filename)s at line number %(lineno)d',
    },
    "handlers": {
        "infoHandler": {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'debugHandler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'fileName': 'debug.log',
        },
        'loggers': {
            'debugLogger': {
                'level': 'DEBUG',
                'handlers': 'debugHandler',
            },
            'infoLogger': {
                'level': 'INFO',
                'handlers': 'infoHandler',
            },
        }
    }
}

logging.config.dictConfig(CONFIG)

logging.getLogger()
