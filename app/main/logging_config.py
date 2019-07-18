''' Logging info, debug with coloredlogs '''
import logging.config

import coloredlogs

coloredlogs.install()

CONFIG = {
    "version": 1,
    'disable_existing_loggers': False,
    "formatters": {
        "standard": {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        }
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
            'filename': 'debug.log',
        }
    },
    'loggers': {
        'debugLogger': {
            'level': 'DEBUG',
            'handlers': ['debugHandler']
        },
        'infoLogger': {
            'level': 'INFO',
            'handlers': ['infoHandler']
        },
    }
}

logging.config.dictConfig(CONFIG)

logging.getLogger()
