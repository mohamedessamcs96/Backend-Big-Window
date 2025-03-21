import React from 'react';

import './GoalList.css';


//JSx enable us to write js in html by converting to react create element

const GoalList = (props) => {
  return (
    <div className='course-goal '>
    <ul className='course-list'>
      {props.goals.map((goal) => (
        <li key={goal.id}>{goal.text}</li>
      ))}
    </ul>
    </div>
  );
};

export default GoalList;
