class personinfo:
    """
    Class that generates new instances of PersonInfo
    """

    personinfo_list = [] 

    def __init__(self,username,password,email):

        self.username = username
        self.password = password
        self.email = email