from enjalice import context
from enjalice.exceptions import NoHandler
from enjalice.intent_handler import IntentHandlersCollection
from enjalice.internals.route import ABCRoute
from enjalice.request import AliceRequest
from enjalice.response import AliceResponse


class Blueprint(ABCRoute):
    def __init__(self):
        self.intents: IntentHandlersCollection = \
            IntentHandlersCollection()

    async def dispatch_request(self, request_obj: AliceRequest) -> AliceResponse:
        context.session_state.set(request_obj.state.session)

        response = None

        for intent_handler in self.intents.iter_intents(request_obj.request.nlu.intents):
            response = await self._get_response(intent_handler.handler,
                                                request_obj)
            if response is not None:
                break

        if response is None:
            raise NoHandler(f"Can't handle request: {request_obj}")

        return response
