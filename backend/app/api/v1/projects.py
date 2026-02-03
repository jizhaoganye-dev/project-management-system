"""
案件（プロジェクト）API
CRUD操作
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional

from app.database import get_db
from app.models.project import Project
from app.models.user import User
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
    ProjectStats,
)
from app.core.deps import get_current_user

router = APIRouter()


@router.get("/", response_model=List[ProjectResponse])
async def get_projects(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    status: Optional[str] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    案件一覧取得
    """
    query = db.query(Project).filter(Project.user_id == current_user.id)
    
    if status:
        query = query.filter(Project.status == status)
    
    if priority:
        query = query.filter(Project.priority == priority)
    
    if search:
        search_pattern = f"%{search}%"
        query = query.filter(
            (Project.title.ilike(search_pattern)) |
            (Project.description.ilike(search_pattern))
        )
    
    query = query.order_by(Project.updated_at.desc())
    
    projects = query.offset(skip).limit(limit).all()
    return projects


@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    project_data: ProjectCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    案件作成
    """
    new_project = Project(
        **project_data.model_dump(),
        user_id=current_user.id
    )
    
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    
    return new_project


@router.get("/stats", response_model=ProjectStats)
async def get_project_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    案件統計情報取得
    """
    user_projects = db.query(Project).filter(Project.user_id == current_user.id)
    
    stats = {
        "total": user_projects.count(),
        "planning": user_projects.filter(Project.status == "planning").count(),
        "in_progress": user_projects.filter(Project.status == "in_progress").count(),
        "completed": user_projects.filter(Project.status == "completed").count(),
        "on_hold": user_projects.filter(Project.status == "on_hold").count(),
        "cancelled": user_projects.filter(Project.status == "cancelled").count(),
    }
    
    return stats


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    案件詳細取得
    """
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"案件ID {project_id} が見つかりません"
        )
    
    return project


@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    案件更新
    """
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"案件ID {project_id} が見つかりません"
        )
    
    update_data = project_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(project, field, value)
    
    db.commit()
    db.refresh(project)
    
    return project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    案件削除
    """
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"案件ID {project_id} が見つかりません"
        )
    
    db.delete(project)
    db.commit()
    
    return None
