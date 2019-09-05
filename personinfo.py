class personinfo:
    """
    Class that generates new instances of personinfo
    """

    personinfo_list = [] 

    def __init__(self,username,password,email):

        self.username = username
        self.password = password
        self.email = email

        
    personinfo_list = [] 
    
    def save_personinfo(self):

        '''
        save_personinfo method saves personinfo objects into personinfo_list
        '''

        personinfo.personinfo_list.append(self)
      