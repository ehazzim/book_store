-- Drop tables if they already exist to allow clean re-seeding
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS users;

-- Create the books table
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT
);

-- Create the users table for authentication
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Seed initial books data
INSERT INTO books (title, author) VALUES
    ('The Gruffalo', 'Julia Donaldson'),
    ('Ada Twist, Scientist', 'Andrea Beaty'),
    ('The Girl Who Drank the Moon', 'Kelly Barnhill'),
    ('Dragons in a Bag', 'Zetta Elliott'),
    ('Dune', 'Frank Herbert'),
    ('Neuromancer', 'William Gibson'),
    ('Do Androids Dream of Electric Sheep?', 'Philip K. Dick'),
    ('Snow Crash', 'Neal Stephenson');

-- Seed initial test user
INSERT INTO users (username, password) VALUES
    ('cyber_reader', 'matrix_pass123');