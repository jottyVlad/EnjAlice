from aiohttp import web

from enjalice.attachments.button import ImageButton, ResponseButton
from enjalice.attachments.cards import BigImage
from enjalice.routers import Dispatcher
from enjalice.request import AliceRequest
from enjalice.response import text
from example.aiohttp_server import app


async def start_handler(_: AliceRequest):
    return text(
        msg="Это пример работы с карточками"
    )


dp = Dispatcher(start_handler)


@dp.message_handler(priority=100)
def handle_fallback(_: AliceRequest):
    res = text(msg="Это основной текст")
    res.response.card = BigImage(
        image_id="213044/9bebbb719d12e0c952e4",
        button=ImageButton(
            text="Текст кнопки",
            url="https://google.com",
            payload={
                "key1": "value1"
            }
        )
    )

    res.response.buttons.append(ResponseButton(
        title="Кнопка1",
        url="https://github.com",
        payload={
            "key1": "value1"
        },
        hide=True
    ))
    return res


if __name__ == '__main__':
    app['dp'] = dp
    web.run_app(app, host="127.0.0.1", port=8888)
