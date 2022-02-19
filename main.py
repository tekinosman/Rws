from typing import Optional

from fastapi import BackgroundTasks, FastAPI, Response

from fastapi.responses import FileResponse, HTMLResponse

from fastapi.staticfiles import StaticFiles

from helpers import html_gen

from async_lru import alru_cache


app = FastAPI()
cache_size = 1024**2 # 1 MB


# Homepage
@app.get("/")
#uncomment to enable caching# @alru_cache(maxsize = cache_size)
async def home():
	content = await html_gen.homepage()
	return HTMLResponse(content)												


# Clears homepage's cache (temporary)
@app.post("/clear")
def clear():
	home.cache_clear()


# Static files
app.mount("/static", StaticFiles(directory = "static"), name = "static")