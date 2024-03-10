import React, { useEffect, useState } from "react";
import { getInformation } from "../../Helper/static";
import { enlist_student_course, get_all_courses, get_student_course_names } from "../../API/student";

// Define a TypeScript interface for the course
interface Courses {
    [key: number]: string;
}

interface bigCourse {
    Classes: object;
    CourseName: string;
    DepartmentId: string;
    ItemId: string;
    ItemType: string;
}

function StudentComponent() {
    const [courses, setCourses] = useState<Courses[] | null>(null);
    const [allcourses, setAllCourses] = useState<bigCourse[] | null>(null);
    const [loadingCourses, setLoadingCourses] = useState(true);
    const [loadingAllCourses, setLoadingAllCourses] = useState(true);
    const username = getInformation()["cognito:username"];

    useEffect(() => {
        // Get the student's courses
        get_student_course_names(username)().then((response) => {
            response.json().then(data => {
                if (response.status === 200) {
                    setCourses(data);
                } else {
                    setCourses([]);
                }
                setLoadingCourses(false);
            });
        });

        // Get all the courses
        get_all_courses()().then((response) => {
            response.json().then(data => {
                if (response.status === 200 && data.length > 0) {
                    setAllCourses(data);
                } else {
                    setAllCourses([]);
                }
                setLoadingAllCourses(false);
            });
        });
    }, []);

    return (
        <div className="container-fluid p-0">
            <h1 className="h3 mb-3">Student Dashboard</h1>
            <p className="mb-3">
                Welcome to the student dashboard. Here you can view all the courses you have
                registered for and view your attendance for each course by clicking on a
                course.
            </p>
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title">Courses</h5>
                            <h6 className="card-subtitle text-muted">These are all the courses you have enrolled in.</h6>
                        </div>
                        <div className="card-body">
                            <table className="table table-striped" style={{ width: "100%" }}>
                                <thead>
                                    <tr>
                                        <th>Course Name</th>
                                        <th>View</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {loadingCourses ? (
                                        <tr><td>Loading...</td><td></td></tr>
                                    ) : courses ? (
                                        Object.entries(courses).map(([course_id, course_name], index) => (
                                            <tr key={index}>
                                                <td>{String(course_name)}</td>
                                                <td>
                                                    <button className="btn btn-primary" onClick={() => window.location.href = `/studentattendance?course_id=${encodeURIComponent(String(course_id))}&course_name=${encodeURIComponent(course_name.toString())}`}>View</button>
                                                </td>
                                            </tr>
                                        ))
                                    ) : (
                                        <tr><td>No courses found.</td><td></td></tr>
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
                            <h5 className="card-title">Enroll in Course</h5>
                            <h6 className="card-subtitle text-muted">Choose one of the courses to enroll in.</h6>
                        </div>
                        <div className="card-body">
                            <table className="table table-striped" style={{ width: "100%" }}>
                                <thead>
                                    <tr>
                                        <th>Course Name</th>
                                        <th>Enroll</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {loadingAllCourses ? <tr><td>Loading...</td></tr> : allcourses && allcourses.length > 0 ? allcourses.map((course, index) => (
                                        <tr key={index}>
                                            <td>{course.CourseName}</td>
                                            <td>
                                                <button
                                                    className="btn btn-primary"
                                                    onClick={async () => {
                                                        try {
                                                            const courseId = username + '#' + course.ItemId;

                                                            const fetchFunction = enlist_student_course(courseId, username, course.ItemId);
                                                            const response = await fetchFunction();

                                                            if (!response.ok) {
                                                                const result = await response.json();
                                                                if (result === "Request not finished succesfully: The conditional request failed") {
                                                                    alert("You are already enrolled in this course.");
                                                                    return;
                                                                }
                                                                throw new Error(`HTTP error! status: ${response.status}`);
                                                            }

                                                            const result = await response.json();
                                                            if (result === "Record created successfully.") {
                                                                alert('Enrolled successfully.');
                                                                window.location.reload();
                                                            } else {
                                                                alert(`Error: ${JSON.stringify(result)}`);
                                                            }
                                                        } catch (error) {
                                                            console.error(error);
                                                            alert(`Error: ${(error as Error).message}`);
                                                        }
                                                    }}
                                                >
                                                    Enroll
                                                </button>
                                            </td>

                                        </tr>
                                    )) : <tr><td>No courses available for enrollment.</td></tr>}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div >
    );
}
export default StudentComponent;
