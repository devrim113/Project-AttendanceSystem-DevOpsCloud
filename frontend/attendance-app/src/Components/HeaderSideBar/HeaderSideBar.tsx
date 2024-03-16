/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";
import { Outlet } from "react-router";
import { bearerCookie, getInformation } from "../../Helper/static";
import { useNavigate } from "react-router-dom";
import { removeCookie } from "../../Helper";

/**
 * Renders the header sidebar component.
 * 
 * @returns The JSX element representing the header sidebar.
 */
function HeaderSideBar() {
    let navigator = useNavigate();

    let information = getInformation();
    const name = information["name"];
    const role: [String]= information["cognito:groups"];

    const logout = () => {
        removeCookie(bearerCookie)
        navigator("/");
    }
    return (
        <div className="wrapper">
            <nav id="sidebar" className="sidebar">
                <div className="sidebar-content js-simplebar">
                <a className="sidebar-brand" href="index.html">
                    <span className="align-middle me-3">Attendance System</span>
                </a>
                <ul className="sidebar-nav">
                    {role.includes("Students") && (
                        <li className="sidebar-item">
                        <a className="sidebar-link" onClick={() => navigator("/")}>
                            <i className="align-middle" data-feather="user" />{" "}
                            <span className="align-middle">Student</span>
                        </a>
                        </li>
                    )}
                    {role.includes("Teachers") && (
                        <li className="sidebar-item">
                        <a className="sidebar-link" onClick={() => navigator("/teacher")}>
                            <i className="align-middle" data-feather="user" />{" "}
                            <span className="align-middle">Teacher</span>
                        </a>
                        </li>
                    )}
                    {role.includes("Admins") && (
                        <li className="sidebar-item">
                        <a className="sidebar-link" onClick={() => navigator("/admin")}>
                            <i className="align-middle" data-feather="layers" />{" "}
                            <span className="align-middle">Admin</span>
                        </a>
                        </li>
                    )}
                </ul>
                </div>
            </nav>
            <div className="main">
                <nav className="navbar navbar-expand navbar-light navbar-bg">
                <a className="sidebar-toggle">
                    <i className="hamburger align-self-center" />
                </a>
                <div className="navbar-collapse collapse">
                    <ul className="navbar-nav navbar-align">
                    <li className="nav-item dropdown">
                        <a
                        className="nav-icon dropdown-toggle d-inline-block d-sm-none"
                        href="#"
                        data-bs-toggle="dropdown"
                        >
                        <i className="align-middle" data-feather="settings" />
                        </a>
                        <a
                        className="nav-link dropdown-toggle d-none d-sm-inline-block"
                        href="#"
                        data-bs-toggle="dropdown"
                        id="header-name"
                        ><span className="text-dark">{name}</span></a>
                        <div className="dropdown-menu dropdown-menu-end">
                        <a className="dropdown-item" onClick={() => logout()}>
                            Sign out
                        </a>
                        </div>
                    </li>
                    </ul>
                </div>
                </nav>
                <main className="content">
                    <Outlet />
                </main>
                <footer className="footer">
                <div className="container-fluid">
                    <div className="row text-muted">
                    <div className="col-6 text-start"></div>
                    <div className="col-6 text-end">
                        <p className="mb-0">
                        © 2023/2024 -{" "}
                        <a href="index.html" className="text-muted">
                            DevOps group 6
                        </a>
                        </p>
                    </div>
                    </div>
                </div>
                </footer>
            </div>
        </div>
    );
}

export default HeaderSideBar;