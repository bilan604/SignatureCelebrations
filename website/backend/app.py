from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Get the absolute path to the frontend directory
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/inflatables")
async def read_inflatables():
    return FileResponse(os.path.join(FRONTEND_DIR, "inflatables.html"))

@app.get("/stag-and-doe")
async def read_stag_and_doe():
    return FileResponse(os.path.join(FRONTEND_DIR, "stag-and-doe.html"))

@app.get("/tents-equipment")
async def read_tents_equipment():
    return FileResponse(os.path.join(FRONTEND_DIR, "tents-equipment.html"))

@app.get("/nerf-wars")
async def read_nerf_wars():
    return FileResponse(os.path.join(FRONTEND_DIR, "nerf-wars.html"))

@app.get("/snack-machines")
async def read_snack_machines():
    return FileResponse(os.path.join(FRONTEND_DIR, "snack-machines.html"))


app.mount("/", StaticFiles(directory="website/frontend", html=False), name="frontend")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
