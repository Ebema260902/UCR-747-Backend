@echo off
title TCU-747 - Iniciando...

set BACKEND=%~dp0.
set FRONTEND=%~dp0..\UCR-747

start /min "TCU-747 Backend" cmd /k "title TCU-747 Backend && cd /d "%BACKEND%" && call venv\Scripts\activate.bat && uvicorn app.main:app --host 0.0.0.0 --port 8000"

timeout /t 4 /nobreak > nul

start /min "TCU-747 Frontend" cmd /k "title TCU-747 Frontend && cd /d "%FRONTEND%" && npm run dev"

timeout /t 6 /nobreak > nul

start http://localhost:5173
