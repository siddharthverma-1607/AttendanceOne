from django.shortcuts import render
from . import viewAttendanceDao as dao
# Create your views here.


def attendance(response):
    if response.method == "POST":
        attendanceResult = {}
        # view = response.POST.get("view")
        # download = response.POST.get("download")
        userId = response.POST.get("userId")
        # print("UserId - ", userId)

        attendanceDetails = dao.getAttendanceDetails(userId)
        # print(attendanceDetails)
        attendeeNames = attendanceDetails[0][0]
        attendeeId = attendanceDetails[0][1]
        dateDetail = attendanceDetails[1]
        attendanceRecord = []

        print("attendeeNames : ", attendeeNames)
        print("attendeeId : ", attendeeId)
        print("Date details : ", dateDetail)
        print(attendanceRecord, "\n\n")

        for date, record in dateDetail.items():
            # print(date, record)
            singleDayRecord = []
            singleDayRecord.append(date.replace(":", "/"))
            for id in attendeeId:
                if id in record:
                    # print("Yes")
                    singleDayRecord.append("Yes")
                else:
                    singleDayRecord.append("No")

            attendanceRecord.append(singleDayRecord)

        print(attendanceRecord)

        attendanceResult = {"state": "true", "attendanceID": attendeeId,
                            "attendeeName": attendeeNames, "attendanceRecord": attendanceRecord, "totalAttendees": len(attendeeId)}

        return render(response, "viewattendance/viewAttendance.html", attendanceResult)
    else:
        return render(response, "viewattendance/viewAttendance.html")
