class PersonInfo:
    """
    Class that generates new instances of PersonInfo
    """

    PersonInfo_list = [] 

    def __init__(self,login,username,password,email):

        self.login = login
        self.username = username
        self.password = password
        self.email = email