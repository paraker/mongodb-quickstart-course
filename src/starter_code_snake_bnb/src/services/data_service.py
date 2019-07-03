from src.starter_code_snake_bnb.src.data.owners import Owner

from src.starter_code_snake_bnb.src.data.cages import Cage


def create_account(name: str, email: str) -> Owner:
    owner = Owner()  # Instantiate an Owner (a host)
    owner.name = name  # add name to the instance
    owner.email = email  # add email to the instance

    owner.save()  # save is a method inherited from the mongoengine Document class
    # The save() method will use all default values in the creation, I think.
    # I also think that this will create the entry in the database.

    return owner


def find_account_by_email(email: str) -> Owner:
    """

    :param email: the email address of the person creating the account
    :return: result of query from db for the email address (if it exists)
    """
    owner = Owner.objects().filter(email=email).first()  # returns the value from a query to the db, we're choosing the
    # first object i the return statement.
    # I think it looks through all objects called email in the owners collection.
    return owner  # return back


def register_cage(active_account, name, allow_dangerous, has_toys, carpeted, metres) -> Cage:
    cage = Cage()
    cage.name = name
    cage.square_metres = metres
    cage.is_carpeted = carpeted
    cage.has_toys = has_toys
    cage.allow_dangerous_snakes = allow_dangerous
    cage.save()

    account = find_account_by_email(active_account.email)
    account.cage_ids.append(cage.id)
    account.save()

    return cage
