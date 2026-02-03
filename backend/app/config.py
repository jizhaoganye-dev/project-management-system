"""
設定ファイル
環境変数の管理
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    アプリケーション設定
    """
    
    # アプリケーション
    APP_NAME: str = "Project Management API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # データベース
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/project_management"
    
    # JWT認証
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# 設定インスタンス
settings = Settings()
