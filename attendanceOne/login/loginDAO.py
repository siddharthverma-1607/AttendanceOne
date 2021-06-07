import pymongo
import base64


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
