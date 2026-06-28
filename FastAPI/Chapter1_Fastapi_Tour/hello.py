###################################
#   My Hello World in FastAPI     #
###################################

from fastapi import FastAPI, Header

app = FastAPI() 

@app.post("/hi") # Decorator
def great(who:str = Header()): 
    return f"Hello? {who}?"

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("hello:app", reload=True)