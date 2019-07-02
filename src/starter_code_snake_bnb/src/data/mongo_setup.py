import mongoengine

def global_init():
	mongoengine.register_connection(alias='core', name='snake_bnb')
	# This sets up the connections to a local mongodb, with no security,
	# no encryption, no username etc. Purely dev purposes.

	