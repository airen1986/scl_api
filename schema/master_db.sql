--
-- File generated with SQLiteStudio v3.4.17 on Fri Nov 28 11:34:28 2025
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: S_Models
CREATE TABLE S_Models (
    ModelId     INTEGER PRIMARY KEY AUTOINCREMENT,
    ModelUID    TEXT    NOT NULL
                        UNIQUE,
    ModelName   TEXT,
    ProjectName TEXT,
    ModelPath   TEXT,
    CreatedAt   TEXT    NOT NULL
                        DEFAULT (datetime('now') ),
    OwnerId     INTEGER,
    UNIQUE (
        ModelName,
        ProjectName
    )
);


-- Table: S_UserModels
CREATE TABLE S_UserModels (
    ModelId     INTEGER,
    UserId      INTEGER,
    AccessLevel TEXT    NOT NULL,
    GrantedAt   TEXT    NOT NULL
                        DEFAULT (datetime('now') ),
    PRIMARY KEY (
        ModelId,
        UserId
    )
);


-- Table: S_UserRoles
CREATE TABLE S_UserRoles (
    RoleId      INTEGER PRIMARY KEY AUTOINCREMENT,
    RoleName    TEXT    NOT NULL
                        UNIQUE,
    RoleDescription TEXT,
    CreatedAt   TEXT    NOT NULL
                        DEFAULT (datetime('now') ),
    UpdatedAt   TEXT    NOT NULL
                        DEFAULT (datetime('now') ) 
);


-- Table: S_Users
CREATE TABLE S_Users (
    UserId         INTEGER PRIMARY KEY AUTOINCREMENT,
    RoleId         INTEGER NOT NULL,
    Email          TEXT    NOT NULL
                           UNIQUE,
    DisplayName    TEXT,
    PasswordHash   TEXT    NOT NULL,
    PasswordSalt   TEXT    NOT NULL,
    ActivationCode TEXT,
    ResetToken     TEXT,
    TokenExpiry    TEXT,
    IsActive       INTEGER NOT NULL
                           DEFAULT 1,
    CreatedAt      TEXT    NOT NULL
                           DEFAULT (datetime('now') ),
    UpdatedAt      TEXT    NOT NULL
                           DEFAULT (datetime('now') ) 
);

INSERT INTO S_UserRoles (RoleId, RoleName, RoleDescription) VALUES (0, 'User', 'General User');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
