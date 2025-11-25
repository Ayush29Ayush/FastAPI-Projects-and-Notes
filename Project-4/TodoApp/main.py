from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users
import starlette

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/health", status_code=starlette.status.HTTP_200_OK)
async def health():
    return {"status": "ok"}

# This is similar to django routers, the endpoints of the main app will now also have the endpoints of the auth app
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)