from enjalice import Dispatcher, Bot, AliceRequest
from enjalice.response import text


async def start_handler(_: AliceRequest):
    return text(
        msg="Привет, я тестовый навык для разработки оболочки над моим API enj-alice"
    )


dp = Dispatcher(start_handler)
bot = Bot(dp=dp)

bot.webhook_host = "127.0.0.1"
bot.webhook_port = 8888
bot.webhook_path = "/alice"


@dp.message_handler(priority=100)
def handle_fallback(_: AliceRequest):
    return text(msg="Сработал фоллбек!")


if __name__ == '__main__':
    bot.run()
