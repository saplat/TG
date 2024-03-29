from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    os.getenv('admin0'),
    os.getenv('admin1')
]

ip = os.getenv("ip")

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')


POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"