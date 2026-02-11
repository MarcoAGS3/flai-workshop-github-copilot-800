import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function Home() {
  return (
    <div className="welcome-section">
      <h1 className="display-4">Welcome to OctoFit Tracker</h1>
      <p className="lead">Track your fitness activities, compete with teams, and achieve your goals!</p>
      
      <div className="row mt-5 g-4">
        <div className="col-md-4">
          <Link to="/users" className="text-decoration-none">
            <div className="card clickable-card">
              <div className="card-body text-center">
                <i className="bi bi-people-fill" style={{fontSize: '3rem', color: '#667eea'}}></i>
                <h3 className="card-title mt-3">Users</h3>
                <p className="card-text text-muted">View and manage all users</p>
              </div>
            </div>
          </Link>
        </div>
        
        <div className="col-md-4">
          <Link to="/activities" className="text-decoration-none">
            <div className="card clickable-card">
              <div className="card-body text-center">
                <i className="bi bi-activity" style={{fontSize: '3rem', color: '#667eea'}}></i>
                <h3 className="card-title mt-3">Activities</h3>
                <p className="card-text text-muted">Track your fitness activities</p>
              </div>
            </div>
          </Link>
        </div>
        
        <div className="col-md-4">
          <Link to="/leaderboard" className="text-decoration-none">
            <div className="card clickable-card">
              <div className="card-body text-center">
                <i className="bi bi-trophy-fill" style={{fontSize: '3rem', color: '#667eea'}}></i>
                <h3 className="card-title mt-3">Leaderboard</h3>
                <p className="card-text text-muted">See who's leading the pack</p>
              </div>
            </div>
          </Link>
        </div>
      </div>
      
      <div className="mt-5">
        <Link to="/teams" className="btn btn-primary btn-lg me-2">View Teams</Link>
        <Link to="/workouts" className="btn btn-outline-secondary btn-lg">Browse Workouts</Link>
      </div>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img src="/octofitapp-logo.png" alt="OctoFit Logo" />
            OctoFit Tracker
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/activities" element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/users" element={<Users />} />
        <Route path="/workouts" element={<Workouts />} />
      </Routes>
    </div>
  );
}

export default App;
