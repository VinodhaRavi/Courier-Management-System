from db.db_connection import get_connection
from mysql.connector import Error

class CourierServiceDb:

    def __init__(self):
        self.cnx = get_connection()
        self._ensure_tables()

    def _ensure_tables(self):
        ddl = """
        CREATE TABLE IF NOT EXISTS courier(
            id INT AUTO_INCREMENT PRIMARY KEY,
            tracking   VARCHAR(20) UNIQUE,
            status     VARCHAR(50),
            user_id    INT,
            delivery_date DATE
        );
        CREATE TABLE IF NOT EXISTS payment(
            id INT AUTO_INCREMENT PRIMARY KEY,
            courier_id INT,
            amount DECIMAL(10,2),
            pay_date DATE
        );
        """
        cur = self.cnx.cursor()
        for stmt in ddl.strip().split(";"):
            if stmt.strip():
                cur.execute(stmt)
        self.cnx.commit()

    def insert_courier(self, tracking, status, user_id=None, date=None):
        sql = "INSERT INTO courier(tracking,status,user_id,delivery_date) VALUES(%s,%s,%s,%s)"
        cur = self.cnx.cursor()
        cur.execute(sql, (tracking, status, user_id, date))
        self.cnx.commit()

    def update_status(self, tracking, new_status):
        cur = self.cnx.cursor()
        cur.execute("UPDATE courier SET status=%s WHERE tracking=%s",
                    (new_status, tracking))
        self.cnx.commit()

    def get_status(self, tracking):
        cur = self.cnx.cursor()
        cur.execute("SELECT status FROM courier WHERE tracking=%s", (tracking,))
        row = cur.fetchone()
        return row[0] if row else None
