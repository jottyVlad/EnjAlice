from enjalice import Dispatcher, Bot, AliceRequest, AliceResponse

dp = Dispatcher()
bot = Bot(dp=dp)

bot.webhook_host = "127.0.0.1"
bot.webhook_port = 8888
bot.webhook_path = "/alice"

dp.start_text = "Привет, я тестовый навык для разработки оболочки над моим API enj-alice"


@dp.message_handler(priority=1000, intent=["YANDEX.HELP", "tell_fortunes"])
async def handle_help(request: AliceRequest,
                      response: AliceResponse):
    # Here we can process data in request
    # Then fill data in response
    response.response.text = "У меня пока что нет команд, но они обязательно будут!"
    response.response.tts = "Этот текст говорит, что у меня пока что нет команд!"
    # And return AliceResponse object
    return response


@dp.message_handler(priority=100)
async def handle_fallback(request: AliceRequest,
                          response: AliceResponse):
    response.response.text = "Сработал фоллбек!"
    # And return AliceResponse object
    return response

bot.run()
