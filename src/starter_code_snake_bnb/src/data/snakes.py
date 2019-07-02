class Snake:
	registered_date = None
	species = None

	length = None
	name = None
	is_venomous = None

	meta = {
		'db_alias': 'core',  # Telling mongodb that this entry goes into the core db
		'collection': 'snakes'  # Telling mongodb that this goes to the 'snakes' collection (table?)
	}