class credentials:
    """
    Class that generates new instances of user's credentials
    """
    pass

    credentials_list=[]

    def __init__(self,twitter_account,password):
        self.twitter_account = twitter_account
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        credentials.credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        credentials.credentials_list.remove(self)
    
    @classmethod
    def find_by_twitter_account(cls,twitter_account):
        '''
        Method that takes in a twitter_account and returns a credentials that matches that credentials.
        Args:
            twitter_account: twitter_account to search for
        Returns :
           credentials of person that matches the number.
        '''

        for credentials in cls.credentials_list:
            if credentials.twitter_account == twitter_account:
                return credentials

    @classmethod
    def credentials_exist(cls,twitter_account):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            twitter_account: twitter_account to search for
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.twitter_account == twitter_account:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list    