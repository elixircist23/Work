import sqlite3

class DBUtil:
    
    #need to add mysql support
    def __init__(self, Path, Table):
        self.conn = sqlite3.connect(Path)
        self.c = self.conn.cursor()
        self.path = Path
        self.table = Table

    #add column list?    
    def insert(self, Name, Age, Club):
        self.c.execute("INSERT INTO %s (name, age, club) VALUES ('%s', '%s', '%s');"
                       % (self.table, Name, Age, Club))
        self.conn.commit();

    def query(self, columnList):
        if type(columnList) != list:
            print('columnList parameter needs to be a list')
            return
        
        columnString = ''
        for i in columnList:
            columnString = columnString + i + ','
        #take out the last comma
        columnString = columnString[:-1]
        self.conn.commit();

        return self.c.execute('SELECT %s FROM %s;' % (columnString, self.table))
            

    def update(self, setColumn, setValue, whereColumn, whereValue):
        self.c.execute("UPDATE %s SET %s = '%s' WHERE %s = '%s';"
                       % (self.table, setColumn, setValue, whereColumn, whereValue))


    

        

        
        
