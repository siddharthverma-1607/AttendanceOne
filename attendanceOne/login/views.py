from django.shortcuts import render
from . import loginDAO as dao
from io import BytesIO
from PIL import Image
import face_recognition
# Create your views here.


def login(response):
    """
    Vaildates Login and directs to User Space if validated
    Or 
    back to login.
    """
    if response.method == "POST":
        email = response.POST.get("email")
        password = response.POST.get("pwd")
        result = dao.authUser(email, password)

        if result[0] == True:
            # print(result[1])
            result[1]["auth"] = True
            return render(response, "login/setCookies.html", result[1])

        else:
            return render(response, "login/login.html", {"result": result})
    else:
        return render(response, "login/login.html")


def userSpace(response):
    return render(response, "login/userSpace.html")


def addUser(response):

    if response.method == "POST":
        userId = response.POST.get("userId")
        limit = dao.getUserLimit(userId)
        print(limit)
        if limit['userLimit'] == 0:
            return render(response, "login/addUser.html", limit)
        else:
            name = response.POST.get("userName")
            roll = response.POST.get("roll")
            img = response.FILES['img']
            print(img)

            # Method 1
            attendeeImg = b''
            for i in img:
                attendeeImg += i
            attendeeImg = BytesIO(attendeeImg)
            attendeeImg = face_recognition.load_image_file(attendeeImg)
            encoding = face_recognition.face_encodings(attendeeImg)[0].tolist()
            print(encoding)

            # Method 2
            # img = Image.open(img)
            # image_bytes = BytesIO()
            # img.save(image_bytes, format='JPEG')
            # img.show()

            # Method 1
            attendeeDetails = {'name': name, 'roll': roll,
                               'img': encoding, 'userId': userId}

            # Method 2
            # attendeeDetails = {'name': name, 'roll': roll,
            #                    'img': image_bytes.getvalue(), 'userId': userId}

            query = dao.sendAttendeeDetails(attendeeDetails)
            # print(query)

            return render(response, "login/addUser.html", query)
    else:
        return render(response, "login/addUser.html")


def deleteAccount(response):
    return render(response, "login/deleteAccount.html")


def deleteUser(response):
    return render(response, "login/deleteUser.html")


def shareLink(response):
    return render(response, "login/shareLink.html")


def updateUser(response):
    return render(response, "login/updateUser.html")
