import React from "react";

function TeacherComponent() {
    return (
        <div className="container-fluid p-0">
        <h1 className="h3 mb-3">Teacher Dashboard</h1>
        <p>
            Welcome to the teacher dashboard. Here you can see all the courses you are
            teaching and create new courses. Click on a course to see the attendance of
            the students. Scroll down to see the create a course card.
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
                        className="form-control"
                        id="courseName"
                        placeholder="Course Name"
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

    )
}

export default TeacherComponent;