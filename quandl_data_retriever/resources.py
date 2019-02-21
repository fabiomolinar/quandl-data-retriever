"""Resource classes"""
import abc
import urllib.parse
import re
import json

class Resource(abc.ABC):
    @abc.abstractmethod
    def get_url(self):
        pass

    @abc.abstractstaticmethod
    def save():
        pass

class ForgeOne(Resource):
    def __init__(self, key):
        self.API_KEY = key

    API_ENDPOINT = {
        "scheme": "https",
        "netloc": "forex.1forge.com",
        "path": "/1.0.3/"
    }
    
    def get_url(self, url):
        parsed = urllib.parse.urlparse(url)
        path = parsed.path
        if not re.search(self.API_ENDPOINT["path"], path):
            path = self.API_ENDPOINT["path"] + path
            path = re.sub(r'//', "/", path)
        query = parsed.query
        if not re.search(r'api_key=', query):
            if query != "" and query[-1] != "&":
                query += "&"
            query += "api_key=" + self.API_KEY
        unparsed = urllib.parse.urlunparse((
            self.API_ENDPOINT["scheme"],
            self.API_ENDPOINT["netloc"],
            path,
            "",
            query,
            ""
        ))
        return unparsed

    @staticmethod
    def save(data):
        pass

class Quandl(ForgeOne):
    API_ENDPOINT = {
        "scheme": "https",
        "netloc": "www.quandl.com",
        "path": "/api/v3/"
    }

    @staticmethod
    def save(data):
        data = re.search(r"<body[^{]*{(.*?)}.*\/body>", data.decode("utf-8").replace("\n",""))
        if data:
            try:
                data = json.loads("{" + data.group(1) + "}")
            except json.decoder.JSONDecodeError:
                # Sometimes the API return the JSON without a } at the end
                data = json.loads("{" + data.group(1) + "}}")
            if len(data["dataset"]["data"]) == 0:
                return
            del data["dataset"]["description"]
            del data["dataset"]["newest_available_date"]
            del data["dataset"]["oldest_available_date"]
            del data["dataset"]["frequency"]
            del data["dataset"]["premium"]
            del data["dataset"]["limit"]
            return data