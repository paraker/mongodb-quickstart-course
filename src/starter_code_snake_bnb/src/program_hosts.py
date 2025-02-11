from colorama import Fore
from src.starter_code_snake_bnb.src.infrastructure.switchlang import switch
import src.starter_code_snake_bnb.src.infrastructure.state as state
import src.starter_code_snake_bnb.src.services.data_service as svc


def run():
    print(' ****************** Welcome host **************** ')
    print()

    show_commands()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case('c', create_account)
            s.case('a', log_into_account)
            s.case('l', list_cages)
            s.case('r', register_cage)
            s.case('u', update_availability)
            s.case('v', view_bookings)
            s.case('m', lambda: 'change_mode')
            s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
            s.case('?', show_commands)
            s.case('', lambda: None)
            s.default(unknown_command)

        if action:
            print()

        if s.result == 'change_mode':
            return


def show_commands():
    print('What action would you like to take:')
    print('[C]reate an account')
    print('Login to your [a]ccount')
    print('[L]ist your cages')
    print('[R]egister a cage')
    print('[U]pdate cage availability')
    print('[V]iew your bookings')
    print('Change [M]ode (guest or host)')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()


def create_account():
    print(' ****************** REGISTER **************** ')
    name = input('What is your name?')
    email = input('What is your email?').strip().lower()

    old_account = svc.find_account_by_email(email)
    if old_account:
        error_msg(f'ERROR: the account with email {email} already exists.')
        return
    state.active_account = svc.create_account(name, email)  # State.active_account is a variable from the
    # infrastructure folder.
    # active_account starts as None but is set here to the return value from the data_service module
    success_msg(f'Created new accounts with id {state.active_account.id}')


def log_into_account():
    print(' ****************** LOGIN **************** ')

    email = input('What is your email?').strip().lower()
    account = svc.find_account_by_email(email)

    if not account:
        error_msg(f'could not find account with email {email}')
        return

    state.active_account = account
    success_msg('logged in successfully')


def register_cage():
    print(' ****************** REGISTER CAGE **************** ')

    if not state.active_account:
        error_msg('you ust log in to register a cage')

    metres = input('How many square metres is the cage?')
    if not metres:
        error_msg('cancelled')
        return

    metres = float(metres)
    carpeted = input('carpeted? y/n').lower().startswith('y')
    has_toys = input('snake toys? y/n').lower().startswith('y')
    allow_dangerous = input('tolerates venomous snakes? y/n').lower().startswith('y')
    name = input('give your cage a name')

    svc.register_cage(
        state.active_account,
        name, allow_dangerous,
        has_toys, carpeted, metres
    )

    state.reload_account()
    success_msg(f'Register new cage with id {cage.id}')


def list_cages(suppress_header=False):
    if not suppress_header:
        print(' ******************     Your cages     **************** ')

    # TODO: Require an account
    # TODO: Get cages, list details

    print(" -------- NOT IMPLEMENTED -------- ")


def update_availability():
    print(' ****************** Add available date **************** ')

    # TODO: Require an account
    # TODO: list cages
    # TODO: Choose cage
    # TODO: Set dates, save to DB.

    print(" -------- NOT IMPLEMENTED -------- ")


def view_bookings():
    print(' ****************** Your bookings **************** ')

    # TODO: Require an account
    # TODO: Get cages, and nested bookings as flat list
    # TODO: Print details for each

    print(" -------- NOT IMPLEMENTED -------- ")


def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
