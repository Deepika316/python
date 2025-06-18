import React, { useState } from 'react'

const Cricket = (props) => { 
    //states are created here inside the function
    const [runs , setRuns] = useState(0);
    const [wickets , setWickets] = useState(0);
    const [target , setTarget] = useState(props.target);
    const [ballcount,setBallcount]=useState(0);



    // const handleSix = () =>{
    //     setRuns(runs + 6);
    // }

    // const handleFour = () =>{
    //     setRuns(runs + 4);
    // }

    //const handleOne = () =>{
       // setRuns(runs + 1);
   // }
    const handleRuns = (run) => {
        if(runs + run >= target)
            alert("Target Chased");
        setRuns(runs + run)
    };

    const handleWicket = () =>{

        if(wickets + 1 === 10)
            alert("All Out");

        setWickets(wickets + 1); // it will take some time to update
    }

     const handlecount=(ball)=>{
    setBallcount(ballcount+ball)
   }


    
    const overs=`${Math.floor((ballcount)/6)}.${ballcount%6}`

    const totalballs = props.totalovers * 6
    const remainingballs = totalballs - ballcount
    const oversleft = `${Math.floor(remainingballs / 6)}.${remainingballs % 6}`


  return (
    <>
   
        <h1>Score : {runs} / {wickets}</h1>
        {
        ballcount >= totalballs?
         <h2>Failed to Chase Target</h2>// overs done => "Failed to Chase Target"
        : 
        <>
            <h2>Current Over : {overs}</h2>
            <h2>Overs Left: {oversleft}</h2>
        </>
        }
        
        {
            wickets < 10 && runs < target && ballcount<totalballs?
            <div>
                <button onClick={()=>{handleRuns(6);handlecount(1);}} >Six</button>
                <button onClick={()=>{handleRuns(4);handlecount(1);}} >Four</button>
                <button onClick={()=>{handleRuns(3);handlecount(1);}}>Three</button>
                <button onClick={()=>{handleRuns(2);handlecount(1);}}>Two</button>
               <button onClick={()=>{handleRuns(1);handlecount(1);}}>One</button>
                <button onClick={()=>{handleRuns(0);handlecount(1);}}>Dot ball</button>
                <button onClick={()=>{handleWicket();handlecount(1);}} >Wicket</button>
            </div>
            :
            <h2>Game Over</h2>
        }
       
    </>
    
  )
}

export default Cricket