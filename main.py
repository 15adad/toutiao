from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import news, users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # 允许访问后端的"源"（前端地址），必须是精确的 协议://主机:端口
    # 三个分别是：Vite 默认端口、Vite 的 127.0.0.1 写法、CRA/Next 常用端口
    allow_origins=[
        # "http://localhost:5173",      # Vite 前端（localhost）
        # "http://127.0.0.1:5173",      # Vite 前端（127.0.0.1，和上面是不同源）
        "http://localhost:3000",      # 其他前端工具默认端口
    ],

    # 是否允许前端携带 Cookie / Authorization 等凭证
    # 开了这个，allow_origins 就不能用 ["*"]，必须写具体地址
    allow_credentials=True,

    # 允许的 HTTP 方法，["*"] = 全部（GET/POST/PUT/PATCH/DELETE/OPTIONS...）
    allow_methods=["*"],

    # 允许前端请求里携带的请求头，["*"] = 全部
    # 比如 Content-Type、Authorization、自定义头都靠它放行
    allow_headers=["*"],
)
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