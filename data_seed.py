import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    description TEXT,
    stock INTEGER
)
''')

# Insert 100 fake products
for i in range(1, 101):
    category = "laptop" if i % 2 == 0 else "book"
    c.execute("INSERT INTO products (name, category, price, description, stock) VALUES (?, ?, ?, ?, ?)", (
        f"{category.title()} Product {i}",
        category,
        500 + i * 10,
        f"This is a description for {category} {i}",
        100 - (i % 20)
    ))

conn.commit()
conn.close()
print("✅ Mock data inserted.")
