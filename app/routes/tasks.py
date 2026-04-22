from fastapi import APIRouter
from app.models.task import Task

router = APIRouter()

tasks = []
task_id = 1


@router.post("/tasks")
def create_task(task: Task):
    global task_id

    new_task = {
        "id": task_id,
        "title": task.title
    }

    tasks.append(new_task)
    task_id += 1

    return new_task


@router.get("/tasks")
def get_tasks():
    return tasks


@router.delete("/tasks/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    return {"message": "Task not found"}
