from fastapi import FastAPI
import uvicorn

from core.config import settings
from api_v1 import router as router_vps

app = FastAPI()
app.include_router(router=router_vps, prefix=settings.api_v1_prefix)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)