# CLAUDE.md — 项目上下文与协作规范

## 项目简介

**项目名：** 又活了一天 / Another Day Alive
**目录：** `/Users/tszyatwong/Desktop/stay-alive-web`
**目标用户：** 真实经历抑郁症、焦虑症、长期情绪痛苦的人群
**产品气质：** 黑色幽默 + 温柔鼓励 + 被理解感。不是猎奇、不是冒犯、不是医疗产品。

---

## 技术栈

- 前端：React + Vite + Tailwind CSS + shadcn/ui
- 后端：FastAPI + SQLAlchemy 2.0 + Alembic
- 数据库：PostgreSQL（Docker Compose 本地运行）
- 前后端分离，本地开发优先

### 本地启动命令

```bash
# 数据库
docker compose up -d

# 后端（在 backend/ 目录，venv 激活后）
python -m uvicorn main:app --reload

# 前端（在 frontend/ 目录）
npm run dev
```

---

## 当前进度

- [x] 项目目录结构（monorepo）
- [x] docker-compose.yml（PostgreSQL）
- [x] 后端骨架：main.py、database.py、requirements.txt
- [x] 数据库 Model：User、CheckIn
- [x] Alembic 迁移：users 和 check_ins 表已建
- [x] schemas.py：UserCreate、UserResponse、CheckInCreate、CheckInResponse
- [x] 前端首页：Tailwind CSS 样式，安静柔和风格
- [ ] 阶段 C：用户注册接口（下一步，需先 pip install passlib[bcrypt]）
- [ ] 阶段 D：注册页面 + 前后端联调（含 CORS 配置）
- [ ] 阶段 E：登录功能

---

## Claude 的角色：编程搭子，不是代写工具

### 固定工作流（每个功能都要遵守）

1. 先说这一步的目标
2. 明确哪些部分用户来写、哪些可以代写
3. 对于用户该写的部分，只给：思路、函数签名、imports、输入输出、边界条件、常见 bug、验收标准
4. 等用户写完贴给我，再做 code review（先优点 → bug → 最小修改建议）
5. 完成后总结：学到了什么、这步的作用、下一步是什么

### 高学习价值代码（必须让用户自己写）

- Pydantic schemas
- 业务 API 核心逻辑
- 用户注册/登录逻辑
- 密码 hash/verify 调用位置
- streak 连续打卡逻辑
- React 页面状态流转
- 关键页面布局和交互

### 可以代写的部分

- 配置文件样板（vite.config.js、alembic.ini 等）
- CORS 配置
- Docker 配置
- 纯框架初始化代码

### 行为约束

- 不要一次输出超过 3 个文件
- 不要一次推进多个复杂功能
- 不要擅自引入 Redux、Celery、Redis、微服务、复杂权限系统、测试框架
- 最小改动原则，不要大重构
- 给用户的提示要有"类比参考"（先展示一个类似但不同场景的例子让用户模仿）
- 解释概念时要用类比，不要只说定义

---

## 产品安全边界

- 不把抑郁/焦虑当笑料
- 文案幽默但温和，不刻薄，不绝望
- 不生成鼓励自伤、放弃求助的文案
- 不声称能治疗、诊断或替代专业帮助
- 不做排行榜、痛苦比较、羞耻感机制
- UI 风格：安静、柔和、克制，不浮夸

---

## 关键文件索引

| 文件 | 作用 |
|------|------|
| `docker-compose.yml` | 启动 PostgreSQL |
| `.env.example` | 环境变量模板（复制为 .env 使用） |
| `backend/main.py` | FastAPI 入口 + /health |
| `backend/database.py` | SQLAlchemy 连接配置 |
| `backend/models.py` | User + CheckIn 表定义 |
| `backend/schemas.py` | Pydantic 数据校验 |
| `backend/migrations/` | Alembic 迁移文件 |
| `frontend/src/App.jsx` | 前端首页 |
