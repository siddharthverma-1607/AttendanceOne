from django.shortcuts import render
from io import BytesIO
from PIL import Image
import base64
import face_recognition
from django.views.decorators.csrf import csrf_exempt
from attendanceOne import settings
# Create your views here.


@csrf_exempt
def attendance(response, userid):
    if response.method == "POST":
        # f = open(settings.MEDIA_ROOT + '/webcamimages/userimage.jpg', 'wb')
        # f.write(request.raw_post_data)
        # f.close()
        return render(response, "markAttendance/markAttendance.html", {'userid': userid, 'attendeeImgSend': True})
    else:
        return render(response, "markAttendance/markAttendance.html", {'userid': userid})
