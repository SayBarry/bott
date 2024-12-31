from os import path, getenv

class Config:
    API_ID = int(getenv('API_ID','22092598'))
    API_HASH = getenv('API_HASH','93de73c78293c85fd6feddb92f91b81a')
    BOT_TOKEN = getenv('BOT_TOKEN','7393252205:AAG55M3Zv9cOnTVoHS3a3FDlMOzxVVAqPf4')

config = Config()
