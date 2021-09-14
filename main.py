import uvicorn
from fastapi import FastAPI
from app.routes import metric_route

app = FastAPI()

app.include_router(metric_route.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)