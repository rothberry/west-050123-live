from lib.models.hat import Hat
from lib.models.user import User
from lib.helpers import term_wrap, star_line, center_string_stars
from os import system
from ipdb import set_trace

""" 
  Testing!

  When testing databases, we usually have one for test data
  One for the Development
  One for the Public, Production Environment

  Why would we want to separate these 3(ish) dbs?
  - Same methodolgy as git branches
  - The public is interacting with the Production db,
  - The Devs have an active db for beta-testing, new features
  - The Test Db/environment, only becomes active while the tests are running

"""

if __name__ == "__main__":
    system("clear")
    term_wrap("Console Testing")
    u1 = User()
    u2 = User("cARLA")

    print(u1.username == "")
    print(u2.username == "cARLA")

    