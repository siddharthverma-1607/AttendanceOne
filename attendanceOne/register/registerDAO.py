import pymongo
from datetime import date, datetime


def getConnection():
    """
    Creates a Connection with the MongoDB

    Returns
    -------
    client object
        client object is used to connect to Online Mongo DB
    """
    # *********************** Mongo DB Configs ***********************
    # Replace your URL here. Don't forget to replace the password.
    connection_url = "mongodb+srv://attendanceOne:RAykugYVqUjLEuP9@attendanceonecluster.sbwzi.mongodb.net/attendanceOneUser?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    return client


def addNewUser(userObject):
    """
    Adds new User To User DB, Creates UserSpace row in userSpace DB.

    Parameters
    ----------
    arg1 : Model Object
        Model Object will hold all data required for seacrhing from to MongoDB.

    """
    connection = getConnection()
    # Database
    Database = connection.get_database('attendanceOneUser')

    userTable = Database.users

    #  calculating user age
    born = datetime.strptime(
        userObject.dob, '%Y-%m-%d')
    print(born)
    today = date.today()
    age = today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))

    queryObject = {
        'name': userObject.name,
        'email': userObject.email,
        'contact': userObject.contact,
        'organization': userObject.organization,
        'dob': born,
        'age': age,
        'socialLinks': userObject.socialLinks,
        'password': userObject.password
    }

    # Inserting into userDB
    queryId = userTable.insert_one(queryObject)
    print(queryId)
    print(queryId.inserted_id)
    connection.close()
    # Creating UserSpace in UserSpace Table
    createUserSpace(queryId)


def createUserSpace(queryId):
    """
    Creates UserSpace Document in UserSpaceDB with userId as foreign Key from UserDB.

    Parameters
    ----------
    arg1 : userID
        UserID is object ID created when inserted into User DB. Will be used as foreign key.
    """
    connection = getConnection()

    # Database
    Database = connection.get_database('attendanceOneUser')

    userSpaceTable = Database.userSpace

    queryObject = {
        'userId': queryId.inserted_id,
        # userDetail : [ {image-1, roll-1, name-1, datePresent[]}, {image-1, roll-1, name-1, datePresent[]}, {image-1, roll-1, name-1, datePresent[]} ]
        'userDetails': [],
        # 'recordTaken' : [ date-1, date-2, date-3, date-N],
        'recordTaken': [],
        'userLimit': 10
    }

    query = userSpaceTable.insert_one(queryObject)
    connection.close()


def searchUser(userObject):
    """
    This method will search if user already exists in user DB.

      Parameters
      ----------
      arg1 : Model Object
          Model Object will hold all data required for submiting help query to MongoDB.

      Returns
      -------
      Boolean
      True : User does not exists
      False : User already exists
    """
    connection = getConnection()
    Database = connection.get_database('attendanceOneUser')

    userTable = Database.users

    queryObject = {
        'email': userObject.email
    }

    query = userTable.find_one(queryObject)

    if query == None:
        return True
    else:
        return False
