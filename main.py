from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Duke"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

@app.get("/sub/{num1}/{num2}")
def sub(num1: int, num2: int):
    """Do subtraction of two numbers"""

    total = num1 - num2
    return {"total": total}

@app.get("/mul/{num1}/{num2}")
def mul(num1: int, num2: int):
    """Multiply two numbers together"""

    total = num1 * num2
    return {"total": total}

@app.get("/div/{num1}/{num2}")
def div(num1: int, num2: int):
    """Do division between two numbers"""

    total = num1 / num2
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
