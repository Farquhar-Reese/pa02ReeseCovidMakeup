import sqlite3
import csv


def to_trans_dict(trans_tuple):
    trans = {'rowid':trans_tuple[0], 'item #':trans_tuple[1], 'amount':trans_tuple[2] , 'category':trans_tuple[3] , 'date':trans_tuple[4] , 'description' : trans_tuple[5]}
    return trans

def to_trans_dict_list(trans_tuples):
    ''' convert a list of trans tuples into a list of dictionaries'''
    return [to_trans_dict(transaction) for transaction in trans_tuples]

class Transaction():
    db_name = ''
    def __init__(self, db_name):
        self.db_name = db_name

        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS transactions")
        cur.execute("CREATE TABLE IF NOT EXISTS transactions ('item #' text, 'amount' real, 'category' text, 'date' real, 'description' text)")
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
        return to_trans_dict_list(tuples)
    
    def select_one(self,rowid):
        ''' return a category with a specified rowid '''
        con= sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples[0])

    def summarize(self): #done by nick and adam 
        ''' return all of the categories as a list of dicts '''
        con= sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("SELECT rowid,sum(amount), date from transactions, Group By date Order by rowid ASC;")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list_summarize(tuples)
    
    def add(self,item):
        ''' add a transaction to the transaction table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item #'], item['amount'] , item['category'] , item['date'], item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]
    
    def delete(self,rowid):
        ''' add a category to the categories table.
        this returns the rowid of the inserted element
         '''
    con= sqlite3.connect(self.dbfile)
    cur = con.cursor()
    cur.execute('''DELETE FROM transactions
                   WHERE rowid=(?);
                ''',(rowid,))
    con.commit()
    con.close()



if __name__ == "__main__":
    pass
