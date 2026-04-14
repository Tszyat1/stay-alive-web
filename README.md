# 又活了一天 / Another Day Alive

> 一个面向真实经历情绪痛苦的人群的小打卡网站。
> 不是医疗产品，不是恶搞网站。只是想说：今天撑下来，也值得被看见。

---

## 技术栈

- 前端：React + Vite
- 后端：FastAPI + SQLAlchemy 2.0 + Alembic
- 数据库：PostgreSQL（Docker 运行）

---

## 本地启动步骤

### 1. 准备环境变量

```bash
cp .env.example .env
# 默认配置即可本地运行，无需修改
```

### 2. 启动数据库

```bash
docker compose up -d
# 验证：docker ps 能看到 stay_alive_db 容器
```

### 3. 启动后端

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
# 访问 http://localhost:8000/health
# Swagger UI: http://localhost:8000/docs
```

### 4. 运行数据库迁移

```bash
cd backend
alembic upgrade head
```

### 5. 启动前端

```bash
cd frontend
npm install
npm run dev
# 访问 http://localhost:5173
```

---

## 目录结构

```
stay-alive-web/
├── frontend/          # React + Vite 前端
├── backend/           # FastAPI 后端
├── docker-compose.yml # 只启动 PostgreSQL
├── .env.example       # 环境变量模板（不要把 .env 提交到 git）
└── README.md
```
