import uvicorn
from fastapi import FastAPI


app = FastAPI(title="gs-backend-app",
              description="FastAPI Ground Station Backend",
              version="0.0.1")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("mian:app", port=9000, reload=True)
