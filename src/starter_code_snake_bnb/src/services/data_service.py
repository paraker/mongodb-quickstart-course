from data.owners import Owner


def create_account(name: str, email: str) -> Owner:
    owner = Owner()  # Instantiate an Owner
    owner.name = name  # add name to the instance
    owner.email = email  # add email to the instance

    owner.save()  # save is a method inherited from the mongoengine Document class
    # The save() method will use all default values in the creation, I think

    return owner


def find_account_by_email(email: str) -> Owner:
    """

    :param email: the email address of the person creating the account
    :return: result of query from db for the email address (if it exists)
    """
    owner = Owner.objects().filter(email=email).first()  # returns the value from a query to the db, we're choosing the
    # first object i the return statement.
    return owner  # return back
