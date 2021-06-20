import pymongo
import base64
from io import BytesIO
import face_recognition
import numpy as np


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


def getAttendeeDetails(userId):
    """
    Gets Attendee details from UserSpace.

    Parameter
    ------
    userID - Foreign Key

    Returns
    ----------
    attendeeDetails : {name, roll, img, userId}
        name - Attendee Name
        roll - Attendee Roll
        img - Attendee Img
        userId - User Id (Foreign Key for userSpace)

    """
    connection = getConnection()

    # Database
    Database = connection.get_database('attendanceOneUser')

    userSpaceTable = Database.userSpace

    query = userSpaceTable.find_one({'userId': userId})

    result = query
    connection.close()
    return result


def attendeePresent(userId, webcamImg):
    result = [False]

    # Getting attendees details
    userAttendeeDetails = getAttendeeDetails(userId)
    i = 1

    # Load Webcam image to find faces in
    test_image = face_recognition.load_image_file(webcamImg)

    # Encoding face of Webcam image
    face_encoding = face_recognition.face_encodings(
        test_image)[0]

    print(type(face_encoding))

    # Stores known face encodeing from userSpaceDB
    known_face_encodings = []
    # Stores known face names of attendee from userSpaceDB
    known_face_names = []
    # Stores known face uniqueID of attendee from userSpaceDB
    known_face_id = []

    for attendee in userAttendeeDetails['userDetails']:
        print("Attendee No. ", i)
        i += 1

        known_face_names.append(attendee['name'])
        known_face_id.append(attendee['roll'])

        # attendeeImage = base64.b64decode(attendee['img'])
        attendeeImage = attendee['img']
        # attendeeImage = BytesIO(attendeeImage)
        # print(attendeeImage)

        # attendeeImage = face_recognition.load_image_file(attendeeImage)
        # encoding = face_recognition.face_encodings(attendeeImage)[0]

        encoding = np.fromiter(attendeeImage, dtype=np.double)

        known_face_encodings.append(encoding)

    # Find if face is present
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    if True in matches:
        result[0] = True
        matches.reverse()
        first_match_index = (len(matches) - matches.index(True) - 1)
        name = known_face_names[first_match_index]
        attendeeID = known_face_id[first_match_index]
        print(name, attendeeID)

    return result
