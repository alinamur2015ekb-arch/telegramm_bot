import aiosqlite

DB_NAME = "database.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                text TEXT,
                budget INTEGER,
                term TEXT
            )
        ''')
        await db.commit()

async def create_orders(text, budget, term):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            INSERT INTO orders (text, budget, term) VALUES (?, ?, ?)
        ''', (text, budget, term))
        await db.commit()


async def get_orders():
    async with aiosqlite.connect(DB_NAME) as db:
        order = await db.execute('SELECT * FROM orders')
        result = await order.fetchall()
        return result


async def init_db2():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS applicants (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                stack TEXT,
                portfolio TEXT
            )
        ''')
        await db.commit()

async def create_join(name, age, stack, portfolio):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            INSERT INTO applicants (name, age, stack, portfolio) VALUES (?, ?, ?, 
        ''', (name, age, stack, portfolio))
        await db.commit()

async def get_join():
    async with aiosqlite.connect(DB_NAME) as db:
        join = await db.execute('SELECT * FROM applicants') 
        result = await join.fetchall()
        return result
