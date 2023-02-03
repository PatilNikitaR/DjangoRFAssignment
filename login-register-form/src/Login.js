import React ,{ useState } from "react";

export const Login = (props) => {
    const[email, setEmail] = useState('');
    const[pass, setPass] = useState('');
    
    const handleSubmit = (e) =>
    {
      e.preventDefault();
         console.log(e.target.email.value)
         console.log(e.target.password.value)

         fetch("http://127.0.0.1:8000/bookop/login/", {
             
            // Adding method type
            method: "POST",
             
           // Adding body or contents to send
            body: JSON.stringify({
              email:e.target.email.value,
              password:e.target.password.value,
             

            }),
      
            // Adding headers to the request
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
         
        //Converting to JSON
        .then(response => response.json())
         
          };
 
    
    return (
        <>
            <form onSubmit={handleSubmit}>
              
                <label htmlFor="email">email</label>
                <input value={email} onChange={(e)=> setEmail(e.target.value)} type="email" placeholder="nikita@gmail.com" id="email" name="email" />
                <label htmlFor="password">password</label>
                <input value={pass} onChange={(e)=> setPass(e.target.value)} type="password" placeholder="*******"  name="password" />
                <button type="submit">Log In</button>
            </form>
            <button onClick={()=> props.onFormSwitch('Register')}>Don't have an account? Register here.</button>
        </>
    )
}