from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from functionality import getGoogleHomepage
import os
import uvicorn


# Define request models
class URLRequest(BaseModel):
    url: str

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_google_homepage")
async def get_google_homepage_endpoint():
    try:
        # Call the scraping function with a different name
        projects = await getGoogleHomepage()  # Note: not async if using Selenium
        if projects is None:
            raise HTTPException(status_code=500, detail="Failed to fetch projects")
        return {"projects": projects}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)