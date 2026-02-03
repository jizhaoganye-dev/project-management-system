"""
タスクモデル
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey, DECIMAL
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Task(Base):
    """
    タスクテーブル
    """
    
    __tablename__ = "tasks"
    
    # 主キー
    id = Column(Integer, primary_key=True, index=True)
    
    # 外部キー
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"))
    
    # 基本情報
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    
    # ステータス・優先度
    status = Column(
        String(50),
        default="todo",
        nullable=False,
        index=True,
    )
    priority = Column(
        String(20),
        default="medium",
        nullable=False,
    )
    
    # スケジュール
    due_date = Column(Date)
    estimated_hours = Column(DECIMAL(5, 2))
    actual_hours = Column(DECIMAL(5, 2))
    
    # タイムスタンプ
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, status={self.status})>"
