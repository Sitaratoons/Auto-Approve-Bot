from os import environ

API_ID = int(environ.get("API_ID", "18946488"))
API_HASH = environ.get("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", ""))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002471954376"))
ADMINS = int(environ.get("ADMINS", "6692613520"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://Renamest:Renamest@cluster0.prfhc.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "Ajay")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
