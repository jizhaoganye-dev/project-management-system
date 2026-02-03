"""
Project Management API
FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# アプリケーション作成
app = FastAPI(
    title="Project Management API",
    description="案件管理システムのREST API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS設定（フロントエンドからのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # ローカル開発
        "http://localhost:5173",  # Vite開発サーバー
        "https://*.vercel.app",   # Vercelデプロイ
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ルートエンドポイント
@app.get("/")
async def root():
    """
    APIルート - ヘルスチェック
    """
    return {
        "message": "Project Management API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
    }


# ヘルスチェックエンドポイント
@app.get("/health")
async def health_check():
    """
    ヘルスチェック
    """
    return {
        "status": "healthy",
        "database": "connected",
    }


# スタートアップイベント
@app.on_event("startup")
async def startup_event():
    """
    アプリケーション起動時の処理
    """
    print("🚀 Project Management API starting...")
    print("📚 API Docs: http://localhost:8000/docs")


# シャットダウンイベント
@app.on_event("shutdown")
async def shutdown_event():
    """
    アプリケーション終了時の処理
    """
    print("👋 Project Management API shutting down...")


# APIルーター登録
from app.api.v1 import auth, projects, tasks

app.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication"])
app.include_router(projects.router, prefix="/api/v1/projects", tags=["projects"])
app.include_router(tasks.router, prefix="/api/v1", tags=["tasks"])
