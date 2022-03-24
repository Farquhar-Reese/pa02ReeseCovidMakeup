import sqlite3
import csv


def to_cat_dict(cat_tuple):
    ''' cat is a category tuple (rowid, name, desc)'''
    cat = {'rowid':cat_tuple[0], 'name':cat_tuple[1], 'desc':cat_tuple[2]}
    return cat

def to_cat_dict_list(cat_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_cat_dict(cat) for cat in cat_tuples]

class Transaction():
    db_name = ''
    def __init__(self, db_name):
        self.db_name = db_name

        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS transactions")
        cur.execute("CREATE TABLE IF NOT EXISTS transactions (item text, amount int, category text, date text, description text)")
        con.commit()
        con.close()
        

    def select_all(self):
        ''' return all of the categories as a list of dicts.'''
        con= sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)
    
    def select_one(self,rowid):
        ''' return a category with a specified rowid '''
        con= sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict(tuples[0])

    def add(self,item):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("INSERT INTO categories VALUES(?,?,?,?,?)",(item['item'],item['desc'], item['amount'] , item['category'] , item['date']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]




if __name__ == "__main__":
    pass