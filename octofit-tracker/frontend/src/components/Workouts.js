import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log('Fetching workouts from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts array:', workoutsData);
        setWorkouts(workoutsData);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) {
    return (
      <div className="content-container">
        <div className="alert alert-info d-flex align-items-center" role="alert">
          <div className="spinner-border spinner-border-sm me-3" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <div>Loading workouts...</div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="content-container">
        <div className="alert alert-danger" role="alert">
          <h5 className="alert-heading">Error Loading Workouts</h5>
          <p className="mb-0">{error}</p>
        </div>
      </div>
    );
  }

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'Easy': 'bg-success',
      'Medium': 'bg-warning text-dark',
      'Hard': 'bg-danger',
      'Beginner': 'bg-success',
      'Intermediate': 'bg-warning text-dark',
      'Advanced': 'bg-danger'
    };
    return badges[difficulty] || 'bg-secondary';
  };

  return (
    <div className="content-container">
      <h1 className="page-title">Workouts</h1>
      <p className="text-muted mb-4">Discover personalized workout suggestions to reach your fitness goals</p>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <div className="d-flex justify-content-between align-items-start mb-3">
                    <h5 className="card-title mb-0">{workout.name}</h5>
                    <span className={`badge ${getDifficultyBadge(workout.difficulty)}`}>
                      {workout.difficulty}
                    </span>
                  </div>
                  <p className="card-text flex-grow-1">{workout.description}</p>
                  <ul className="list-group list-group-flush mt-auto">
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Type:</strong>
                      <span className="badge bg-primary">{workout.activity_type}</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Duration:</strong>
                      <span>{workout.duration} min</span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Calories:</strong>
                      <span className="badge bg-success">{workout.calories_estimate}</span>
                    </li>
                  </ul>
                  <button className="btn btn-primary mt-3 w-100">Start Workout</button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-warning" role="alert">
              <p className="mb-0 text-center"><em>No workouts found</em></p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Workouts;
