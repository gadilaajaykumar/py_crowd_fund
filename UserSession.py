# Class Session: to store current user information
class UserSession:

    def __init__(self, _id, firstName, lastName, email, password, phoneNumber):
        self.userId = _id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phoneNumber = phoneNumber

    def displayUser(self):
        print(
            "> FirstName: {}\n LastName: {} \n> Email: {}\n > PhoneNumber: {}\n".format(self.firstName, self.lastName,
                                                                                        self.email,
                                                                                        self.phoneNumber))

