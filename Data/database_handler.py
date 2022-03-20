import os
import sqlite3

class DatabaseHandler():
	def __init__(self, database_name : str):
		self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
		self.con.row_factory = sqlite3.Row

	def add_account(self ,website: str, email: str, username: str, password: str):
		cursor = self.con.cursor()
		query = f"INSERT INTO Account (website, email, username, password) VALUES ('{website}', '{email}', '{username}', '{password}');"
		cursor.execute(query)
		cursor.close()
		self.con.commit()
    
	def del_account(self, website : str):
		cursor = self.con.cursor()
		query = f"DELETE FROM account WHERE website = '{website}';"
		cursor.execute(query)
		cursor.close()
		self.con.commit()

	def list_account(self, website: str):
		cursor = self.con.cursor()
		query = f"SELECT * FROM account WHERE website = ?;"
		cursor.execute(query, (website,))
		result = cursor.fetchall()
		cursor.close()
		print(dict(result[0]))
        