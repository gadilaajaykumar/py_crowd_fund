#!/bin/usr/python

from pymongo import MongoClient
from bson.objectid import ObjectId
from Package.Helpers.Helper import Helper
from Package.Helpers.UserSession import UserSession
from Package.Modals.Project import Project
from Package.Modals.User import User

while True:
    print('> Crowd Funding Application')
    print('> Registration - Press (1)')
    print('> Login - Press (2)')
    print('> Exit - Press (3)')
    # Classes
    helper = Helper()
    user = User()
    project = Project()
    # Reader Input
    inputReader = int(input('> Your Choice: '))
    if inputReader == 1:
        while True:
            print('> ENTER YOUR DATA')
            firstName = input('> FirstName: ')
            lastName = input('> LastName:')
            email = input('> Email(please enter a valid email): ')
            if not helper.email_validator(email):
                print('> PLEASE ENTER A VALID EMAIL.')
                continue
            password = input('> Password: ')
            confirmPassword = input('> Confirm Password: ')
            if not helper.password_confirmation(password, confirmPassword):
                print('> PLEASE ENTER SAME PASSWORD')
                continue
            phoneNumber = input('> Phone Number (please enter a valid phone number): ')
            if not helper.phone_number_validator(phoneNumber):
                print('> PLEASE ENTER VALID PHONE NUMBER')
                continue
            status = user.create_user(firstName, lastName, email, password, phoneNumber)
            if not status:
                print('> User Already Registered')
            else:
                print("> CONGRATULATION")
            break
    elif inputReader == 2:
        print('> USER LOGIN')
        while True:
            email = input('> email: ')
            password = input('> Password: ')
            userdata = user.findOneUser(email, password)
            print("result:", userdata)
            if not userdata:
                print('> Failed Login.')
            else:
                userID = userdata['_id']
                userFirstName = userdata['firstName']
                userLastName = userdata['lastName']
                userEmail = userdata['email']
                userPassword = userdata['password']
                userPhoneNumber = userdata['phoneNumber']
                userSession = UserSession(userID, userFirstName, userLastName, userEmail, userPassword, userPhoneNumber)
                while True:
                    print('> Create Project - press (0)')
                    print('> Delete Project - Press (1)')
                    print('> View One Project - press (2)')
                    print('> View All Projects - press (3)')
                    print('> Exit - press (4)')
                    userChoice = int(input('> your choice: '))
                    if userChoice == 0:
                        title = input('> project title: ')
                        details = input('> project details: ')
                        total = int(input('> project total target: '))
                        startDate = input('> project start date: ')
                        endDate = input('> project end data: ')
                        projectStatus = project.createProject(userSession.userId, title, details, total, startDate,
                                                              endDate)
                        if projectStatus:
                            print('> Project Created Successfully...')
                        else:
                            print('> Sorry Project Creation Failed...')
                    elif userChoice == 1:
                        title = input('> enter project title: ')
                        status = project.deleteOneProject(userSession.userId, title)
                        if status:
                            print('> Project Deleted Successfully...')
                        else:
                            print('> Project Deletion Failed...')
                    elif userChoice == 2:
                        title = input('> enter project title: ')
                        status = project.findOneProject(userSession.userId, title)
                        if status:
                            print(status)
                            print('> Project Deleted Successfully...')
                        else:
                            print(status)
                            print('> Project Deletion Failed...')
                    elif userChoice == 3:
                        print(project.findAllProject(userSession.userId))
                    elif userChoice == 4:
                        break
    elif inputReader == 3:
        break
    else:
        print('> Sorry, Enter Valid Input\n')
