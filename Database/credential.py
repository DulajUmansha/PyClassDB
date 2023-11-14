class Credential:
    def __init__(self) -> None:
        self.user_name = None
        self.password = None

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, value):
        self.user_name = value

    def get_password(self):
        return self.password

    def set_password(self, value):
        self.password = value
