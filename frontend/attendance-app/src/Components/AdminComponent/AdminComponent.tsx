import React, { useEffect, useState } from "react";
import { get_all_courses } from "../../API/student";
import { generateSimpleUUID } from "../../Helper/decrypter";
import { create_course } from "../../API/course";


function AdminComponent() {
    const [courses, setCourses] = useState<null | any>(null);

    const [courseInput, setCourseInput] = useState("");

    useEffect(() => {
        get_all_courses()().then((response) => {
            response.json().then(data => {
                    console.log(data);
                    if (response.status === 200 && data.length > 0) {
                        setCourses(data);
                    } else {
                        setCourses([]);
                    }
                });
            });
        }, []);
    const renderCourses = (course: any) => {
        return (
            <tr>
                <td>{course["CourseName"]}</td>
                <td>
                    <a className="btn btn-primary">
                        View
                    </a>
                </td>
            </tr>
        )
    }
    
    const newCourse = async (event: any): Promise<void> => {
        event.preventDefault();

        const ItemId: string = generateSimpleUUID() + '#' + courseInput;
        const DepartmentId: string = '1';

        try {
            const response: Response = await create_course(ItemId, courseInput, DepartmentId)();
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
    }

    return (
        <div className="container-fluid p-0">
            <h1 className="h3 mb-3">Admin Dashboard</h1>
            <p>
                Welcome to the Admin dashboard. Here you can see all the courses. Click on a
                course to see the attendance of the students. Scroll down to see the create
                a course card.
            </p>
            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title">Courses</h5>
                            <h6 className="card-subtitle text-muted">
                                These are all the courses
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
                                    {
                                        courses ? courses.map((course: any) => renderCourses(course)) : <tr><td>Loading...</td><td></td></tr>
                                    }
                                </tbody>
                                <tbody id="data-student-courses"></tbody>
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
                            <form id="create-course">
                                <div className="mb-3">
                                    <label htmlFor="courseName" className="form-label">
                                        Course Name
                                    </label>
                                    <input
                                        type="text"
                                        value={courseInput}
                                        onChange={(e) => setCourseInput(e.target.value)}
                                        className="form-control"
                                        id="courseName"
                                        placeholder="Course Name"
                                    />
                                </div>
                                <button onClick={newCourse} className="btn btn-primary">
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
                            <h5 className="card-title">Create a Teacher</h5>
                            <h6 className="card-subtitle text-muted">Create a new teacher</h6>
                        </div>
                        <div className="card-body">
                            <form id="create-teacher">
                                <div className="mb-3">
                                    <label htmlFor="teacherName" className="form-label">
                                        Teacher Name
                                    </label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="teacherName"
                                        placeholder="Teacher Name"
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="teacherUsername" className="form-label">
                                        Teacher Username
                                    </label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="teacherUsername"
                                        placeholder="Teacher Username"
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="teacherPassword" className="form-label">
                                        Teacher Password
                                    </label>
                                    <input
                                        type="password"
                                        className="form-control"
                                        id="teacherPassword"
                                        placeholder="Teacher Password"
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
        </div>

    );
}

export default AdminComponent;