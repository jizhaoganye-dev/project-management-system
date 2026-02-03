"""
タスクスキーマ
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class TaskBase(BaseModel):
    """
    タスクベーススキーマ
    """
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    status: str = Field(default="todo", max_length=50)
    priority: str = Field(default="medium", max_length=20)
    due_date: Optional[date] = None
    estimated_hours: Optional[Decimal] = None
    actual_hours: Optional[Decimal] = None


class TaskCreate(TaskBase):
    """
    タスク作成スキーマ
    """
    project_id: int
    assigned_to: Optional[int] = None


class TaskUpdate(BaseModel):
    """
    タスク更新スキーマ（すべてオプショナル）
    """
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[str] = Field(None, max_length=50)
    priority: Optional[str] = Field(None, max_length=20)
    due_date: Optional[date] = None
    estimated_hours: Optional[Decimal] = None
    actual_hours: Optional[Decimal] = None
    assigned_to: Optional[int] = None


class TaskResponse(TaskBase):
    """
    タスクレスポンススキーマ
    """
    id: int
    project_id: int
    assigned_to: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class TaskStats(BaseModel):
    """
    タスク統計スキーマ
    """
    total: int
    todo: int
    in_progress: int
    completed: int
    blocked: int
