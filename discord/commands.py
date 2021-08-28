from .types.interactions import ApplicationCommandOption
from typing import Coroutine, List, TYPE_CHECKING
from .types.snowflake import Snowflake

class ApplicationCommandOption:
    
    def __init__(self, name, description, required,type="string", options=[], choices=[]):
        self.name = name
        self.description = description
        self.required = required
        self.type = type
        self.options = options
        self.choices = choices
    
    def to_dict(self):
        dict_options = []
        for option in self.options:
            dict_options.append(option.to_dict())
        dict_choices = []
        for choice in self.choices:
            dict_choices.append(choice.to_dict())
        return {"name":self.name, "description":self.description,"required":self.required,"type":self.type, "options":dict_options, "choices":dict_choices}

class ApplicationCommandOptionResponse:

    def __init__(self, name, value):
        self.name = name
        self.value = value

class ApplicationCommandCallback():

    def __init__(self, name: str, description: str, callback: str, options: List = [], guild_ids : List = []):
        self.name = name
        self.description = description
        self.callback = callback
        self.options = options
        self.guild_ids = guild_ids
        if len(self.guild_ids) == 0:
            self.is_global = True
        else:
            self.is_global = False
        print(self.guild_ids)
    
    def to_dict(self):
        data = {"name":self.name, "description":self.description, "type":1}
        options = []
        for option in self.options:
            options.append(option.to_dict())
        if len(options) > 0:
            data.update({"options":options})
        return data

class ApplicationCommand():

    if TYPE_CHECKING:
        id: Snowflake
        application_id: Snowflake
        name: str
        description: str
        callback: Coroutine


    def __init__(self, id: Snowflake, application_id: Snowflake, name: str, description: str, callback: ApplicationCommandCallback=None):
        self.id = id
        self.application_id = application_id
        self.name = name
        self.description = description
        self.callback = callback
