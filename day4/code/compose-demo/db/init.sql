CREATE TABLE IF NOT EXISTS items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(8,2) NOT NULL
);

INSERT INTO items (name, price) VALUES
  ('Keyboard', 49.99),
  ('Mouse', 19.50),
  ('Monitor', 179.00);
