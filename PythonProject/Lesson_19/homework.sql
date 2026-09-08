DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

-- ========================================================
-- 1. Спроектированные таблицы и ограничения (PRIMARY, FOREIGN KEY, UNIQUE)
-- ========================================================

-- Таблица пользователей
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица товаров
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0
);

-- Таблица заказов
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Таблица позиций в заказе
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price_at_purchase REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);

-- Индексы для часто используемых запросов
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_order_items_order_product ON order_items(order_id, product_id);


-- ========================================================
-- 2. Добавление данных (SEEDING)
-- ========================================================

INSERT INTO users (email, first_name, last_name) VALUES
('alex@dodo.com', 'Алексей', 'Хлебушкин'),
('maria@dodo.com', 'Мария', 'Иванова'),
('john@dodo.com', 'Иван', 'Смирнов');

INSERT INTO products (title, price, stock) VALUES
('Смартфон', 4500.00, 15),
('Ноутбук', 6900.90, 5),
('Беспроводные наушники', 535.00, 40),
('Чехол для телефона', 135.00, 100);

INSERT INTO orders (user_id, status) VALUES
(1, 'Completed'),
(1, 'Processing'),
(2, 'Completed');

INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase) VALUES
(1, 1, 1, 4500.00),
(1, 3, 2, 535.00),
(2, 4, 1, 135.00),
(3, 2, 1, 6900.90);


-- ========================================================
-- 3. Получение данных, фильтрация и сортировка
-- ========================================================

-- Какие товары дороже 500 рублей, сортировка по цене сверху вниз
SELECT title, price
FROM products
WHERE price > 500.00
ORDER BY price DESC;


-- ========================================================
-- 4. JOIN (Объединение таблиц)
-- ========================================================

-- Получение информации по составу заказа №1 с именами покупателей и товаров
SELECT
    o.id AS order_id,
    u.email AS user_email,
    p.title AS product_title,
    oi.quantity,
    oi.price_at_purchase
FROM order_items oi
JOIN orders o ON oi.order_id = o.id
JOIN users u ON o.user_id = u.id
JOIN products p ON oi.product_id = p.id;


-- ========================================================
-- 5. Агрегатные функции и GROUP BY
-- ========================================================

-- Подсчет общей стоимости каждого заказа и сколько уникальных товаров в нем
SELECT
    oi.order_id,
    COUNT(oi.product_id) AS total_unique_products,
    SUM(oi.quantity * oi.price_at_purchase) AS total_order_sum
FROM order_items oi
GROUP BY oi.order_id;


-- ========================================================
-- 6. Изменение и удаление данных (UPDATE / DELETE)
-- ========================================================

-- Обновим статус заказа
UPDATE orders SET status = 'Shipped' WHERE id = 2;

-- Уберу из каталога товар, которого нет на складе (допустим, добавим и удалим)
DELETE FROM products WHERE stock = 0;