import random
from user import User
from credentials import Credential

def create_user_account(user_name,pass_word):
    """
    Function to create a new account
    """
    new_user = User(user_name,pass_word)
    return new_user