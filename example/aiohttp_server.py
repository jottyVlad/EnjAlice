from aiohttp import web
from enjalice.request import AliceRequest


async def handle(request: web.Request):
    data = await request.json()
    response = await request.app['dp'].dispatch_request(
        AliceRequest.parse_obj(data)
    )
    return web.json_response(response.dict())


app = web.Application()
app.router.add_post('/alice-webhook-path', handle)
