from aiohttp import web

from blueprints import bps, bp as full_bp  # noqa
from enjalice.dispatcher import Dispatcher
from enjalice.request import AliceRequest
from enjalice.response import text
from example.aiohttp_server import app


async def start_handler(_: AliceRequest):
    return text(
        msg="Это пример работы с blueprints"
    )


dp = Dispatcher(start_handler)

for bp in bps:
    dp.register_blueprint(bp)

# Or
# dp.register_blueprint(full_bp)

if __name__ == '__main__':
    app['dp'] = dp
    web.run_app(app, host="127.0.0.1", port=8888)
