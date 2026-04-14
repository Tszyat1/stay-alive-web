import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# 从项目根目录的 .env 文件读取环境变量
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

DATABASE_URL = os.getenv("DATABASE_URL")

# engine 是数据库连接的核心对象，整个应用共用一个
engine = create_engine(DATABASE_URL)

# SessionLocal 是一个"会话工厂"，每次处理请求时用它创建一个新 session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 是所有 Model 类的父类，后续 models.py 里会用到
class Base(DeclarativeBase):
    pass


def get_db():
    """
    FastAPI 的依赖注入函数。
    每次 API 请求进来时，自动创建一个数据库 session，请求结束后自动关闭。
    用法：在路由函数参数里写 db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
