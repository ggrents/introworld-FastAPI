from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

view_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@view_router.get("/")
async def get_introworld_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@view_router.get("/register")
async def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@view_router.get("/login")
async def get_register(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
