import React from 'react';
import './App.css';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HeaderSideBar from './Components/HeaderSideBar/HeaderSideBar';
import RedirectWithToken from './Components/LoginComponent/Login';
import StudentComponent from './Components/StudentComponent/StudentComponent';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<RedirectWithToken />}>
            <Route path="/" element={<HeaderSideBar />}>
              <Route path="/" element={<StudentComponent/>} />
            </Route>

          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
