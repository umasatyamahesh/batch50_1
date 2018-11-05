import sqlite3
import json
import sys
#sys.path.append('C:\\Users\\umasa\\Anaconda2\\Lib\\site-packages\\sqlalchemy\\dialects\\postgresql')
#print sys.path
import psycopg2
def getcon():
	con=sqlite3.connect("batch50_bkp.sqlite3")
	cur=con.cursor()
	return cur,con

def postgres_getcon():
	f=open("config.json")
	data=json.load(f)
	db_data=data.get("dbdetails")
	dbname=db_data.get("dbname")
	username=db_data.get("username")
	pswd=db_data.get("password")
	port=db_data.get("port")
	host=db_data.get("host")
	con=psycopg2.connect(database=dbname,user=username,password=pswd,port=port,host=host)
	cur=con.cursor()
	return cur,con

def create_customer():
	cur,con=postgres_getcon()
	cur.execute("create table customer(id int, name varchar(250))")
	con.commit()
	con.close()
	print 'Create Successful'

def insert_customer():
	cust_id=int(raw_input("Enter Cust Id:"))
	cust_name=raw_input("Enter Customer Name")
	q="insert into customer values(%s, '%s')" %(cust_id,cust_name)
	cur,con=postgres_getcon()
	cur.execute(q)
	con.commit()
	con.close()
	print 'Insert Successful'

def update_customer():
	cur,con=postgres_getcon()
	new_name=raw_input("Enter New Name:")
	rec=int(raw_input("enter id to be updated"))	
	print rec
	q="update customer set name = '%s' where id = %s"%(new_name,rec)
	#q="update customer set name = new_name where id = 121223"
	#q="update customer set name = 'Mahesh Kumar J' where id = 121223"
	cur.execute(q)
	con.commit()
	con.close()
	print 'Update Successful'

def delete_customer():
	cur,con=postgres_getcon()
	q="drop table customer"
	cur.execute(q)
	con.commit()
	con.close()
	print 'delete Successful'

if __name__=='__main__':
	create_table_customer()