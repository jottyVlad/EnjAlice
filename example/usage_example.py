from aiohttp import web
from enjalice.routers import Dispatcher
from enjalice.request import AliceRequest
from enjalice.response import text

from aiohttp_server import app


async def start_handler(_: AliceRequest):
    return text(
        msg="Привет, я тестовый навык для разработки оболочки над моим API enj-alice"
    )


dp = Dispatcher(start_handler)


@dp.message_handler(priority=1000, intent=["YANDEX.HELP"])
async def handle_help(_: AliceRequest):
    return text(
        msg="У меня пока что нет команд, но они обязательно будут!",
        tts="Этот текст говорит, что у меня пока что нет команд!"
    )


if __name__ == '__main__':
    app['dp'] = dp
    web.run_app(app)
