
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS manager;
DROP TABLE IF EXISTS food;
DROP TABLE IF EXISTS restaurant;
DROP TABLE IF EXISTS restaurant_food;
DROP TABLE IF EXISTS order;
DROP TABLE IF EXISTS comment;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  phone_number TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  name TEXT NOT NULL,
  region TEXT NOT NULL,
  address TEXT NOT NULL,
  credit REAL NOT NULL
);

CREATE TABLE manager (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  name TEXT NOT NULL
--  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--  author_id INTEGER NOT NULL,
--  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE restaurant (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  region TEXT NOT NULL,
  address TEXT NOT NULL,
  serving_regions TEXT NOT NULL,
  work_hours TEXT NOT NULL,
  delivery_time REAL NOT NULL,
  delivery_fee REAL NOT NULL,
  manager_id INTEGER,
  FOREIGN KEY (manager_id)
           REFERENCES manager(id)
);


CREATE TABLE food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);


CREATE TABLE restaurant_food (
    restaurant_id INTEGER,
    food_id INTEGER,
    count INTEGER NOT NULL,
    copen TEXT NOT NULL DEFAULT "none",
    price REAL NOT NULL,
    disabled INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (restaurant_id)
           REFERENCES restaurant(id),
    FOREIGN KEY (food_id)
           REFERENCES food(id),
    PRIMARY KEY (restaurant_id, food_id)
);

CREATE TABLE order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    restaurant_id INTEGER,
    food_id INTEGER,
    count INTEGER NOT NULL DEFAULT 1,
    status TEXT NOT NULL DEFAULT "restaurant confirmation pending",
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)
           REFERENCES user(id),
    FOREIGN KEY (restaurant_id)
           REFERENCES restaurant(id),
    FOREIGN KEY (food_id)
           REFERENCES food(id)
);


<<<<<<< HEAD
CREATE TABLE order_ (

);
=======
CREATE TABLE comment (
    order_id INTEGER PRIMARY KEY,
    score INTEGER NOT NULL,
    content TEXT NOT NULL,
    manager_reply TEXT,
    FOREIGN KEY (order_id)
           REFERENCES order(id)
);
>>>>>>> f580807477131cef4423f65ecd8b35a9d18d0b51
