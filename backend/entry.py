import uvicorn
from app.main import app as fastapi_app


def main():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
