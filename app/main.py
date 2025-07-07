from fastapi import FastAPI
from app.api.routes import router as api_router
from app.db.base import Base, engine

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(api_router)
