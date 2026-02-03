"""
ユーザースキーマ
"""

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    """
    ユーザーベーススキーマ
    """
    email: EmailStr
    username: str = Field(..., min_length=1, max_length=100)


class UserCreate(UserBase):
    """
    ユーザー作成スキーマ（リクエスト）
    """
    password: str = Field(..., min_length=8, max_length=100)


class UserResponse(UserBase):
    """
    ユーザーレスポンススキーマ
    """
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserInDB(UserBase):
    """
    データベース内のユーザー（内部使用）
    """
    id: int
    hashed_password: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
