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
        # 'facebook_link':'#',
        # 'twitter_link':'#',
        # 'linkdin_link' : '#',
        # 'whatsapp_link' : '#',
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
