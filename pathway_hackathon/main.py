import uvicorn
from fastapi import FastAPI
from src.api.router import router
from src.utils.config import Config

app = FastAPI(title="Research Paper Evaluation System")
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    Config.validate()
    uvicorn.run(app, host="0.0.0.0", port=8000)


