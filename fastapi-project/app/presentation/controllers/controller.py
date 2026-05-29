from presentation.schemas.requests import request
#from app.application.interfaces import interface

class HelloController:

    def __init__(self):
        pass
        
    def download(self):
        r = request.TestRequest()
        r.validate()
    
    def controller_method(self, name: str):
        return {"message": f"Controller method called for {name}"}

        