###################################
#   My Hello World in FastAPI     #
###################################

from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def great():
    return f"Hello?World?"

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("hello:app", reload=True)