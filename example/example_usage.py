from enjalice import Dispatcher, Bot, AliceRequest
from enjalice.consts import Sounds
from enjalice.response import text


dp = Dispatcher()
bot = Bot(dp=dp)

bot.webhook_host = "127.0.0.1"
bot.webhook_port = 8888
bot.webhook_path = "/alice"


@dp.start_handler()
async def start_handler(_: AliceRequest):
    return text(
        msg="Привет, я тестовый навык для разработки оболочки над моим API enj-alice"
    )


@dp.message_handler(priority=1000, intent=["YANDEX.HELP"])
async def handle_help(request: AliceRequest):
    return text(
        msg="У меня пока что нет команд, но они обязательно будут!",
        tts="Этот текст говорит, что у меня пока что нет команд!"
    )


if __name__ == '__main__':
    bot.run()
