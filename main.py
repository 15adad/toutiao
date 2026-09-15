from fastapi import FastAPI

from routers import news, users

app = FastAPI()

# 挂载路由
app.include_router(news.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)