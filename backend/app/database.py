"""
データベース接続設定
SQLAlchemy設定
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# データベースエンジン
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # SQLログ出力（開発時のみ）
)

# セッションローカル
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# モデルのベースクラス
Base = declarative_base()


# データベースセッション取得（依存性注入）
def get_db():
    """
    データベースセッションを取得
    FastAPIの依存性注入で使用
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
