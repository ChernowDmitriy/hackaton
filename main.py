import asyncio

from fastapi import FastAPI

from api import router as api_router
from infrastructure.database import BaseModel, engine

app = FastAPI()
app.include_router(api_router)


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def main():
    await create_table()

asyncio.run(main())
