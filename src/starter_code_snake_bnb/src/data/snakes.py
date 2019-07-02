import mongoengine
import datetime

class Snake(mongoengine.Document):
	registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
	# Above sets a default time to now, note how we're passing a value not using the function, I think?
	
	species = mongoengine.StringField(required=True)  # Tells mongo this is a stringfield? And it's required?

	length = mongoengine.FloatField(required=True)
	name = mongoengine.StringField(required=True)
	is_venomous = mongoengine.BooleanField(required=True)

	meta = {
		'db_alias': 'core',  # Telling mongodb that this entry goes into the core db
		'collection': 'snakes'  # Telling mongodb that this goes to the 'snakes' collection (table?)
	}