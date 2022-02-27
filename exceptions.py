class FileAlreadyExist(Exception):
    def __init__(self, text):
        self.txt = text

class NotCorrectNickName(Exception):
    def __init__(self, text):
        self.txt = text

class NotCorrectPassword(Exception):
    def __init__(self, text):
        self.txt = text