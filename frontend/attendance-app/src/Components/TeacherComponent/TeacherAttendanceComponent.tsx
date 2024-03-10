import React, { useEffect, useState } from "react";
import { getInformation } from "../../Helper/static";
import { get_all_course_attendance } from "../../API/teacher";
import { get_course, update_course } from "../../API/course";

interface AttendanceRecord {
    from: string;
    to: string;
    status: 'present' | 'absent' | string;
}

interface Attendance {
    [date: string]: AttendanceRecord;
}

interface AttendanceObject {
    ItemId: string;
    CourseId: string;
    UserId: string;
    ItemType: 'Attendance';
    Attendance: Attendance;
}

let attendance_object = {
    'ItemId': '992b162a-cd9c-4205-b471-4e3a2830309e#1',
    'CourseId': '1',
    'UserId': '992b162a-cd9c-4205-b471-4e3a2830309e',
    'ItemType': 'Attendance',
    'Attendance': {
        '2022-01-01': {
            'from': '09:00',
            'to': '12:00',
            'status': 'present'
        }
    }
}

function TeacherAttendanceComponent() {
    const [attendance, setAttendance] = useState<AttendanceObject[] | null>(null);
    const [loadingAttendance, setLoadingAttendance] = useState(true);
    const [lessonDate, setLessonDate] = useState("");
    const [lessonStartTime, setLessonStartTime] = useState("");
    const [lessonEndTime, setLessonEndTime] = useState("");

    const queryParams = new URLSearchParams(window.location.search);
    const course_id = queryParams.get('course_id') ?? "";
    const course_name = queryParams.get('course_name') ?? "";
    const username = getInformation()["cognito:username"];

    useEffect(() => {
        // Get the student's courses
        get_all_course_attendance(course_id)().then((response) => {
            response.json().then(data => {
                if (response.status === 200) {
                    console.log(data);
                    data = [attendance_object];
                    setAttendance(data);
                } else {
                    setAttendance([]);
                }
                setLoadingAttendance(false);
            });
        });
    }, [course_id]);

    const renderAttendance = (attendanceObj: AttendanceObject) => {
        const entries = Object.entries(attendanceObj.Attendance);
        return entries.map(([date, record], index) => (
            <tr key={index}>
                <td>{date}</td>
                <td>{`${record.from} - ${record.to}`}</td>
                <td>{record.status}</td>
                <td><button className="btn btn-primary">Change</button></td>
            </tr>
        ));
    };

    const createLesson = async (event: React.FormEvent<HTMLFormElement>): Promise<void> => {
        event.preventDefault();

        get_course(course_id)().then((response) => {
            response.json().then(async data => {
                if (response.status === 200) {
                    let classes = data.Classes;
                    classes[lessonDate] = { from: lessonStartTime, to: lessonEndTime };
                    try {
                        // Update the course with the new lesson
                        const response: Response = await update_course(course_id, course_name, "1", classes)();
                        if (response.ok && await response.json()) {
                            alert("Lesson created successfully");
                            window.location.reload();
                        } else {
                            alert("Error creating lesson");
                        }
                    } catch (error: any) {
                        console.error("Error creating lesson", error);
                        alert("Error creating lesson");
                    }
                } else {
                    console.log("Error");
                }
            });
        });
    }

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
                                        <th>Date</th>
                                        <th>Time</th>
                                        <th>Attendance</th>
                                        <th>Change</th>
                                    </tr>
                                </thead>
                                <tbody id="data-student-attendance">
                                    {loadingAttendance ? (
                                        <tr><td>Loading...</td><td></td><td></td><td></td></tr>
                                    ) : attendance && attendance.length > 0 ? (
                                        attendance.map(att => renderAttendance(att))
                                    ) : (
                                        <tr><td>No attendance found</td><td></td><td></td><td></td></tr>
                                    )}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title">Create lesson</h5>
                            <h6 className="card-subtitle text-muted">Create a new lesson for the course. All
                                registered students for this course will be set to absent as standard.</h6>
                        </div>
                        <div className="card-body">
                            <form id="create-lesson" onSubmit={createLesson}>
                                <div className="mb-3">
                                    <label htmlFor="lesson-date" className="form-label">Date</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="lesson-date"
                                        data-mask="00/00/0000"
                                        placeholder="YYYY-MM-DD"
                                        required
                                        value={lessonDate}
                                        onChange={(e) => setLessonDate(e.target.value)}
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="lesson-start-time" className="form-label mb-0">Start time</label>
                                    <input type="text"
                                        className="form-control"
                                        id="lesson-start-time"
                                        data-mask="00:00"
                                        placeholder="HH:MM"
                                        required
                                        value={lessonStartTime}
                                        onChange={(e) => setLessonStartTime(e.target.value)}
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="lesson-end-time" className="form-label mb-0">End time</label>
                                    <input type="text"
                                        className="form-control"
                                        id="lesson-end-time"
                                        data-mask="00:00"
                                        placeholder="HH:MM"
                                        required
                                        value={lessonEndTime}
                                        onChange={(e) => setLessonEndTime(e.target.value)}
                                    />
                                </div>
                                <button type="submit" className="btn btn-primary">Create lesson</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
export default TeacherAttendanceComponent;