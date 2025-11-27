from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse
import models
from database import engine
from routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import starlette

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def test(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)

@app.get("/health", status_code=starlette.status.HTTP_200_OK)
async def health():
    return {"status": "ok"}

# This is similar to django routers, the endpoints of the main app will now also have the endpoints of the auth app
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)