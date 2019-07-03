import datetime
import mongoengine


class Owner(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)

    snake_ids = mongoengine.ListField()
    cage_ids = mongoengine.ListField()

    meta = {
        'db_alias': 'core',  # Telling mongodb that this entry goes into the core db
        'collection': 'owners'  # Telling mongodb that this goes to the 'owners' collection (table?)
    }
