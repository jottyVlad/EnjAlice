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


@dp.message_handler(priority=100)
def handle_fallback(_: AliceRequest):
    return text(msg="Сработал фоллбек!")


if __name__ == '__main__':
    app['dp'] = dp
    web.run_app(app)
