# -*- coding: utf-8 -*-
import re


# Define a function for
# for validating an Email
def email_checker(email):
    """
    Python program to validate an Email
    pass the regualar expression and the string in search() method
    :param email:
    :return:
    """
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email):
        return True
    else:
        return False
