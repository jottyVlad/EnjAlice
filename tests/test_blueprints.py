import pytest

from enjalice.routers import Blueprint, Dispatcher
from enjalice.response import AliceResponse, text
from enjalice.request import AliceRequest, State


@pytest.fixture
def bps() -> Blueprint:
    bp1 = Blueprint()

    @bp1.message_handler(priority=0, intent=['TEST.INTENT.ASYNC'])
    async def test_1(_):
        return text("Test handler 1")

    bp2 = Blueprint()

    @bp2.message_handler(priority=1, intent=['TEST.INTENT.SYNC'])
    def test_2(_):
        return text("Test handler 2")

    return bp1, bp2


@pytest.fixture
def dp(bps) -> Dispatcher:
    d = Dispatcher(lambda _: AliceResponse())
    d += bps[0] + bps[1]
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
    state = State(session=session)
    async for resp in call_handlers(dp, state=state):
        assert resp.session_state['test'] == 42
        assert resp.session_state is not session
