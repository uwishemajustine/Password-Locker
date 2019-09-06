class personinfo:
    """
    Class that generates new instances of personinfo
    """

    personinfo_list = [] 

    def __init__(self,login_name,username,password,email):

        self.login_name = login_name
        self.username = username
        self.password = password
        self.email = email

        
    personinfo_list = [] 
    
    def save_personinfo(self):

        '''
        save_personinfo method saves personinfo objects into personinfo_list
        '''

        personinfo.personinfo_list.append(self)
    
    def delete_personinfo(self):

        '''
        delete_personinfo method deletes a saved personinfo from the personinfo_list
        '''

        personinfo.personinfo_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a personinfo that matches that personinfo.
        Args:
            username: username to search for
        Returns :
            personinfo of person that matches the number.
        '''

        for personinfo in cls.personinfo_list:
            if personinfo.username == username:
                return personinfo
