# Images
Используются только в `ItemsList` и `ImageGallery`.

### ImageWithButton

- `image_id: str` - идентификатор изображения,
который возвращается в ответ на запрос загрузки.
- `title: Optional[str]` - заголовок изображения.
- `description: Optional[str]` - описание изображения.
- `button: Optional[ImageButton]` - cвойства изображения,
на которое можно нажать. `ImageButton` находится в 
`enjalice.attachments.button`.

Используется в `ItemsList`.

### ImageWithoutButton
- `image_id: str` - идентификатор изображения, 
который возвращается в ответ на запрос загрузки.
- `title: Optional[str]` - Заголовок для изображения. 
Максимум 128 символов.

Используется в `ImageGallery`.