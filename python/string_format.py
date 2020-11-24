from string import Template

SECRET = 'secret'

class Error:
    def __init__(self):
        pass

err = Error()
user_input = '${error.__init__.__globals__[SECRET]}'
print(Template(user_input).substitute(error=err))
