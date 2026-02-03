"""
案件（プロジェクト）スキーマ
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime
from decimal import Decimal


class ProjectBase(BaseModel):
    """
    案件ベーススキーマ
    """
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    client_name: Optional[str] = Field(None, max_length=100)
    status: str = Field(default="planning", max_length=50)
    priority: str = Field(default="medium", max_length=20)
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[Decimal] = None
    repository_url: Optional[str] = Field(None, max_length=500)
    demo_url: Optional[str] = Field(None, max_length=500)
    tech_stack: Optional[List[str]] = []


class ProjectCreate(ProjectBase):
    """
    案件作成スキーマ
    """
    pass


class ProjectUpdate(BaseModel):
    """
    案件更新スキーマ（すべてオプショナル）
    """
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    client_name: Optional[str] = Field(None, max_length=100)
    status: Optional[str] = Field(None, max_length=50)
    priority: Optional[str] = Field(None, max_length=20)
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    budget: Optional[Decimal] = None
    repository_url: Optional[str] = Field(None, max_length=500)
    demo_url: Optional[str] = Field(None, max_length=500)
    tech_stack: Optional[List[str]] = None


class ProjectResponse(ProjectBase):
    """
    案件レスポンススキーマ
    """
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ProjectStats(BaseModel):
    """
    案件統計スキーマ
    """
    total: int
    planning: int
    in_progress: int
    completed: int
    on_hold: int
    cancelled: int
