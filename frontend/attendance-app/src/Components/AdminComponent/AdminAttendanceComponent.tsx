import React, { useEffect, useState } from "react";
import { get_all_course_attendance } from "../../API/teacher";
import { get_course, update_course } from "../../API/course";
import { update_attendance } from "../../API/student";


interface AttendanceRecord {
    from: string;
    to: string;
    status: 'present' | 'absent' | null;
}

interface AttendanceDateRecord {
    [date: string]: AttendanceRecord;
}

type AttendanceObject = [string, string, AttendanceDateRecord];

/**
 * Renders the admin attendance component.
 * This component displays the attendance of students for a specific course.
 * It also allows the admin to create a new lesson for the course.
 */
function AdminAttendanceComponent() {
    const [attendance, setAttendance] = useState<AttendanceObject[] | null>(null);
    const [loadingAttendance, setLoadingAttendance] = useState(true);
    const [lessonDate, setLessonDate] = useState("");
    const [lessonStartTime, setLessonStartTime] = useState("");
    const [lessonEndTime, setLessonEndTime] = useState("");

    const queryParams = new URLSearchParams(window.location.search);
    const course_id = queryParams.get('course_id') ?? "";
    const course_name = queryParams.get('course_name') ?? "";

    useEffect(() => {
        // Get the student's courses
        get_all_course_attendance(course_id)().then((response) => {
            response.json().then(data => {
                if (response.status === 200) {
                    setAttendance(data);
                } else {
                    setAttendance(null);
                }
                setLoadingAttendance(false);
            });
        });
    }, [course_id]);

    const renderAttendance = (item: AttendanceObject) => {
        const [userId, username, dates] = item;
        if (!dates) return null;
        const itemId = userId + course_id;
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

    const createLesson = async (event: React.FormEvent<HTMLFormElement>): Promise<void> => {
        event.preventDefault();

        get_course(course_id)().then((response) => {
            response.json().then(async data => {
                if (response.status === 200) {
                    let classes;
                    if (data.Classes) {
                        classes = data.Classes;
                    } else {
                        classes = {};
                    }
                    classes[lessonDate] = { from: lessonStartTime, to: lessonEndTime };
                    try {
                        // Update the course with the new lesson
                        const response: Response = await update_course(course_id, course_name, "1", classes)();
                        if (response.ok && await response.json()) {
                            alert("Lesson created successfully, it will not show up until a student enrolls in the course");
                            window.location.reload();
                        } else {
                            alert("Error creating lesson");
                        }
                    } catch (error: any) {
                        console.error("Error creating lesson", error);
                        alert("Error creating lesson");
                    }
                } else {
                    console.error("Error");
                    alert("Error creating lesson");
                }
            });
        });
    }

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
                            <h5 className="card-title">Attendance of Course {course_name} with id {course_id} (Seen as Admin)
                            </h5>
                            <h6 className="card-subtitle text-muted">The attendance of the students for this course can be found in
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
                                    {loadingAttendance && attendance && attendance.length > 0 ? (
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
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title">Create lesson</h5>
                            <h6 className="card-subtitle text-muted">Create a new lesson for the course. All
                                registered students for this course will be set to empty as standard.</h6>
                        </div>
                        <div className="card-body">
                            <form id="create-lesson" onSubmit={createLesson}>
                                <div className="mb-3">
                                    <label htmlFor="lesson-date" className="form-label">Date</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="lesson-date"
                                        pattern="\d{4}-\d{2}-\d{2}"
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
                                        pattern="[0-2][0-9]:[0-5][0-9]"
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
                                        pattern="[0-2][0-9]:[0-5][0-9]"
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
export default AdminAttendanceComponent;