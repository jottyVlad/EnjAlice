# EnjAlice

EnjAlice - асинхронная обёртка над API Яндекс.Алисы, которая предоставляет возможность быстро запустить и удобно разрабатывать callback диалоги.

## Установка

```
pip install enjalice
```

## Hello, World на EnjAlice
Для того чтобы написать простейшее приложение на EnjAlice
с помощью aiohttp, нужно инициализировать приложение aiohttp,
написать простейший обработчик запроса, поступающий от Алисы
и передающий его обертке.
```python
from aiohttp import web
from enjalice.request import AliceRequest
from enjalice.routers import Dispatcher
from enjalice.response import text


async def handle(request: web.Request):
    data = await request.json()
    response = await request.app['dp'].dispatch_request(
        AliceRequest.parse_obj(data)
    )
    return web.json_response(response.dict())


app = web.Application()
app.router.add_post('/alice-webhook-path', handle)

async def start_handler(_: AliceRequest):
    return text(
        msg="Привет, я тестовый навык для разработки оболочки над моим API enj-alice"
    )


dp = Dispatcher(start_handler)


@dp.message_handler(priority=1000)
async def handle_help(_: AliceRequest):
    return text(msg="Hello, World!")


if __name__ == '__main__':
    app['dp'] = dp
    web.run_app(app)
```

Аналогично можно использовать FastAPI, BlackSheep или другие,
даже синхронные, фреймворки, потому что фреймворк поддерживает
как синхронные, так и асинхронные хендлеры.

## Copyright
Проект имеет лицензию MIT.

Copyright © Jotty
