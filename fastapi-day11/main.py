from fastapi import FastAPI
from routers import files

app = FastAPI(title="Day 11 - File Uploads and Background Tasks")

app.include_router(files.router)   # ✅ FIXED HERE

@app.get("/")
def home():
    return {"message": "Day 11 Working"}
