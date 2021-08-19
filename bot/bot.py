import json
from typing import Optional

from aiohttp import web

from bot.dispatcher import Dispatcher
from bot.request import AliceRequest
from bot.response import AliceResponse


class Bot:
    def __init__(self, dp: Dispatcher):
        self.dispatcher: Dispatcher = dp
        self._webhook_host: str = ""
        self._webhook_port: Optional[int] = None
        self._webhook_path: str = ""

    def set_webhook_host(self, host: str):
        self._webhook_host = host

    def set_webhook_port(self, port: int):
        self._webhook_port = port

    def set_webhook_path(self, path: str):
        self._webhook_path = path

    def run(self):
        if not self._webhook_host:
            raise ValueError("You have to set webhook host first! "
                             "Use set_webhook_host method for it")
        app = web.Application()
        app.add_routes([web.post(
            self._webhook_path, self.handle
        )])
        web.run_app(app=app,
                    host=self._webhook_host,
                    port=self._webhook_port)

    async def handle(self, request: web.Request):
        data = await request.json()
        request_obj = AliceRequest.parse_obj(data)

        if request_obj.session.new:
            response = AliceResponse()
            response.response.text = self.dispatcher.start_text
            response_json = json.loads(response.json())
            return web.json_response(response_json)

        for intent_handler in self.dispatcher.intents:
            if (intent_handler.name in list(request_obj.request.nlu.intents.keys()))\
                    or intent_handler.name is None:
                alice_response = AliceResponse()
                alice_response.session_state = request_obj.state.session
                response: AliceResponse = await intent_handler.handler(
                    request_obj,
                    alice_response
                )
                if response is None:
                    continue

                response_json = json.loads(response.json())

                return web.json_response(response_json)
