import pymongo


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
    connection = getConnection()
    # Database
    Database = connection.get_database('attendanceOneUser')

    userTable = Database.users

    queryObject = {
        'name': userObject.name,
        'email': userObject.email,
        'contact': userObject.contact,
        'organization': userObject.organization,
        'age': userObject.age,
        'password': userObject.password
    }

    queryId = userTable.insert_one(queryObject)
    print(queryId)
    print(queryId.inserted_id)
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
