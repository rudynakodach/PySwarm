import requests

class Webhook:
    def __init__(self, url, type: str = "embed" or "message"):
        self.url = url
        self.embeds = []
        self.Title = None
        self.username = None
        self.Author = None
        self.type = type

    def addField(self, embed: list[dict], name: str = None, value: str = None, inline: bool = False):
        if self.type == "message":
            raise ValueError("Cannot add embed fields in a message.")
        field = {"name": name, "value": value, "inline": inline}
        self.fields.append(field)
        
    def _build(self) -> dict:
        data = {}
        if self.username is not None:
            data["username"] = self.username

    def addEmbed(self):
        self.embeds.append({})

    def post(self):
        requests.post(url=self.url, headers={"Content-Type": "application/json"}, data=self._build())
