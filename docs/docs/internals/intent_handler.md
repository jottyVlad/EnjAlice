# Intents
В этом разделе будет рассказано про сущности `IntentHandler`
и `IntentHandlerCollection`.

## IntentHandler
Тип данных, используемый в `Dispatcher`.

Это **pydantic** модель, состоящая из 3х полей.

- `name: Optional[str]` - название интента (как в Диалогах)
- `priority: int` - приоритет исполнения хендлера
- `handler: Callable` - ссылка на функцию (асинхронную или
синхронную), которая будет исполняться, если сработал интент.
Принимает на вход объект AliceRequest, 
возвращает AliceResponse.

Именно экземпляр класса `IntentHandler` создается, когда вы
используете метод `register_message_handler` или декоратор
`message_handler` в `Dispatcher`.

## IntentHandlerCollection
MutableSet - множество элементов `IntentHandler`. 
Порядок итерации по элементам идет от самого высокого
приоритета к самому низкому.
Имеет следующие методы:

`add(obj: IntentHandler)` - добавление нового элемента в
коллекцию

`discard(obj: IntentHandler)` - удаляет элемент obj из
коллекции.