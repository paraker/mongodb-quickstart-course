active_account = None
import services.data_service as svc


def reload_account():
    global active_account
    if not active_account:
        return

    active_account = svc.find_account_by_email(active_account.email)