import db_structure
while True:
	opt=raw_input("""
	DB Operations:
		1.create
		2.Insert
		3.Update
		4.Delete
		q.quit
	""")
	opt=opt.lower()
	if opt in ['q','quit']:
		print 'Thank You!!!'
		break
	elif opt == '1':
		db_structure.create_customer()
	elif opt == '2':
		db_structure.insert_customer()
	elif opt == '3':
		db_structure.update_customer()
	elif opt == '4':
		db_structure.delete_customer()
	else:
		print 'Wrong Option'
