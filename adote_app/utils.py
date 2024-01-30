import re
from django.contrib import messages
from django.contrib.messages import constants


def password_is_valid(request, password):
    if len(password) < 6:
        messages.add_message(request, constants.ERROR,
                             'Ops! Sua senha deve conter 6 ou mais caractertes!')
        return False

    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR,
                             'Sua senha não contem letras maiúsculas')
        return False

    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR,
                             'Ops! Sua senha não contem letras minúsculas!')
        return False

    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR,
                             'Ops! Sua senha não contém números!')
        return False

    return True
