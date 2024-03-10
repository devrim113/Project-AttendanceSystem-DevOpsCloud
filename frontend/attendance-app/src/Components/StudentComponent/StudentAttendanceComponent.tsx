import React, { useEffect, useState } from "react";
import { getInformation } from "../../Helper/static";
import { get_student_course_attendance } from "../../API/student";

interface attendance {
    ItemType: string;
    UserId: string;
    Attendance: string;
    ItemId: string;
    CourseId: string;
}

function StudentAttendanceComponent() {
    const [attendance, setAttendance] = useState<attendance[] | null>(null);
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
                    console.log(data);
                    setAttendance(data);
                } else {
                    setAttendance([]);
                }
                setLoadingAttendance(false);
            });
        });
        console.log(attendance);
    }, []);

    return (
        <div className="container-fluid p-0">
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title">Attendance of Student for course {course_name} <span
                                id="course-name"></span> with id <span id="course-id"></span>
                            </h5>
                            <h6 className="card-subtitle text-muted">The attendance of the student can be found in
                                the table below. </h6>
                        </div>
                        <div className="card-body">
                            <table id="datatables-responsive" className="table table-striped" style={{ width: "100%" }}>
                                <thead>
                                    <tr>
                                        <th>Date</th>
                                        <th>Time</th>
                                        <th>Attendance</th>
                                        <th>Change</th>
                                    </tr>
                                </thead>
                                <tbody id="data-student-attendance">
                                    {loadingAttendance ? <tr><td>Loading...</td><td></td><td></td><td></td></tr> : attendance && attendance.length > 0 ? attendance.map((att, index) => (
                                        <tr key={index}>
                                            <td>{att.ItemId}</td>
                                            <td>{att.CourseId}</td>
                                            <td>{att.Attendance}</td>
                                            <td><button className="btn btn-primary">Change</button></td>
                                        </tr>
                                    )) : <tr><td>No attendance found</td><td></td><td></td><td></td></tr>
                                    }
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
