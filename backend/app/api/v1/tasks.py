"""
タスクAPI
CRUD操作
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.models.task import Task
from app.models.project import Project
from app.models.user import User
from app.schemas.task import (
    TaskCreate,
    TaskResponse,
    TaskUpdate,
    TaskStats,
)
from app.core.deps import get_current_user

router = APIRouter()


@router.get("/project/{project_id}/tasks", response_model=List[TaskResponse])
async def get_project_tasks(
    project_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    status: Optional[str] = None,
    priority: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    案件のタスク一覧取得
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
    
    query = db.query(Task).filter(Task.project_id == project_id)
    
    if status:
        query = query.filter(Task.status == status)
    
    if priority:
        query = query.filter(Task.priority == priority)
    
    query = query.order_by(Task.created_at.asc())
    
    tasks = query.offset(skip).limit(limit).all()
    return tasks


@router.post("/project/{project_id}/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    project_id: int,
    task_data: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    タスク作成
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
    
    if task_data.project_id != project_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="URLのproject_idとリクエストボディのproject_idが一致しません"
        )
    
    new_task = Task(**task_data.model_dump())
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task


@router.get("/project/{project_id}/tasks/stats", response_model=TaskStats)
async def get_task_stats(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    タスク統計情報取得
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
    
    project_tasks = db.query(Task).filter(Task.project_id == project_id)
    
    stats = {
        "total": project_tasks.count(),
        "todo": project_tasks.filter(Task.status == "todo").count(),
        "in_progress": project_tasks.filter(Task.status == "in_progress").count(),
        "completed": project_tasks.filter(Task.status == "completed").count(),
        "blocked": project_tasks.filter(Task.status == "blocked").count(),
    }
    
    return stats


@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    タスク詳細取得
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"タスクID {task_id} が見つかりません"
        )
    
    project = db.query(Project).filter(
        Project.id == task.project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="このタスクにアクセスする権限がありません"
        )
    
    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    タスク更新
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"タスクID {task_id} が見つかりません"
        )
    
    project = db.query(Project).filter(
        Project.id == task.project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="このタスクを更新する権限がありません"
        )
    
    update_data = task_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    
    db.commit()
    db.refresh(task)
    
    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    タスク削除
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"タスクID {task_id} が見つかりません"
        )
    
    project = db.query(Project).filter(
        Project.id == task.project_id,
        Project.user_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="このタスクを削除する権限がありません"
        )
    
    db.delete(task)
    db.commit()
    
    return None
