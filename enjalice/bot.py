import json
from typing import Optional

from aiohttp import web

from .dispatcher import Dispatcher
from .request import AliceRequest


class Bot:
    def __init__(self, dp: Dispatcher):
        self.dispatcher: Dispatcher = dp
        self.webhook_host: str = ""
        self.webhook_port: Optional[int] = None
        self.webhook_path: str = ""

    def run(self):
        if not self.webhook_host:
            raise ValueError("You have to set webhook host first! "
                             "Use set_webhook_host method for it")
        app = web.Application()
        app.add_routes([web.post(
            self.webhook_path, self.handle
        )])
        web.run_app(app=app,
                    host=self.webhook_host,
                    port=self.webhook_port)

    async def handle(self, request: web.Request):
        data = await request.json()

        response = await self.dispatcher.dispatch_request(
            AliceRequest.parse_obj(data)
        )

        return web.json_response(response.dict())
