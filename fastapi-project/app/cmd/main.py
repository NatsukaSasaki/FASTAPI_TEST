from fastapi import FastAPI
from presentation.controllers.controller import HelloController


def main():
    import uvicorn
    #controller = di.get_controller()
    #controller.download()

    app = FastAPI()

    controller = HelloController()
    app.add_api_route("/test/{name}", controller.controller_method, methods=["GET"])

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
