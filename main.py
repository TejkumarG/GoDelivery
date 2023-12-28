from fastapi import FastAPI

import packages_routers
import shipper_routers

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(packages_routers.router)
app.include_router(shipper_routers.router)
