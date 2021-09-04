from . import context
from ._hints import MessageHandlerFunction
from .blueprints.blueprint import Blueprint
from .exceptions import NoHandler
from .intent_handler import IntentHandlersCollection
from .internals.route import ABCRoute
from .request import AliceRequest
from .response import AliceResponse


class Dispatcher(ABCRoute):
    def __init__(self, start_handler: MessageHandlerFunction):
        self.intents: IntentHandlersCollection = \
            IntentHandlersCollection()
        self.start_dialog_handler = start_handler

    async def dispatch_request(self, request_obj: AliceRequest) -> AliceResponse:
        context.session_state.set(request_obj.state.session)

        response = None

        if request_obj.session.new:
            # When user starts a new conversation
            response = await self._get_response(self.start_dialog_handler, request_obj)
        else:
            for intent_handler in self.intents.iter_intents(request_obj.request.nlu.intents):
                response = await self._get_response(intent_handler.handler,
                                                    request_obj)
                if response is not None:
                    break

        if response is None:
            raise NoHandler(f"Can't handle request: {request_obj}")

        return response

    def register_blueprint(self, blueprint: Blueprint):
        for intent in blueprint.intents:
            self.intents.add(intent)
