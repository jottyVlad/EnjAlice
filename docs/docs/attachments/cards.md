# Card
Карточки могут 3х разных видов: `BigImage`, `ItemsList`, 
`ImageGallery`.

Все типы карточек находятся в `enjalice.attachments.cards`.

Карточку можно прикрепить к сообщению:

`res.response.card = card`

### BigImage

- `image_id: str` - идентификатор изображения,
который возвращается в ответ на запрос загрузки.
- `title: Optional[str]` - заголовок изображения.
- `description: Optional[str]` - описание изображения.
- `button: Optional[ImageButton]` - cвойства изображения,
на которое можно нажать. `ImageButton` находится в 
`enjalice.attachments.button`.

### ItemsList

- `header: Optional[Header]` - заголовок изображения.
`Header` можно найти в 
`enjalice.attachments.items_list_additions`.
- `items: List[ImageWithButton]` - набор изображений.
Не меньше 1 и не больше 5. `ImageWithButton`
можно найти в `enjalice.attachments.image`.
- `footer: Footer` - кнопки под списком изображений.
`Footer` можно найти в
`enjalice.attachments.items_list_additions`.

### ImageGallery

`items: List[ImageWithoutButton]` - набор изображений.
Не меньше 1 и не больше 7. `ImageWithoutButton`
можно найти в `enjalice.attachments.image`.