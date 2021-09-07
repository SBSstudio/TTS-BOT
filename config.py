# By @jack


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1997384120:AAG_7jxgLi_V1FvMof9msuo09hA2c9EAC6k")

    APP_ID = int(os.environ.get("APP_ID", 3283847))

    API_HASH = os.environ.get("API_HASH", "432c6eebf8df924b27be598c295c3692")
