class Owner:
	registered_date = None
	name = None
	email = None

	snake_ids = list()
	cage_ids = list()
	
	meta = {
		'db_alias': 'core',  # Telling mongodb that this entry goes into the core db
		'collection': 'owners'  # Telling mongodb that this goes to the 'snakes' collection (table?)
	}