import re, os, time
import datetime

class Config:
    id_pattern = re.compile(r'^.\d+$') 
   
    BOT_TOKEN = "1173368697:AAEOETJROlE0PGE5HXK_UZKZCy_WSPaXYvo"

    API_ID = 2532603

    API_HASH = "f565b00bbe3ad9c6748e39a3a71d16e7"

    CLIENT_ID = "961047305075-221ebtjv4e7gbhjbivo4f57dq1v1dgdc.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = 754495556

    DB_NAME = "utubeitbot"    

    DB_URL = "mongodb+srv://user:user@cluster0.x3e1p.mongodb.net"

    SUPPORT_CHAT_LINK = "https://t.me/hxsupport"

    SESSION_NAME = ":memory:"

    BOT_START_TIME = time.time()
    
    BOT_START_DATETIME = datetime.datetime.now().strftime("%B %d, %Y %I:%M:%S %p")

    BOT_UPTIME  = time.time()

    DOWNLOAD_DIRECTORY = "./downloads/"

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")
    
    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
    
# Id 961047305075-j6s6ii7h44f2n68kprn1qim4fki5nrhu.apps.googleusercontent.com
# Secret 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
