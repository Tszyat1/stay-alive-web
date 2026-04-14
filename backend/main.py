from fastapi import FastAPI
from database import engine

app = FastAPI(title="又活了一天 API")


@app.get("/health")
def health_check():
    """
    健康检查接口。
    用途：确认后端服务正常运行，数据库连接没有问题。
    """
    try:
        # 尝试连接数据库，如果失败会抛出异常
        with engine.connect():
            db_status = "connected"
    except Exception:
        db_status = "disconnected"

    return {"status": "ok", "database": db_status}
