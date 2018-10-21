import sqlite3
def getcon():
	con=sqlite3.connection("batch50_bkp.sqlite3")
	cur=con.cursor()
	return cur,con
def create_table_customer():
	cur,con=getcon()
	cur.execute("create table customer(id int, name varchar(250)")
def insert_customer():
	pass
def update_customer():
	pass
if __name__=='__main__':
	create_table_customer()