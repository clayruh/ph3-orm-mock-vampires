from lib import CONN, CURSOR
from lib.classes.castle import Castle

class Vampire:

    # MAGIC METHODS #
    def __init__(self, name, year_born, castle_id, id=None):
        self.name = name
        self.year_born = year_born
        self.castle_id = castle_id
        self.id = id

    def __repr__(self):
        return f"Vampire(id={self.id} name={self.name}, year_born={self.year_born}, castle_id={self.castle_id})"

    # CLASS METHODS #
    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS vampires (
        id INTEGER PRIMARY KEY,
        name TEXT,
        year_born INTEGER,
        castle_id INTEGER
        )
        """
        CURSOR.execute(sql)
    
    @classmethod
    def query_all(cls):
        sql="SELECT * FROM vampires"
        rows = CURSOR.execute(sql).fetchall()
        return [Vampire(row[1], row[2], row[3], row[0]) for row in rows]
    
    @classmethod
    def oldest(cls):
        sql="SELECT min(year_born) FROM vampires"
        oldest_year = CURSOR.execute(sql).fetchone()[0]
        return f"The oldest vampire is {2023 - oldest_year} years old. DAYUM!"

    # PROPERTIES #
    @property
    def year_born(self):
        return self._year_born

    @year_born.setter
    def year_born(self, value):
        if (type(value)==int) and (1432 <= value <= 2002):
            self._year_born = value
        else:
            # what's the difference betw raise and return?
            print(ValueError("vamp too old! (or young, iunno)"))

    @property
    def castle(self):
        sql="SELECT * FROM castles WHERE id = ?"
        row = CURSOR.execute(sql, [self.castle_id]).fetchone()

        if row:
            return Castle(row[1], row[0])
        
    @castle.setter
    def castle(self, value):
        if isinstance(value, Castle):
            self.castle = value.id
        else:
            raise ValueError("that castle doesn't exist breh")

    # INSTANCE METHODS #
    def create(self):
        sql="""INSERT INTO vampires (name, year_born, castle_id)
        VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, [self.name, self.year_born, self.castle_id])
        CONN.commit()

        self.id=CURSOR.lastrowid

    def update(self):
        sql="""UPDATE vampires
        SET name = ?, year_born = ?, castle_id = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, [self.name, self.year_born, self.castle_id, self.id])
        CONN.commit()
    
    def delete(self):
        sql="DELETE FROM vampires WHERE id = ?"
        CURSOR.execute(sql, [self.id])
        CONN.commit()
        self.id = None

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()