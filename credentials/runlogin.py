#!/usr/bin/env python3.6

from credentials import credentials
from personinfo import personinfo 
import random


def create_personinfo(login_name,username,password,email):
    '''
    Function to create a new personinfo
    '''
    new_personinfo = create_personinfo(login_name,username,password,email)
    return new_personinfo


def create_credentials(twitter_account,password):
    """
    Function to create new credentials
    """
    new_credentials = credentials("alsenj20@yahoo.com","199b")
    return new_credentials

def save_personinfo(personinfo):
    """
    Function to save personinfo
    """
    personinfo.save_personinfo_details()

def save_credentials(credentials):
    """
    Function to save credentials
    """
    credentials.save_credentials() 


def delete_personinfo(personinfo):
    """
    Function to delete a personinfo
    """
    personinfo.delete_personinfo()

def delete_credentials(credentials):
    """
    Function to delete all credentials
    """
    credentials.delete_credentials()


def find_personinfo(username):
    '''
    Function that finds a personinfo by username and returns the personinfo
    '''
    return personinfo.find_by_username(username)

def find_credentials(twitter_account):
    '''
    Function that finds a credentials by twitter_account and returns the credentials
    '''
    return credentials.find_by_twitter_account(twitter_account)


def check_existing_personinfo(username):
    '''
    Function that check if a personinfo exists with that username and return a Boolean
    '''
    return personinfo.personinfo_exist(username)

def check_existing_credentials(twitter_account):
    '''
    Function that check if a credentials exists with that twitter_account and return a Boolean
    '''
    return credentials.credentials_exist(twitter_account)   


def display_personinfo():
    '''
    Function that returns all the saved personinfo
    '''
    return personinfo.display_personinfo()

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return credentials.display_credentials()    


def main():

    print("Welcome to your Password Locker, choose your path from the list of allowed actions")
    username = input()
    print("\n")
    print(f"Hello {username}.what would you like to do?")
    while True:
        print("\nUse these short codes below:")
        print("-" * 12)
        print("Use these short codes : ca - create a new account, gp - generate password, cp - create your password, ex -exit the account, da- display account")

        short_code = input().lower()

        if short_code == 'ca':
            print("New account")
            print("-" * 10)

            print("\nEnter login_name ...")
            login_name = input()

            print("\nEnter username ...") 
            username = input()

            print("\nEnter a password ...")
            password = input()

            print("Enter an email ...")
            email = input()

            save_personinfo(create_personinfo(login_name, username, password, email)) 
            save_credentials(create_credentials(twitter_account, password))
            print('\n')
            print(f"A new {site} Account by {login_name} {username} {password} {email} has successfully been created")  
            print(f" The twitter_account is {twitter_account} and the password is {password}")
            print('\n')


        elif short_code == "gp":
            print("\n create another account")
            print("-"*15)
            print("enter the account you created before")
            site = input()
            print(f"So you want to create a {site}?")

            print("First name ....")
            first_name = input()

            print("Last name ...", )
            last_name = input()

            print("Phone number ...")
            phone_number = input()

            print("Email address ...")
            email_address = input()

            print("Enter username ... Hint: a secure password will be generated for you...")
            user_name = input()

            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            password = "".join(random.sample(s, 8))
   
            save_personinfo(create_personinfo(login_name, username, password, email)) 
            save_credentials(create_credentials(twitter_account, password))
            print('\n')
            print(f"A new {site} Account by {login_name} {username} {password} {email} has successfully been created")  
            print(f" The twitter_account is {twitter_account} and the password is {password}")
            print('\n')
  

        elif short_code == "ex":
            print(":/ See you soon then...")
            break
        else:
            print(" :( Only key in the allowed actions !!")


       


if __name__ == '__main__':

    main()