import sqlite3

def main():
	
	conn = sqlite3.connect('Italia.db')
	c = conn.cursor()
	
	c.execute('''CREATE TABLE roster
				 (
				  id 	INTEGER PRIMARY KEY NOT NULL,
				  name 	TEXT, 
				  age 	INTEGER, 
				  club 	TEXT
				  )''')
	
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()
