# Changelog

Ведение истории изменений ведется с версии 2.2.0

## 2.2.0

- Теперь в модели `Meta` поле `interfaces`
  использует специальную модель `Interfaces`.
- Переписан `IntentHandlerCollection` (алгоритм теперь работает за O(1)).
- Добавлена возможность использовать различные типы
  `request` (на данный момент доступны `SimpleUtterance`,
  `ButtonPressed`, `Purchase.Confirmation`).
- Добавлена поддержка директив
  (`DirectiveStartPurchase`, `DirectiveConfirmPurchase`).
- `IntentHandler` теперь dataclass, а не pydantic модель.
- Добавлена поддержка поля `analytics` (модель `Analytics`).
- Теперь в tts можно добавлять свои аудио (метод
  `AliceResponse.add_custom_audio(skill_id, sound_id)`)
- Добавлена поддержка `application_state` и
  `user_state_update`.
- Для tokens в классе `Entity` создана отдельная модель -
  `EntityToken`.
- Добавлена поддержка добавления пауз и эффектов произношения в tts(методы
  `AliceResponse.add_voice_effect(self, effect, text)` и
  `AliceResponse.add_pause(self, ms)`).

## 2.2.1

- Добавлена поддержка запроса с "Утренним шоу Алисы" (
  `ShowItemMeta` класс в `Response`, `Show.Pull` тип в `AliceRequest`).