import mongoengine
import datetime

class Cage(mongoengine.Document):  # Sets this class to have a basetype of mongoengine.Document
	registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)

	name = mongoengine.StringField(required=True)
	price = mongoengine.FloatField(required=True)
	square_metres = mongoengine.FloatField(required=True)
	is_carpeted = mongoengine.BooleanField(required=True)
	has_toys = mongoengine.BooleanField(required=True)
	allow_dangerous_snakes = mongoengine.BooleanField(default=False)

	bookings = mongoengine.EmbeddedDocumentListField(Booking)  # we're saying bookings is an embedded document?

		meta = {
		'db_alias': 'core',  # Telling mongodb that this entry goes into the core db
		'collection': 'cages'  # Telling mongodb that this goes to the 'snakes' collection (table?)
	}
	