from fastapi import APIRouter, Request    # Import tools: APIRouter for creating route groups, Request for handling incoming data

router = APIRouter(prefix="/api")         # Create a router with /api prefix

@router.get("/")                         # Test route at /api
async def root():
    return {"message": "API is working"}

@router.get("/chat")                      # This will be at /api/chat
async def read_chat():                    # async function that runs when someone visits /chat
    return {"message": "Chat endpoint ready"}  # Send back a simple message

@router.post("/chat")                     # This will be at /api/chat
async def handle_chat(request: Request):   # async function that runs when someone sends data to /chat
    return {"message": "Message received"} # Send back a simple response



