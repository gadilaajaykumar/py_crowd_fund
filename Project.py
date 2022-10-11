from pymongo import MongoClient
from bson.objectid import ObjectId


class Project:
    # initial fields
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    crowdFundingDatabase = client.CrowdFundingDatabase
    projectCollection = crowdFundingDatabase.project

    # Create Project
    def createProject(self, userId, title, details, totalTarget, startDate, endDate):
        newProjectDocument = {
            'userId': ObjectId(userId),
            'title': title,
            'details': details,
            'total': totalTarget,
            'startDate': startDate,
            'endDate': endDate
        }
        return self.projectCollection.insert_one(newProjectDocument).inserted_id

    # View All Project
    def findAllProject(self, userId):
        allProjectsDictionry = {}
        for project in self.projectCollection.find({'userId': userId}):
            projectDictionry = {
                'title': project['title'],
                'details': project['details'],
                'total': project['total'],
                'startDate': project['startDate'],
                'endDate': project['endDate']
            }
            allProjectsDictionry[projectDictionry['title']] = projectDictionry
        return allProjectsDictionry

    def findOneProject(self, userId, title):
        return self.projectCollection.find_one({
            'userId': userId,
            'title': title
        })

    # Delete One Project For One User
    def deleteOneProject(self, userID, projectTitle):
        return self.projectCollection.delete_one({
            'userId': ObjectId(userID),
            'title': projectTitle
        })

    # Delete All Project for One User
    def deleteAllProject(self, userID):
        return self.projectCollection.delete({
            'userId': ObjectId(userID),
        })
