import logo from './logo.svg';
import React,{useState} from 'react';

import './App.css';


import GoalList from './components/GoalList/GoalList'
import NewGoal from './components/NewGoal/NewGoal'

//react will note render the screen every function or event triggered, you have to till react when should rendered so we use state
function App() {

  const [goals,setGoals] = useState([
    {'id':'g1','text':'Finish the course'},
    {'id':'g2','text':'Learn all about the course'},
    {'id':'g3','text':'Help the students course'}
  ])

  const addNewGoal = (newGoal) => {
    // Use the previous state to add new goals without overwriting the old ones
    setGoals((prevGoals) => prevGoals.concat(newGoal));
  };


  
  return (
    <div className="App">
      <NewGoal onAddGoal={addNewGoal} />
      <GoalList goals={goals}/>
    </div>
  );
}

export default App;
