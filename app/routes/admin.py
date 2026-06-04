import os
import subprocess
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/admin", tags=["admin"])

# Paths derived from this file's location
# __file__ = .../UCR-747 Backend/app/routes/admin.py
_ROUTES_DIR = os.path.dirname(os.path.abspath(__file__))
_APP_DIR = os.path.dirname(_ROUTES_DIR)
BACKEND_DIR = os.path.dirname(_APP_DIR)
FRONTEND_DIR = os.path.normpath(os.path.join(BACKEND_DIR, "..", "UCR-747"))


class GitPushRequest(BaseModel):
    message: str = "Actualización de contenido"


def _run_git_push(path: str, message: str) -> dict:
    try:
        subprocess.run(
            ["git", "add", "-A"],
            cwd=path, check=True, capture_output=True,
            text=True, encoding="utf-8", errors="replace"
        )

        commit = subprocess.run(
            ["git", "commit", "-m", message],
            cwd=path, capture_output=True,
            text=True, encoding="utf-8", errors="replace"
        )

        # "nothing to commit" is not an error
        nothing_to_commit = (
            "nothing to commit" in commit.stdout or
            "nothing to commit" in commit.stderr
        )
        if commit.returncode != 0 and not nothing_to_commit:
            return {"status": "error", "message": commit.stderr or commit.stdout}

        push = subprocess.run(
            ["git", "push"],
            cwd=path, capture_output=True,
            text=True, encoding="utf-8", errors="replace"
        )

        if push.returncode != 0:
            return {"status": "error", "message": push.stderr or push.stdout}

        if nothing_to_commit:
            return {"status": "ok", "message": "Sin cambios nuevos, ya estaba actualizado"}
        return {"status": "ok", "message": "Push exitoso"}

    except FileNotFoundError:
        return {"status": "error", "message": "Git no encontrado. Asegurate de tener git instalado."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.post("/git-push")
def git_push(request: GitPushRequest):
    return {
        "backend": _run_git_push(BACKEND_DIR, request.message),
        "frontend": _run_git_push(FRONTEND_DIR, request.message),
    }
