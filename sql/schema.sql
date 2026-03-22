-- FitWell Health Analytics Database Schema
-- Author: Doreen Tumuhairwe
-- University of the Pacific, M.S. Data Science

-- ─────────────────────────────────────────
-- TABLE 1: users
-- Stores information about each user
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS users (
    user_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    email       TEXT UNIQUE NOT NULL,
    age         INTEGER,
    created_at  DATE DEFAULT CURRENT_DATE
);

-- ─────────────────────────────────────────
-- TABLE 2: workouts
-- Stores each workout session per user
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS workouts (
    workout_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id      INTEGER NOT NULL,
    week         TEXT NOT NULL,
    category     TEXT CHECK(category IN ('Cardio', 'Strength', 'Flexibility')),
    sessions     INTEGER DEFAULT 0,
    logged_at    DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- ─────────────────────────────────────────
-- TABLE 3: wellness_logs
-- Stores daily sleep and mental health scores
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS wellness_logs (
    log_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         INTEGER NOT NULL,
    week            TEXT NOT NULL,
    sleep_score     INTEGER CHECK(sleep_score BETWEEN 0 AND 100),
    mental_score    INTEGER CHECK(mental_score BETWEEN 0 AND 100),
    logged_at       DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- ─────────────────────────────────────────
-- TABLE 4: nutrition_logs
-- Stores daily calorie data per user
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS nutrition_logs (
    nutrition_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id          INTEGER NOT NULL,
    week             TEXT NOT NULL,
    calories_burned  INTEGER,
    calorie_target   INTEGER DEFAULT 2400,
    logged_at        DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- ─────────────────────────────────────────
-- SAMPLE QUERIES
-- ─────────────────────────────────────────

-- Get all workouts for a user
-- SELECT * FROM workouts WHERE user_id = 1;

-- Get average sleep score per week
-- SELECT week, AVG(sleep_score) FROM wellness_logs GROUP BY week;

-- Get weeks where calories were below target
-- SELECT week, calories_burned, calorie_target
-- FROM nutrition_logs
-- WHERE calories_burned < calorie_target;