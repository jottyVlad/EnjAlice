import json
from typing import Optional

from aiohttp import web

from .dispatcher import Dispatcher
from .request import AliceRequest
from .response import AliceResponse


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