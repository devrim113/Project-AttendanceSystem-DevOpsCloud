import React from 'react';
import './App.css';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HeaderSideBar from './Components/HeaderSideBar/HeaderSideBar';
import StudentComponent from './Components/StudentComponent/StudentComponent';
import TeacherComponent from './Components/TeacherComponent/TeacherComponent';
import AdminComponent from './Components/AdminComponent/AdminComponent';
import StudentAttendanceComponent from './Components/StudentComponent/StudentAttendanceComponent';
import { parseCognitoTokensFromUrl } from './Helper/login';
import { getCookie, setCookie } from './Helper';
import { checkValidity } from './Helper/decrypter';
import { bearerCookie, cognitoURL } from './Helper/static';
import TeacherAttendanceComponent from './Components/TeacherComponent/TeacherAttendanceComponent';
import AdminAttendanceComponent from './Components/AdminComponent/AdminAttendanceComponent';
import ProtectionComponent from './Components/ProtectionComponent/ProtectionComponent';

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
    window.location.href = cognitoURL;
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
            <Route element={<ProtectionComponent role="Students" />}>
              <Route path="/" element={<StudentComponent />} />
              <Route path="/studentattendance" element={<StudentAttendanceComponent />} />
            </Route>  

            <Route element={<ProtectionComponent role="Teachers" />}>
              <Route path="/teacher" element={<TeacherComponent />} />
              <Route path="/teacherattendance" element={<TeacherAttendanceComponent />} />
            </Route>

            <Route element={<ProtectionComponent role="Admins" />}>
              <Route path="/adminattendance" element={<AdminAttendanceComponent />} />
              <Route path="/admin" element={<AdminComponent />} />
            </Route>

          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
