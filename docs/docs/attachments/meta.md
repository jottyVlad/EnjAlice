# Meta
Тут информация о дополнительных классах для `Card`.

### Header

- `text: str` - текст заголовка. Максимум 64 символа.

Заголовок списка изображений. 
Используется в `ItemsList`.

### Footer

- `text: str` - текст первой кнопки. Максимум 64 символа.
- `button: Optional[ImageButton]` - дополнительная 
кнопка для списка изображений. `ImageButton` находится в 
`enjalice.attachments.button`.