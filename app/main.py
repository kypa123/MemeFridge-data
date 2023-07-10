import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from app.routers import router


app = FastAPI()
app.include_router(router.mainRouter)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)