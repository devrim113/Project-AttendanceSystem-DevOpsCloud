import React from 'react';
import './App.css';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HeaderSideBar from './Components/HeaderSideBar/HeaderSideBar';
import RedirectWithToken from './Components/LoginComponent/Login';
import StudentComponent from './Components/StudentComponent/StudentComponent';
import TeacherComponent from './Components/TeacherComponent/TeacherComponent';
import AdminComponent from './Components/AdminComponent/AdminComponent';
import StudentAttendanceComponent from './Components/StudentComponent/StudentAttendanceComponent';
import { parseCognitoTokensFromUrl } from './Helper/login';
import { getCookie, setCookie } from './Helper';
import { checkValidity } from './Helper/decrypter';
import { bearerCookie, getInformation } from './Helper/static';
import TeacherAttendanceComponent from './Components/TeacherComponent/TeacherAttendanceComponent';
import AdminAttendanceComponent from './Components/AdminComponent/AdminAttendanceComponent';

function App() {
  // useEffect(() => {
  let { idToken } = parseCognitoTokensFromUrl()
  if (idToken === null) {
    idToken = getCookie(bearerCookie);
  }
  if (idToken && checkValidity(idToken)) {
    // const epochTimeExpire: number = getInformation()["exp"]
    // const utcString = new Date((epochTimeExpire * 1000)+3600).toUTCString()
    setCookie(bearerCookie, idToken)
  } else {
    window.location.href = 'https://student-attendance-system.auth.eu-central-1.amazoncognito.com/login?response_type=token&client_id=6pnhs85ctml9b9f353b14ui6b4&redirect_uri=https://d5j4m0w9schy1.cloudfront.net/';
    return (<>
      Need to login.
    </>)
  }
  // }, []);

  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HeaderSideBar />}>
            <Route path="/" element={<StudentComponent />} />
            <Route path="/teacher" element={<TeacherComponent />} />
            <Route path="/admin" element={<AdminComponent />} />
            <Route path="/studentattendance" element={<StudentAttendanceComponent />} />
            <Route path="/teacherattendance" element={<TeacherAttendanceComponent />} />
            <Route path="/adminattendance" element={<AdminAttendanceComponent />} />
          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
