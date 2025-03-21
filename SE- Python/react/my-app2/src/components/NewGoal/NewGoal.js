import React from 'react';



import './NewGoal.css';

const NewGoal=(props)=>{
    const AddGoalHandler =(event)=>{
        event.preventDefault();

        const newGoal={
            id:Math.random().toString(),
            text:'My New Goal'
        }
        console.log(newGoal);
        props.onAddGoal(newGoal)
    }
    return(
        <form className='new-goal' onSubmit={AddGoalHandler}>
        <input type='text' />
        <button type='submit'>Add Goal</button>
        </form>
    )


}




export default NewGoal;