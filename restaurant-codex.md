## Project as a Story
A short paragraph that frames your project in metaphor — like:

"Welcome to our digital restaurant. The kitchen (backend) is where the magic happens — orders come in, meals get prepped, the mind / the llm through openai  API is our master chef . The dining room (frontend) is where users enjoy their experience."

## Story Log

FastAPI is our ghost system that lets functions easily pass through walls (different files) in our kitchen. Instead of manually walking through doors between files (like routes/chat.py, services/ai_chef.py), our ghosts (@app.get(), @app.post()) can instantly move orders and data wherever they need to go. All ghosts share one system (app = FastAPI()), so they know exactly where everything is in our kitchen.

When an order (request) comes in, the right ghost picks it up, takes it where it needs to go, and brings back what's needed - all automatically because they're part of the FastAPI network. 