class credentials:
    """
    Class that generates new instances of user's credentials
    """
    pass

    credentials_list=[]

    def __init__(self,twitter_account,password):
        self.twitter_account =twitter_account
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        credentials.credentials_list.append(self)
    