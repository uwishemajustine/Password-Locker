#!/usr/bin/env python3.6
import random
from personinfo import personinfo
from credentials import credentials

def create_personinfo(login_name,username,password,email):
    '''
    Function to create a new personinfo
    '''
    new_personinfo = personinfo(login_name,username,password,email)
    return new_personinfo


def create_credentials(twitter_account,password):
    """
    Function to create new user credentials
    """
    new_credentials = credentials(twitter_account,password))
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