from django.shortcuts import render
from io import BytesIO
from PIL import Image
import base64
from django.views.decorators.csrf import csrf_exempt
from attendanceOne import settings
from . import markAttendanceDAO as dao
# Create your views here.


@csrf_exempt
def attendance(response, userid):
    if response.method == "POST":
        attendeeImg = response.POST.get('file')
        img = base64.b64decode(attendeeImg.split(',')[1])
        img = BytesIO(img)
        # img = Image.open(img)
        # buffer = BytesIO()
        # img.save(buffer, format="JPEG")
        # print(img)
        print(type(img))
        # img.show()
        # print(img[0:30])

        checkAttendee = dao.attendeePresent(userid, img)
        if checkAttendee[0]:
            print("Attendance Marked")
        else:
            print("Who are you?!")

        return render(response, "markAttendance/markAttendance.html", {'userid': userid, 'attendeeImgSend': True})
    else:
        return render(response, "markAttendance/markAttendance.html", {'userid': userid})
