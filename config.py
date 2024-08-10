import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "26602863"))
API_HASH = getenv("API_HASH", "44a687eb7cac4df75d9332a65eece369")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7032716003:AAFciDiTLx9iPFSCbVjVDpmG-oX0eIPZlE0")

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "shizuka_song_bot")

# Don't Add style font 
BOT_USERNAME2 = getenv("BOT_USERNAME2" , "miss Broken")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sung:sung@cluster0.eruyz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "1002056908015"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5787354656"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

    # Don't edit variables below this line #
SUDO_USERS = [6566179661, 6415940074, 1886390680]

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Badhacker98/BADMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "bad")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/astheticdpsforu")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ANG_COMMUNITY_7")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BAD_STRING_SESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQGV7W8Ap-q3BQV3o-ppxqTGy6v6HOjPmdY7mlKtjdc_QBcmikkVs1XdviR3JDD2v_gwoYjM0EHpAcCW7kGCS4GZIkoh_PEg44A6w51xs2LuwbyPEtkxiTPMnIOejFp1X96enrIoG5AOKKaTa6IhwNDNLQgZ2MhiA6gbowo1eMnCKEWSrqKcFbEmEzph74s3XbuaRf43INtu9q0U3o3Ip0JTFJI3EDpBjaud3Bu9AKfRAXK70bDBOm5ZgZGsjCVPhGjlzuSwelIqNkXrAoxZYiFfyL3Qur0IlXueV0mA4cKJ9XPplL8wF33RmGzMSPBl6TBoOkF8aGdNCScEAoR51xbr2PG2UwAAAAG93uJyAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


   
# ██████╗░██████╗░░█████╗░██╗░░██╗███████╗███╗░░██╗
# ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░██║
# ██████╦╝██████╔╝██║░░██║█████═╝░█████╗░░██╔██╗██║
# ██╔══██╗██╔══██╗██║░░██║██╔═██╗░██╔══╝░░██║╚████║
# ██████╦╝██║░░██║╚█████╔╝██║░╚██╗███████╗██║░╚███║
# ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝
# 
#      ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░
#      ████╗░████║██║░░░██║██╔════╝██║██╔══██╗
#      ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝
#      ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗
#      ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝
#      ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░




BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://mallucampaign.in/images/img_1723124681.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/559e9b45fe937d650b834.mp4"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/cbb216bd1e84c83bce233.jpg"
STATS_IMG_URL = "https://telegra.ph/file/51badb4aba8d2b7534604.mp4"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/bd3be91cf02a8e4373894.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/7435ac7c4251779d59c71.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d3d80cd8cc0a6363eb21d.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/37ffadfde57a375a786db.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/37ffadfde57a375a786db.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/59d7eaec62d37a98d71ec.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/3c550e5585607aeb25e1b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d3d80cd8cc0a6363eb21d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
