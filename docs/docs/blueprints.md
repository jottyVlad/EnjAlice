# Blueprint

Основа основ обертки.

В неё входит обработка запросов, регистрация хендлеров. Необходим для модульного программирования навыков.

## Пример использования.

В одном файле можно описать блупринт:

```python
from enjalice.routers import Blueprint
from enjalice.request import AliceRequest
from enjalice.response import text

bp = Blueprint()


@bp.message_handler(15, ['YANDEX.HELP'])
async def help_handler(_: AliceRequest):
    return text("Это сообщение помощи")
```

А в другом написать реализацию диспетчера, зарегистрировав блупринт.

```python
from blueprint import bp
from enjalice.routers import Dispatcher
from enjalice.request import AliceRequest
from enjalice.response import text

async def start_handler(_: AliceRequest):
    return text(
        msg="Это пример работы с blueprints"
    )


dp = Dispatcher(start_handler)

dp.register_blueprint(bp)
```

Так же блупринты можно складывать друг с другом:

`bp = bp1 + bp2`

Регистрация хендлеров совпадает с `Dispatcher`. Начальное сообщение не требуется.