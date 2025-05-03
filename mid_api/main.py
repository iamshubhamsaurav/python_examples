from typing import Any

# Internal Imports
from mid_api.methods import Methods
from response import Response

class MidAPI:
    def __init__(self):
        # routes will store all the route as key
        # the value will be a dictionary
        # the key will be method and value will be handler
        self.routes = {}

    def __call__(self, environ, start_response) -> Any:
        response = Response()
        for path, handlers_dict in self.routes.items():
            for request_method, handler in handlers_dict.items():
                if environ['REQUEST_METHOD'] == request_method and path == environ['PATH']:
                    handler(environ, response)
                    response.as_wsgi(start_response)
                    return [response.text.encode()]
    
    def route_handler(self, path, handler, method):
        path_name = path or f"{handler.__name__}"

        if path_name not in self.routes:
            self.routes[path_name] = {}
            
        self.routes[path_name][method] = handler
        return handler

    
    def post(self, path=None):
        def wrapper(handler):
            return self.route_handler(path=path, handler=handler, method=Methods.POST.value)
        
        return wrapper
    
    def patch(self, path=None):
        def wrapper(handler):
            return self.route_handler(path=path, handler=handler, method=Methods.PATCH.value)
        
        return wrapper
    
    def put(self, path=None):
        def wrapper(handler):
            return self.route_handler(path=path, handler=handler, method=Methods.PUT.value)
        
        return wrapper
    
    def delete(self, path=None):
        def wrapper(handler):
            return self.route_handler(path=path, handler=handler, method=Methods.DELETE.value)
        
        return wrapper