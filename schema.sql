
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS manager;
DROP TABLE IF EXISTS food;
DROP TABLE IF EXISTS restaurant;
DROP TABLE IF EXISTS restaurant_food;
DROP TABLE IF EXISTS f_order;
DROP TABLE IF EXISTS comment;

CREATE TABLE user (
  phone_number TEXT PRIMARY KEY,
  password TEXT NOT NULL,
  name TEXT NOT NULL,
  region TEXT NOT NULL,
  address TEXT NOT NULL,
  credit REAL NOT NULL
);

CREATE TABLE manager (
  email TEXT PRIMARY KEY,
  password TEXT NOT NULL,
  name TEXT NOT NULL
--  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--  author_id INTEGER NOT NULL,
--  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE restaurant (
  name TEXT PRIMARY KEY,
  region TEXT NOT NULL,
  address TEXT NOT NULL,
  serving_regions TEXT NOT NULL,
  work_hours TEXT NOT NULL,
  delivery_time REAL NOT NULL,
  delivery_fee REAL NOT NULL,
  manager_email TEXT,
  FOREIGN KEY (manager_email)
           REFERENCES manager(email)
);


CREATE TABLE food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);


CREATE TABLE restaurant_food (
    restaurant_name TEXT,
    food_id INTEGER,
    count INTEGER NOT NULL,
    copen TEXT NOT NULL DEFAULT "none",
    price REAL NOT NULL,
    disabled INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (restaurant_name)
           REFERENCES restaurant(name),
    FOREIGN KEY (food_id)
           REFERENCES food(id),
    PRIMARY KEY (restaurant_name, food_id)
);

CREATE TABLE f_order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_phone TEXT,
    restaurant_name TEXT,
    food_id INTEGER,
    count INTEGER NOT NULL DEFAULT 1,
    status TEXT NOT NULL DEFAULT "restaurant confirmation pending",
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_phone)
           REFERENCES user(phone_number),
    FOREIGN KEY (restaurant_name)
           REFERENCES restaurant(name),
    FOREIGN KEY (food_id)
           REFERENCES food(id)
);


CREATE TABLE comment (
    order_id INTEGER PRIMARY KEY,
    score INTEGER NOT NULL,
    content TEXT NOT NULL,
    manager_reply TEXT,
    FOREIGN KEY (order_id)
           REFERENCES f_order(id)
);
