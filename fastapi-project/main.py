from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return{"message": "Hello from fastapi-project!"}


if __name__ == "__main__":
    main()
