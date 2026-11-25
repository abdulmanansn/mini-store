
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

INSERT INTO customers (name, email)
VALUES ('Ahmed Ali', 'ahmed@example.com');

SELECT * FROM customers;
