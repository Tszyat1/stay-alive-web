from pydantic import BaseModel
from datetime import datetime

# 1. 用户注册时前端发来的数据


class UserCreate(BaseModel):
    username: str   # 用户名
    password: str   # 明文密码（后端收到后会 hash，不会存原文）

# 2. 返回给前端的用户信息（注意：没有密码字段）


class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True  # 让 Pydantic 能直接从 SQLAlchemy model 对象读取数据

# 3. 打卡时前端发来的数据


class CheckInCreate(BaseModel):
    pass


class CheckInResponse(BaseModel):
    id: int
    user_id: int
    checked_at: datetime
    streak_count: int

    class Config:
        from_attributes = True
