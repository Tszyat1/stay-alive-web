from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
import models
import schemas
from passlib.context import CryptContext

app = FastAPI(title="又活了一天 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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


@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 检查用户名是否已存在
    existing_user = db.query(models.User).filter(
        models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="用户名已存在")

    # 创建新用户
    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(username=user.username,
                           hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
