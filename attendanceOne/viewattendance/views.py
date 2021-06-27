from django.shortcuts import render
from . import viewAttendanceDao as dao
# Create your views here.


def attendance(response):
    if response.method == "POST":
        view = response.POST.get("view")
        download = response.POST.get("download")
        userId = response.POST.get("userId")
        # print("UserId - ", userId)

        attendanceDetails = dao.getAttendanceDetails(userId)
        # print(attendanceDetails)
        attendeeNames = attendanceDetails[0][0]
        attendeeId = attendanceDetails[0][1]
        dateDetail = attendanceDetails[1]
        dateTaken = []
        attendanceRecord = [["No"] * len(attendeeNames)] * len(dateDetail)

        attendanceRecordIndex = 0
        for date, record in dateDetail.items():

            dateTaken.append(date)
            for id in attendeeId:
                if id in record:
                    index = attendeeId.index(id)
                    print("Yes", index)
                    attendanceRecord[attendanceRecordIndex][index] = "Yes"
                    print(attendanceRecord[attendanceRecordIndex])
                else:
                    index = attendeeId.index(id)
                    print("No", index)
            print(attendanceRecord)
            attendanceRecordIndex += 1

        print(dateDetail)
        print(attendanceRecord)

        return render(response, "viewattendance/viewAttendance.html")
    else:
        return render(response, "viewattendance/viewAttendance.html")
