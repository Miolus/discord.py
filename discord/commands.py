from typing import Coroutine, TYPE_CHECKING
from discord.types.snowflake import Snowflake


class ApplicationCommand():

    if TYPE_CHECKING:
        id: Snowflake
        application_id: Snowflake
        name: str
        description: str
        callback: Coroutine


    def __init__(self, id: Snowflake, application_id: Snowflake, name: str, description: str, callback: Coroutine=None):
        self.id = id
        self.application_id = application_id
        self.name = name
        self.description = description
        self.callback = callback