from enjalice.blueprints.blueprint import Blueprint
from enjalice.request import AliceRequest
from enjalice.response import text

bp = Blueprint()


@bp.message_handler(10, ['tell_fortunes'])
async def help_handler(_: AliceRequest):
    return text("Это сообщение гадания")
