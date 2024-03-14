/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable @typescript-eslint/no-unused-vars */
import React, { useEffect, useState } from "react";
import { getInformation } from "../../Helper/static";
import { get_student_course_attendance, update_attendance } from "../../API/student";

interface attendance {
    ItemType: string;
    UserId: string;
    Attendance: string;
    ItemId: string;
    CourseId: string;
}

interface AttendanceRecord {
    from: string;
    to: string;
    status: 'present' | 'absent' | null;
}

interface AttendanceDateRecord {
    [date: string]: AttendanceRecord;
}

type AttendanceObject = [string, string, AttendanceDateRecord];

const mockdata = [
    ["1", "John Doe", { "2022-01-01": { "from": "08:00", "to": "10:00", "status": "present" } }]
];

function StudentAttendanceComponent() {
    const [attendance, setAttendance] = useState<AttendanceObject[] | null>(null);
    const [loadingAttendance, setLoadingAttendance] = useState(true);

    const queryParams = new URLSearchParams(window.location.search);
    const course_id = queryParams.get('course_id') ?? "";
    const course_name = queryParams.get('course_name');
    const username = getInformation()["cognito:username"];

    useEffect(() => {
        // Get the student's courses
        get_student_course_attendance(username, course_id)().then((response) => {
            response.json().then(data => {
                if (response.status === 200) {
                    setAttendance(data);
                    console.log(data);
                } else {
                    setAttendance([]);
                }
                setLoadingAttendance(false);
            });
        });
    }, []);

    const renderAttendance = (item: AttendanceObject) => {
        const [userId, username, dates] = item;
        if (!dates) return null;
        const itemId = getInformation()["cognito:username"] + course_id;
        return Object.entries(dates).map(([date, record], index) => {
            return (
                <tr key={`${userId}-${date}-${index}`}>
                    <td>{username}</td>
                    <td>{date}</td>
                    <td>{`${record.from} - ${record.to}`}</td>
                    <td>{record.status}</td>
                    <td><button className="btn btn-primary" onClick={() => updateAttendance(itemId, { [date]: { "from": record.from, "to": record.to, "status": "present" } })}>Present</button></td>
                    <td><button className="btn btn-danger" onClick={() => updateAttendance(itemId, { [date]: { "from": record.from, "to": record.to, "status": "absent" } })}>Absent</button></td>
                </tr>
            );
        });
    };

    const updateAttendance = async (itemId: string, attendance: AttendanceDateRecord) => {
        try {
            const response: Response = await update_attendance(itemId, attendance, course_id)();
            if (response.ok && await response.json()) {
                alert("Attendance updated successfully");
                window.location.reload();
            } else {
                alert("Error updating attendance");
            }
        } catch (error: any) {
            console.error("Error updating attendance", error);
            alert("Error updating attendance");
        }
    };

    return (
        <div className="container-fluid p-0">
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title">Attendance of Student for course {course_name} with id {course_id}
                            </h5>
                            <h6 className="card-subtitle text-muted">The attendance of the student can be found in
                                the table below. </h6>
                        </div>
                        <div className="card-body">
                            <table id="datatables-responsive" className="table table-striped" style={{ width: "100%" }}>
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Date</th>
                                        <th>Time</th>
                                        <th>Attendance</th>
                                        <th>Present</th>
                                        <th>Absent</th>
                                    </tr>
                                </thead>
                                <tbody id="data-student-attendance">
                                    {loadingAttendance ? (
                                        <tr><td>Loading...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
                                    ) : attendance && attendance.length > 0 ? (
                                        attendance.map(att => renderAttendance(att))
                                    ) : (
                                        <tr><td>No attendance found</td><td></td><td></td><td></td><td></td><td></td></tr>
                                    )}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
export default StudentAttendanceComponent;
