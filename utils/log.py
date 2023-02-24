
from logging import config
import os

# ルートディレクトリにログ保存用のディレクトリを作成
if not os.path.exists('./log'):
    os.makedirs('./log')

# loggingの設定
LOGGING = {
    'version':1,
    'disable_existing_loggers': False,
    'formatters':{
        'simple':{
            'format': '%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s'
        }
    },
    'handlers':{
        'fileHandler':{
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': './log/game.log',
            'encoding': 'utf-8'
        }
    },
    'loggers':{
        'game':{
            'level': 'DEBUG',
            'handlers': [
                'fileHandler'
            ],
            'propagate': False
        }
    },
}

def configure_logging():
    """loggingに設定する"""
    config.dictConfig(LOGGING)