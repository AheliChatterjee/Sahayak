from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Agentic Enterprise Assistant API",
    version="1.0.0"
)


# Request schema
class QueryRequest(BaseModel):
    query: str


# Health check endpoint
@app.get("/")
def health():
    return {"status": "API is running"}


# Chat endpoint
@app.post("/chat")
def chat(request: QueryRequest):
    try:
        from agent.agent_controller import handle_user_input
        response = handle_user_input(request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))