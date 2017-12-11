from opsdroid.matchers import match_crontab
from opsdroid.message import Message


@match_crontab("00 16 * * 5")
async def timewatch(opsdroid, config, message):
    connector = opsdroid.default_connector
    room = config.get("room", connector.default_room)
    message = Message("", None, room, connector)
    await message.respond("https://images.informaticslab.co.uk/misc/ac7891fdcb8fa6dd14fb5b0804eb71e2.png")
