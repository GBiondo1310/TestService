from fastapi import FastAPI

server = FastAPI()


@server.get("/")
async def test_ok():
    return "OK"


@server.get("/test_service/")
async def test_service():
    return "OK"
