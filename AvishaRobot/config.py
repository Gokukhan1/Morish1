
class Config(object):
    LOGGER = True

    #####

    ANILIST_CLIENT = "8679"
  
    ANILIST_SECRET = "NeCEq9A1hVnjsjZlTZyNvqK11krQ4HtSliaM7rTN"
  
    API_ID = 22731333
   
    API_HASH = "f8f993acb1d5f51c950ba873404d9af5"
   
    TOKEN = "8154928303:AAHOdHIV_PAMiXzLRhmILYPrw7RSw3cdQi8"
  
    OWNER_ID = "5458968679"

    OWNER_USERNAME = "@i_am_morish"
    
    SUPPORT_CHAT = "PiratesMainchat"
   
    START_IMG = "https://files.catbox.moe/scntdi.jpg"

    JOIN_LOGGER = "-1002052732769"
   
    EVENT_LOGS = "-1002052732769"
  
    ERROR_LOGS = "-1002295880117"

    MONGO_DB_URI= "mongodb+srv://Gojo_tu:Gojo2347@gojo.eii7p.mongodb.net/?retryWrites=true&w=majority&appName=Gojo"
   
    LOG_CHANNEL = "-1002286294709"
   
    BOT_USERNAME = "NoelleSilva_robot"
   
    DATABASE_URL = "postgres://oocekooc:W2w0GdYOHNwvqKh047VMGjhHq_Xlb2sS@hansken.db.elephantsql.com/oocekooc"

    CASH_API_KEY = "V48U2FLLKRHSVD4X"
    
    TIME_API_KEY = "1CUBX1HXGNHW"

    SPAMWATCH_API = "3624487efd8e4ca9c949f1ab99654ad1e4de854f41a14afd00f3ca82d808dc8c"
    
    SPAMWATCH_SUPPORT_CHAT = "+pexefpzqVXBjNzY1"
    
    WALL_API = "2455acab48f3a935a8e703e54e26d121"
    
    REM_BG_API_KEY = "xYCR1ZyK3ZsofjH7Y6hPcyzC"
    
    OPENWEATHERMAP_ID = "887da2c60d9f13fe78b0f9d0c5cbaade"

    BAN_STICKER = "CAACAgEAAxkBAAIrTWYljyX_lqcubkAzg0jy45CRvxAFAAKvAgACrLHoRU50VVvh3xWwNAQ"

    HEROKU_APP_NAME = None

    HEROKU_API_KEY = None

    LASTFM_API_KEY = "8f3315b5806c21004b2822f07825187d"
    
    # Optional fields
    
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [5458968679]  # User id of sudo users
    DEV_USERS = [7078181502]  # User id of dev users
    DEMONS = [7363537003]  # User id of support users
    TIGERS = [7078181502]  # User id of tiger users
    WOLVES = [7078181502]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

  
