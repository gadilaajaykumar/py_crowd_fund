from pymongo import MongoClient
from bson.objectid import ObjectId


class User:
    # initial fields
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    crowdFundingDatabase = client.CrowdFundingDatabase
    userCollection = crowdFundingDatabase.user

    # Create User - Registration
    def create_user(self, firstName, lastName, email, password, phoneNumber):
        newUserDocument = {
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'password': password,
            'phoneNumber': phoneNumber
        }
        checkDocument = {
            'email': email,
        }
        if not self.userCollection.find_one(checkDocument):
            return self.userCollection.insert_one(newUserDocument).inserted_id
        else:
            return False

    # Delete UserByEmail - Remove User
    def deleteUserByEmail(self, userEmail):
        deleteOperation = {
            'email': userEmail
        }
        return self.crowdFundingDatabase.userCollection.delete_one(deleteOperation)

    # Find One User - Login
    def findOneUser(self, email, password):
        findOneUserDocument = {
            'email': email,
            'password': password
        }
        userData = self.userCollection.find(findOneUserDocument)
        userDocumentation = {}
        for property in userData:
            userDocumentation = property

        return userDocumentation
