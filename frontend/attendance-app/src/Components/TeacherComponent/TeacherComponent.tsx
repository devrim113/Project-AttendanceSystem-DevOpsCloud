/* eslint-disable react-hooks/exhaustive-deps */
import React, { useEffect, useState } from "react";
import { getInformation } from "../../Helper/static";
import { get_teacher_course_names, assign_course_to_teacher } from "../../API/teacher";
import { create_course } from "../../API/course";
import { get_all_courses } from "../../API/student";
import { generateSimpleUUID } from "../../Helper/decrypter";

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

function TeacherComponent() {
    const [teacherCourses, setCourses] = useState<Courses[] | null>(null);
    const [allcourses, setAllCourses] = useState<bigCourse[] | null>(null);
    const [loadingCourses, setLoadingCourses] = useState(true);
    const [loadingAllCourses, setLoadingAllCourses] = useState(true);
    const [courseName, setCourseName] = useState('');
    const username = getInformation()["cognito:username"];

    useEffect(() => {
        get_teacher_course_names(username)().then((response) => {
            response.json().then(data => {
                if (response.status === 200) {
                    setCourses(data);
                } else {
                    setCourses([]);
                }
                setLoadingCourses(false);
            });
        });

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

    const handleCreateCourse = async (event: React.FormEvent<HTMLFormElement>): Promise<void> => {
        event.preventDefault();

        const ItemId: string = generateSimpleUUID() + courseName;
        const DepartmentId: string = '1';

        try {
            const response: Response = await create_course(ItemId, courseName, DepartmentId)();
            if (response.ok && await response.json() === "Record created or updated successfully.") {
                alert('Course created successfully');
                window.location.reload();
            } else {
                alert('Failed to create course, maybe the name is already taken?');
            }
        } catch (error: any) {
            console.error('Error creating course:', error);
            alert('Error creating course');
        }
    };

    return (
        <div className="container-fluid p-0">
            <h1 className="h3 mb-3">Teacher Dashboard</h1>
            <p>
                Welcome to the teacher dashboard. Here you can see all the courses you are
                teaching and create new courses. Click on a course to see the attendance of
                the students. Scroll down to see the create a course card and teach a course card.
            </p>
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title">Courses</h5>
                            <h6 className="card-subtitle text-muted">
                                These are all the courses you are teaching
                            </h6>
                        </div>
                        <div className="card-body">
                            <table
                                id="datatables-responsive"
                                className="table table-striped"
                                style={{ width: "100%" }}
                            >
                                <thead>
                                    <tr>
                                        <th>Course Name</th>
                                        <th>View</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {loadingCourses ? (
                                        <tr><td>Loading...</td><td></td></tr>
                                    ) : teacherCourses ? (
                                        Object.entries(teacherCourses).map(([course_id, course_name], index) => (
                                            <tr key={index}>
                                                <td>{String(course_name)}</td>
                                                <td>
                                                    <button className="btn btn-primary" onClick={() => window.location.href = `/teacherattendance?course_id=${encodeURIComponent(String(course_id))}&course_name=${encodeURIComponent(course_name.toString())}`}>View</button>
                                                </td>
                                            </tr>
                                        ))
                                    ) : (
                                        <tr><td>No courses found.</td></tr>
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
                            <h5 className="card-title">Create Course</h5>
                            <h6 className="card-subtitle text-muted">Create a new course</h6>
                        </div>
                        <div className="card-body">
                            <form id="create-course" onSubmit={handleCreateCourse}>
                                <div className="mb-3">
                                    <label htmlFor="courseName" className="form-label">
                                        Course Name
                                    </label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="courseName"
                                        placeholder="Course Name"
                                        value={courseName}
                                        onChange={(e) => setCourseName(e.target.value)}
                                    />
                                </div>
                                <button type="submit" className="btn btn-primary">
                                    Create
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title">Teach a Course</h5>
                            <h6 className="card-subtitle text-muted">Choose one of the courses to teach.</h6>
                        </div>
                        <div className="card-body">
                            <table className="table table-striped" style={{ width: "100%" }}>
                                <thead>
                                    <tr>
                                        <th>Course Name</th>
                                        <th>Teach</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {loadingAllCourses ? <tr><td>Loading...</td><td></td></tr> : allcourses && allcourses.length > 0 ? allcourses.map((course, index) => (
                                        <tr key={index}>
                                            <td>{course.CourseName}</td>
                                            <td>
                                                <button
                                                    className="btn btn-primary"
                                                    onClick={async () => {
                                                        try {
                                                            const courseId = username + course.ItemId;

                                                            const fetchFunction = assign_course_to_teacher(courseId, course.ItemId, username);
                                                            const response = await fetchFunction();

                                                            if (!response.ok) {
                                                                const result = await response.json();
                                                                if (result === "Request not finished succesfully: The conditional request failed") {
                                                                    alert("You are already teaching this course.");
                                                                    return;
                                                                }
                                                                throw new Error(`HTTP error! status: ${response.status}`);
                                                            }

                                                            const result = await response.json();
                                                            if (result === "Record created successfully.") {
                                                                alert('Started teaching successfully.');
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
                                                    Teach
                                                </button>
                                            </td>

                                        </tr>
                                    )) : <tr><td>No courses available for teaching.</td></tr>}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default TeacherComponent;