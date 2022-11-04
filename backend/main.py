from fastapi import FastAPI
from v1.api.user_api import user_router
from core.database.base import Base
from core.database.base import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user_router.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
