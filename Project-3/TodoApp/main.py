from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# This is similar to django routers, the endpoints of the main app will now also have the endpoints of the auth app
app.include_router(auth.router)
app.include_router(todos.router)
