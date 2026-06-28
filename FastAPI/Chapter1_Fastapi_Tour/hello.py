###################################
#   My Hello World in FastAPI     #
###################################

from fastapi import FastAPI, Header
from fastapi import Response

app = FastAPI() 

@app.get("/agent") # Decorator
def get_agent(user_agent:str = Header()): 
    return user_agent

@app.get("/happy", status_code=200)
def happy():
    return ":)"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("hello:app", reload=True)