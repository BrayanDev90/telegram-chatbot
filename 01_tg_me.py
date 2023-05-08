import telegram

from constants import TG_API_KEY

# Prendo il gestore del bot
tbot = telegram.Bot(token=TG_API_KEY)
print(tbot.get_me())
