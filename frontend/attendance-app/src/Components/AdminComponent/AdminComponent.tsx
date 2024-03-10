import React from "react";

function AdminComponent() {
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