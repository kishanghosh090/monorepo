from fastapi import FastAPI

# Initialize the FastAPI app instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI app!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query": query_param}
