-- =========================================
-- Proyecto TCU - SQLite
-- =========================================

PRAGMA foreign_keys = ON;

-- Tabla Creator
CREATE TABLE Creator (
    creator_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_creator TEXT NOT NULL,
    photo_creator TEXT,
    state TEXT,
    career TEXT
);

-- Tabla Category
CREATE TABLE Category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_category TEXT NOT NULL
);

-- Tabla Project
CREATE TABLE Project (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    name_project TEXT NOT NULL,
    description TEXT,
    photo_project TEXT,
    date DATE,
    file_id TEXT,
    state TEXT,
    FOREIGN KEY (creator_id) REFERENCES Creator(creator_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- Tabla Games
CREATE TABLE Games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    name_game TEXT NOT NULL,
    photo_game TEXT,
    description TEXT,
    link TEXT,
    date DATE,
    file_id TEXT,
    state TEXT,
    FOREIGN KEY (creator_id) REFERENCES Creator(creator_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- Tabla Academic_Material
CREATE TABLE Academic_Material (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    name_material TEXT NOT NULL,
    description TEXT,
    photo_material TEXT,
    date DATE,
    file_id TEXT,
    state TEXT,
    FOREIGN KEY (creator_id) REFERENCES Creator(creator_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);
