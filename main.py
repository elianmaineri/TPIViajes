from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.UserDestinos import destinos_router


app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(destinos_router)


Base.metadata.create_all(bind=engine)