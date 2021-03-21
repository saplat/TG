from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

admins = [
    os.getenv('admin0'),
    os.getenv('admin1')
]

ip = os.getenv("ip")
