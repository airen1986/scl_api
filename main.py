from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.staticfiles import StaticFiles

from app.api.router import api_router

app = FastAPI()

# Include API routes first so they take precedence over the catch-all
app.include_router(api_router)

# Serve static files from the root path
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Fallback for SPA routes: any unmatched GET returns index.html
@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
	return FileResponse("static/index.html")
