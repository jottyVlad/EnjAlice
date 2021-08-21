import pytest

from enjalice import Dispatcher
from enjalice import request
from enjalice.response import AliceResponse, text
from enjalice.request import AliceRequest, Request, State, Nlu


@pytest.fixture
def dp() -> Dispatcher:
    d = Dispatcher()

    @d.message_handler(priority=0, intent=['TEST.INTENT.ASYNC'])
    async def test_1(_):
        return text("Test handler 1")

    @d.message_handler(priority=1, intent=['TEST.INTENT.SYNC'])
    def test_2(_):
        return text("Test handler 2")

    return d


async def call_handlers(d: Dispatcher, **kwargs):
    for i in ['TEST.INTENT.ASYNC', 'TEST.INTENT.SYNC']:
        req = AliceRequest(
            request=dict(
                nlu=dict(
                    intents={i: {}}
                )
            ),
            **kwargs
        )
        yield await d.dispatch_request(req)


@pytest.mark.asyncio
async def test_sync_async(dp: Dispatcher):
    async for resp in call_handlers(dp):
        assert isinstance(resp, AliceResponse)
        assert resp.response.text != ''


@pytest.mark.asyncio
async def test_session_state(dp: Dispatcher):
    session = {'test': 42}
    state = State(session={'test': 42})
    async for resp in call_handlers(dp, state=state):
        assert resp.session_state['test'] == 42
        assert resp.session_state is not session
