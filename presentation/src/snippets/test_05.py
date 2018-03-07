# test_05.py
import sqlite3
from unittest import TestCase

class DBConnectionTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(':memory:')
        cur =  cls.conn.cursor()
        people = [('Cersei', 'Lannister'), ('Jon', 'Snow')]
        cur.execute("CREATE TABLE people (first, last);")
        cur.executemany("INSERT INTO people VALUES (?, ?);", people)
        cur.execute("COMMIT")
        cur.close()

    def setUp(self):
        self.cur = self.conn.cursor()
        self.conn.execute("BEGIN;")

    def test_adding_a_new_person(self):
        self.cur.execute("INSERT INTO people VALUES ('Arya', 'Stark');")
        self.cur.execute("SELECT count(*) from people;")
        row = self.cur.fetchone()
        self.assertEqual(row[0], 3)

    def test_we_reverted(self):
        self.cur.execute("SELECT count(*) from people;")
        row = self.cur.fetchone()
        self.assertEqual(row[0], 2)

    def tearDown(self):
        self.cur.execute("ROLLBACK;")
        self.cur.close()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
