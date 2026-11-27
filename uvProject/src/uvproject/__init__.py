from fastapi import FastAPI
import uvicorn

def main() -> None:
    print("Hello from uvproject!")
    uvicorn.run(app , host="0.0.0.0" , port=8000)


app = FastAPI()

app.get("/")
async def root():
    return {"message" : "Goodbye World!!!"}