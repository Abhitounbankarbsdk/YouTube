# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : inline-tube-mate [ Telegram ]
# Repo     : https://github.com/m4mallu/inine-tube-mate
# Author   : Renjith Mangal [ https://t.me/space4renjith ]
# Credits  : https://github.com/SpEcHiDe/AnyDLBot


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1918613455:AAGQMLlRNpcbAmUwV7Jl1uc0ImVAg0oyNm4")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "7868296"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "bfa7fecb33443243ff8c8b0f27f9cd68")

    # Authorized user ids to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1932100298").split())

    # Super users to broadcast messages & fetch subscribers count
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1932100298").split())

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://fccyvrmwdktmui:0b4d157bc6dd91d7e5dd3eb7033af8523aeb6b25178c8290f75cd70761baa32f@ec2-18-235-45-217.compute-1.amazonaws.com:5432/d8g87aoktqs0o0")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "182.74.243.47:3128")

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
