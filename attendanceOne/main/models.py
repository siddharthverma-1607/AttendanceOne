import base64
# Create your models here.


class User():
    def __init__(self, *args):
        self.name = args[0]
        self.email = args[1]
        self.contact = args[2]
        self.organization = args[3]
        self.age = args[4]
        self.password = base64.b64encode(args[5].encode("utf-8"))

    def __str__(self):
        return self.name
