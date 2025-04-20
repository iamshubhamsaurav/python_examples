from typing import Any

class MidAPI:
    def __init__(self):
        pass

    def __call__(self, environ, start_response) -> Any:
        print(environ)
        start_response("200 OK", headers=[])
        return [b"Hello, World"]
    
midapi = MidAPI()