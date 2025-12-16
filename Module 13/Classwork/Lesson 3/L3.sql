-- Create the products table if it doesn't already exist
CREATE TABLE IF NOT EXISTS products (
    product_id text,
    product_name text,
    supplier_id text,
    category_id text,
    unit text,
    price real
);

-- Insert sample data into the products table
INSERT INTO products (product_id, product_name, supplier_id, category_id, unit, price) VALUES
('1', 'Chai', '1', '1', '10 boxes x 20 bags', 18),
('2', 'Chang', '1', '1', '24 - 12 oz bottles', 19),
('3', 'Aniseed Syrup', '1', '2', '12 - 550 ml bottles', 10),
('4', 'Chef Anton Seasoning', '2', '2', '48 - 6 oz jars', 22),
('5', 'Chef Anton Mix', '2', '2', '36 boxes', 21.35);

SELECT * FROM products;

-- Query to count the number of products
SELECT COUNT(product_id) AS product_count FROM products;

-- Query to find the average price of products
SELECT AVG(price) AS average_price FROM products;

-- Query to find the total price of all products
SELECT SUM(price) AS total_price FROM products;

SELECT COUNT(DISTINCT supplier_id) AS distinct_supplier_id FROM products;

SELECT * FROM products WHERE product_name LIKE "__A%";

SELECT AVG(price) AS supplier1_average_price FROM products WHERE supplier_id = '1';

SELECT MIN(price) AS minimum_price FROM products WHERE product_name LIKE "C%";

SELECT price AS second_highest_price FROM products WHERE price = 
    (SELECT MAX(price) FROM products WHERE price < 
        (SELECT MAX(price) FROM products)
-- SELECT MAX(price) AS second_highest_price FROM products 
--     WHERE price < (SELECT MAX(price) FROM products);
);

SELECT * FROM products WHERE LENGTH(unit) > 15;