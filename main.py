from fastapi import FastAPI
from routes.routes import router as youtube_router
from dotenv import load_dotenv

load_dotenv()  # This will load environment variables from a .env file
app = FastAPI()

# Include the YouTube processing router
app.include_router(youtube_router, prefix="/youtube", tags=["youtube"])

# Additional configurations or routes can be added here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
