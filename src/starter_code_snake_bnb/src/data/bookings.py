import mongoengine

class Booking(mongoengine.EmbeddedDocument):  # This class on the other hand is a subclass of an embedded document
	# This is so we can embed it into our cages class.
	# It means that this class is a not a top level item in mongodb basically,
	# It's just put into a top level class (a document! :))
	guest_owner_id = mongoengine.ObjectIdField()
	guest_snake_id = mongoengine.ObjectIdField()

	booked_date = mongoengine.DateTimeField()
	check_in_date = mongoengine.DateTimeField(required=True)
	check_out_date = mongoengine.DateTimeField(required=True)

	review = mongoengine.StringField()
	rating = mongoengine.IntField(default=0)