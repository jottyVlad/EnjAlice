from bot import Dispatcher, Bot, AliceRequest, AliceResponse

dp = Dispatcher()
bot = Bot(dp=dp)

bot.set_webhook_host("127.0.0.1")
bot.set_webhook_port(8888)
bot.set_webhook_path("/alice")

dp.set_start_text("Привет, я тестовый навык для разработки оболочки над моим API enj-alice")


@dp.message_handler(priority=1000, intent="YANDEX.HELP")
async def handle_help(request: AliceRequest,
                      response: AliceResponse):
    # Here we can process data in request
    # Then fill data in response
    response.response.text = "У меня пока что нет команд, но они обязательно будут!"
    # And return AliceResponse object
    return response

bot.run()
