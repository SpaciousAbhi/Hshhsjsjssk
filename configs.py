from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "4770590"))
    API_HASH = getenv("API_HASH", "e33bf9032335b874acb9c6406f044836")
    BOT_TOKEN = getenv("BOT_TOKEN", "6926248838:AAEz3ikX6UK7rAW91zhqg_2O-aapbBZaLyQ")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1002643460174"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://kajaki7757:kGDRiPGNX691vlCL@cluster0.ylww9nv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
