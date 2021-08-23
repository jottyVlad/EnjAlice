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
Коллекция элементов `IntentHandler`. Имеет следующие методы:

`add(obj: IntentHandler)` - добавление нового элемента в
коллекцию

`discard(obj: IntentHandler)` - удаляет элемент obj из
коллекции.

Также имеет переопределенные методы `__iter__` для цикла
`for..in`, `__len__` для метода `len()`, `__contains__` для
использования `in`.