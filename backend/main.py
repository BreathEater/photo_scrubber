from fastapi import FastAPI
from api.router_api import api_router
from api.router_frontend import frontend_router

app = FastAPI()

app.include_router(api_router, prefix="/api")
app.include_router(frontend_router)

