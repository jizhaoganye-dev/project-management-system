"""
案件（プロジェクト）モデル
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey, DECIMAL, ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Project(Base):
    """
    案件テーブル
    """
    
    __tablename__ = "projects"
    
    # 主キー
    id = Column(Integer, primary_key=True, index=True)
    
    # 外部キー
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # 基本情報
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    client_name = Column(String(100))
    
    # ステータス・優先度
    status = Column(
        String(50),
        default="planning",
        nullable=False,
        index=True,
    )
    priority = Column(
        String(20),
        default="medium",
        nullable=False,
    )
    
    # 日程・予算
    start_date = Column(Date)
    end_date = Column(Date)
    budget = Column(DECIMAL(10, 2))
    
    # リンク
    repository_url = Column(String(500))
    demo_url = Column(String(500))
    
    # 技術スタック（配列）
    tech_stack = Column(ARRAY(Text))
    
    # タイムスタンプ
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Project(id={self.id}, title={self.title}, status={self.status})>"
