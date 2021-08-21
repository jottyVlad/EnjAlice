from enjalice import Dispatcher, Bot, AliceRequest
from enjalice.consts import Sounds
from enjalice.response import text


dp = Dispatcher()
bot = Bot(dp=dp)

bot.webhook_host = "127.0.0.1"
bot.webhook_port = 8888
bot.webhook_path = "/alice"

dp.start_text = \
    "Привет, я тестовый навык для разработки оболочки над моим API enj-alice"


@dp.message_handler(priority=150, intent=["tell_fortunes"])
async def handler_tell_fortunes_sound(_: AliceRequest):
    return text(
        msg="Сейчас погадаю",
        tts=Sounds.Bell1 + "Гадание для Вас - Вы сегодня хороший"
    )


if __name__ == '__main__':
    bot.run()
