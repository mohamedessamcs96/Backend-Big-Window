const express =require('express');



const app=express();


app.use((req,res,next)=>{
console.log('MiddleWare');
next();
});

app.use((req,res,next)=>{
    res.send('<form><input type="text" name="username"/><Button type="submit>Create User</Button></form>')
})


app.listen(3000);