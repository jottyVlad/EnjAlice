from aiohttp import web
from enjalice.dispatcher import Dispatcher
from enjalice.request import AliceRequest
from enjalice.consts import Sounds
from enjalice.response import text

from aiohttp_server import app


async def start_handler(_: AliceRequest):
    return text(
        msg="Привет, я тестовый навык для разработки оболочки над моим API enj-alice"
    )


dp = Dispatcher(start_handler)


@dp.message_handler(priority=150, intent=["tell_fortunes"])
async def handler_tell_fortunes_sound(_: AliceRequest):
    return text(
        msg="Сейчас погадаю",
        tts=Sounds.Bell1 + "Гадание для Вас - Вы сегодня хороший"
    )


if __name__ == '__main__':
    app['dp'] = dp
    web.run_app(app)
