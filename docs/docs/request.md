# Классы запроса

Основной класс запроса - `AliceRequest`.

## AliceRequest

- ```
  request: Union[
    SimpleUtterance, ButtonPressed,
    PurchaseConfirmation, ShowPull
  ]
  ```
  основные поля запроса. На данный момент поддерживаются запросы типа
  `SimpleUtterance`, `ButtonPressed`, `Purchase.Confirmation`
  и `Show.Pull`. Подробнее смотрите в документации Яндекса:
  [тут](https://yandex.ru/dev/dialogs/alice/doc/request.html#request__request-desc)
- `meta: Meta` - мета-информация о запросе.
- `session: Session` - информация о сессии запроса.
- `state: State` - состояния (State). Можно 
использовать только если включена соответствующая 
функция в Диалогах.

## Meta

- `locale: str` - язык в POSIX-формате.
- `timezone: str` - название часового пояса, включая алиасы.
- `client_id: str` - не рекомендуется к использованию. Интерфейсы, доступные на клиентском устройстве, перечислены в
  свойстве `interfaces`. Идентификатор устройства и приложения, в котором идет разговор.
- `interfaces: Interfaces` - интерфейсы, доступные на устройстве пользователя.

## Session

- `session_id: str` - уникальный идентификатор сессии.
- `message_id: Optional[int]` - идентификатор сообщения 
в рамках сессии. Инкрементируется с каждым 
следующим запросом.
- `skill_id: str` - идентификатор вызываемого навыка, 
присвоенный при создании.
- `user_id: str` - свойство перестает поддерживаться — 
вместо него следует использовать новое, полностью 
аналогичное свойство `session.application.application_id`.
Идентификатор экземпляра приложения, в котором 
пользователь общается с Алисой. Даже если 
пользователь авторизован с одним и тем же 
аккаунтом в приложении Яндекс для Android и iOS, 
Яндекс.Диалоги присвоят отдельный `user_id` 
каждому из этих приложений.
- `user: User` - атрибуты пользователя Яндекса, 
который взаимодействует с навыком. 
Если пользователь не авторизован в приложении, 
свойства user в запросе не будет.
- `application: Application` - данные о приложении, 
с помощью которого пользователь взаимодействует с навыком.
- `new: bool` - признак новой сессии. Возможные значения:
`True` — пользователь начинает новый разговор с навыком;
`False` — запрос отправлен в рамках уже начатого разговора.

## State

- `session: Dict` - состояние навыка в контексте сессии.
- `user: Dict` - состояние навыка в контексте 
авторизованного пользователя.
- `application: Dict` - Состояние навыка в контексте 
экземпляра приложения пользователя.

## Nlu

- `tokens: List[str]` - массив слов из произнесенной 
пользователем фразы.
- `entities: List[Entity]` - массив именованных сущностей.
- `intents: Dict[str, Dict]` - объект с данными, 
извлеченными из пользовательского запроса.

## Interfaces

- `screen: Dict` - пользователь может 
видеть ответ навыка на экране и открывать ссылки в браузере.
- `account_linking: Dict` - у пользователя есть 
возможность запросить связку аккаунтов.
- `payments: Dict` - поверхность, на которой 
пользователь взаимодействует с навыком, поддерживает 
возможность оплаты.
- `audio_player: Dict` - на устройстве пользователя 
есть аудиоплеер.

## Application

- `application_id: str` - идентификатор экземпляра 
приложения, в котором пользователь общается с Алисой.
Например, даже если пользователь авторизован с 
одним и тем же аккаунтом в приложениях Яндекс 
для Android и iOS, Яндекс.Диалоги присвоят отдельный 
`application_id` каждому из этих приложений.
Этот идентификатор уникален для пары 
«приложение — навык»: в разных навыках значение 
свойства `application_id` для одного и того же 
пользователя будет различаться.

## User

- `user_id: str` - идентификатор пользователя Яндекса,
  единый для всех приложений и устройств.
  Этот идентификатор уникален для пары
  «пользователь — навык»: в разных навыках значение свойства `user_id` для одного и того же пользователя будет
  различаться.
- `access_token: str` - Токен для OAuth-авторизации, который также передается в заголовке `Authorization`
  для навыков с настроенной связкой аккаунтов. Это JSON-свойство можно использовать, например, при реализации навыка в
  Yandex Cloud Functions
  (Диалоги вызывают функции с параметром
  `integration=raw`, который не позволяет получать заголовки клиентского запроса).

## EntityToken

- `start: int` - номер первого слова именованной сущности.
- `end: int` - номер первого слова после именованной сущности.

## Entity

- `tokens: EntityToken` - экземпляр `EntityToken`.
- `type: str` - тип именованной сущности.
- `value: Union[int, Dict]` - формальное описание именованной сущности.