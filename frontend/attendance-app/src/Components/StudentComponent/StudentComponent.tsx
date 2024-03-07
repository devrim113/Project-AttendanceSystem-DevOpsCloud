import React from "react";

function StudentComponent() {
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
                    <h6 className="card-subtitle text-muted">
                        These are all the courses you have enrolled in.
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
                    <h5 className="card-title">Enroll in Course</h5>
                    <h6 className="card-subtitle text-muted">
                        Choose one of the courses to enroll in.
                    </h6>
                    </div>
                    <div className="card-body">
                    <table
                        id="datatables-responsive-2"
                        className="table table-striped"
                        style={{ width: "100%" }}
                    >
                        <thead>
                        <tr>
                            <th>Course Name</th>
                            <th>Enroll</th>
                        </tr>
                        </thead>
                        <tbody id="data-enroll-courses"></tbody>
                    </table>
                    </div>
                </div>
                </div>
            </div>
        </div>

    )
}
export default StudentComponent