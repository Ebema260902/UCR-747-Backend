# TCU-747 — Backend

API REST construida con FastAPI y SQLite. Provee los datos de proyectos, materiales académicos, juegos y creadores del portal TCU-747.

---

## Requisitos previos

| Herramienta | Versión mínima | Descarga |
|-------------|---------------|---------|
| Python | 3.11+ | https://www.python.org/downloads/ |
| Node.js | 18+ | https://nodejs.org/ |
| Git | cualquiera | https://git-scm.com/ |

---

## Instalación (primera vez)

### 1. Clonar ambos repositorios en la misma carpeta

Es importante que queden como carpetas hermanas con exactamente estos nombres:

```
mi-carpeta/
├── UCR-747/            ← frontend
└── UCR-747 Backend/    ← este repo (backend)
```

```bash
git clone https://github.com/stefanoSAN23/UCR-747.git
git clone https://github.com/Ebema260902/UCR-747-Backend.git "UCR-747 Backend"
```

### 2. Instalar dependencias del backend

Dentro de la carpeta `UCR-747 Backend`:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Instalar dependencias del frontend

Dentro de la carpeta `UCR-747`:

```bash
npm install
```

---

## Iniciar los servidores

### Opción A — Doble clic (recomendado)

Hacé doble clic en **`Iniciar TCU-747.bat`** (está en esta carpeta).

Se abren dos ventanas minimizadas en la barra de tareas:
- `TCU-747 Backend` → API en http://localhost:8000
- `TCU-747 Frontend` → App en http://localhost:5173

El navegador se abre solo en unos segundos.

> Para detener los servidores, cerrá esas dos ventanas de la barra de tareas.

### Opción B — Acceso directo en el escritorio

Para no tener que buscar el archivo cada vez:

1. Encontrá `Iniciar TCU-747.bat` en esta carpeta
2. Clic derecho → **Enviar a** → **Escritorio (crear acceso directo)**
3. Desde ahora lo iniciás directamente desde el escritorio

### Opción C — Comandos manuales

```bash
# Terminal 1 — Backend
cd "UCR-747 Backend"
venv\Scripts\activate
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Terminal 2 — Frontend
cd UCR-747
npm run dev
```

---

## Publicar cambios en GitHub

Dentro de la aplicación (barra lateral izquierda) hay un botón **"Publicar en GitHub"** que sube los cambios de ambos repositorios a la vez.

Cualquier otra persona puede actualizar su copia local con:

```bash
git pull   # dentro de cada carpeta
```

---

## Estructura del proyecto

```
app/
├── models/       # Modelos SQLAlchemy
├── routes/       # Endpoints de la API
├── schemas/      # Esquemas Pydantic
├── database.py   # Conexión SQLite
└── main.py       # Punto de entrada
scripts/
└── seed_data.py  # Datos de ejemplo
database.db       # Base de datos local (se incluye en el repo)
```
