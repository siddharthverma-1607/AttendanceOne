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


def getAttendanceDetails(userId):
    result = []
    attendees = [[], []]
    connection = getConnection()

    # Database
    Database = connection.get_database('attendanceOneUser')

    userSpaceTable = Database.userSpace

    query = userSpaceTable.find_one({'userId': userId})

    for item in query['userDetails']:
        attendees[0].append(item['name'])
        attendees[1].append(item['roll'])

    result.append(attendees)
    result.append(query['recordTaken'])
    connection.close()
    return result
