from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database cleaned.")
    await create_tables()
    print("Database is ready!")
    yield
    print("Shutdown")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

