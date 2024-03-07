import React from 'react';
import './App.css';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HeaderSideBar from './Components/HeaderSideBar/HeaderSideBar';
import RedirectWithToken from './Components/LoginComponent/Login';
import StudentComponent from './Components/StudentComponent/StudentComponent';
import TeacherComponent from './Components/TeacherComponent/TeacherComponent';
import AdminComponent from './Components/AdminComponent/AdminComponent';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<RedirectWithToken />}>
            <Route path="/" element={<HeaderSideBar />}>
              <Route path="/" element={<StudentComponent/>} />
              <Route path="/teacher" element={<TeacherComponent/>} />
              <Route path="/admin" element={<AdminComponent/>} />
            </Route>
          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
