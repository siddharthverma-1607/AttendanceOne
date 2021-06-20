import pymongo
import base64


from pymongo.collection import ReturnDocument


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


def authUser(email, password):
    """
    Used for authenticating user and redirecting to userSpace if authenticated.

    Parameters
    ----------
    arg1 : email
    arg2 : password

    Returns
    -------
    [string]
    Redirects to UserSpace or returns string on failed Authentication,
    """
    connection = getConnection()
    # Database
    Database = connection.get_database('attendanceOneUser')

    userTable = Database.users

    query = userTable.find_one({"email": email})

    if query == None:
        connection.close()
        return "Email is incorrect or does not exists"
    else:
        connection.close()
        if base64.b64encode(password.encode("utf-8")) == query["password"]:
            print(query["_id"])
            query["userId"] = query["_id"]
            return [True, query]
        else:
            return "Password is incorrect"


def sendAttendeeDetails(attendeeDetails):
    """
    Adds Attendee details to UserSpace.

    Parameters
    ----------
    attendeeDetails : {name, roll, img, userId}
        name - Attendee Name
        roll - Attendee Roll
        img - Attendee Img
        userId - User Id (Foreign Key for userSpace)

    Return
    ------
    query Object - New Attendee object

    """
    result = {}
    connection = getConnection()

    # Database
    Database = connection.get_database('attendanceOneUser')

    userSpaceTable = Database.userSpace

    """
    queryObject = {
        'userId': '',
        # userDetail : [ {image-1, roll-1, name-1, datePresent[]}, {image-1, roll-1, name-1, datePresent[]}, {image-1, roll-1, name-1, datePresent[]} ]
        'userDetails': [],
        # 'recordTaken' : [ date-1, date-2, date-3, date-N],
        'recordTaken': [],
        'userLimit': 10
    }"""

    query = userSpaceTable.find_one({'userId': attendeeDetails["userId"]})
    # print(query)
    # print(query["userDetails"])

    # updating to default set fields for new details
    userDetails = {
        'img': attendeeDetails['img'],
        'name': attendeeDetails['name'],
        'roll': attendeeDetails['roll']
    }
    userLimit = query["userLimit"]-1

    query = userSpaceTable.update_one(
        {'userId': attendeeDetails["userId"]},
        {'$set': {"userLimit": userLimit}, '$push': {"userDetails": userDetails}})

    if query != None:
        result = {'userAdded': True, 'userLimit': userLimit}

    connection.close()
    return result


def getUserLimit(userId):
    result = {}
    connection = getConnection()

    # Database
    Database = connection.get_database('attendanceOneUser')

    userSpaceTable = Database.userSpace

    query = userSpaceTable.find_one({'userId': userId})

    userLimit = query["userLimit"]

    if query != None:
        result = {'userLimit': userLimit}

    return result
