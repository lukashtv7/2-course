# -*- coding: utf-8 -*-
"""Example Git and GitHub teamwork

TODO:
    * Some commits
    * Pull and Pushs
    * Merge from develop to main
"""
PASSWORD = 1234
USER_NAME = "Dmitry"

ROOT_PASSWORD = 4321
def user_info(id):
    print("\nUser",str(id)+":", USER_NAME, "have pass", PASSWORD)
    print("Root have pass", ROOT_PASSWORD)

user_info(1)