"""
認証スキーマ
"""

from pydantic import BaseModel, EmailStr
from typing import Optional


class Token(BaseModel):
    """
    トークンレスポンス
    """
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """
    トークンデータ（デコード後）
    """
    user_id: Optional[int] = None
    email: Optional[str] = None


class LoginRequest(BaseModel):
    """
    ログインリクエスト
    """
    email: EmailStr
    password: str
