from fastapi import FastAPI
from routes import chat 

app = FastAPI()                          # Create our main FastAPI kitchen

@app.get("/")                            # Root route - like our restaurant's front door
async def root():
    return {"message": "Welcome to our AI Kitchen!"}

app.include_router(chat.router)          # Connect the chat routes to our main app 
