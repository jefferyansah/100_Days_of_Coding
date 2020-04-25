#!
#pw.py This is a password manager app

PASSWORDS = {'email': 'fegpeor349jvfk/feit3n04vmwjm',
             'password': 'JVSDkjskljgeirjkgnvslkfls',
             'luggage': '124534'
             }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')

account = sys.argv[1] # command line argument for the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is not account name ' + account)
