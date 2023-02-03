// import axios from "axios";
import React ,{ useState } from "react";
export const Register = (props) => {
    const[firstname,setFirstname] = useState('');
    const[lastname,setLastname] = useState('');
    const[email, setEmail] = useState('');
    const[phone,setPhone] = useState('');
    const[password, setPass] = useState('');

    const handleSubmit = (e) =>
    
    {
        e.preventDefault();
           
    //     let formData = new FormData();
    //     formData.append('email', e.target.email.value);
    //     formData.append('password', e.target.password.value);
    //     formData.append('first_name', e.target.firstname.value);
    //     formData.append('last_name', e.target.lastname.value);
    //     formData.append('phone', e.target.phone.value);
        
    //     fetch("http://127.0.0.1:8000/bookop/",
    //         {
    //             body: formData,
    //             method: "post",
    //             headers: {
    //                 "Content-Type": "application/x-www-form-urlencoded"
    //               },
    //         });
    // }
          
           fetch("http://127.0.0.1:8000/bookop/", {
             
            // Adding method type
            method: "POST",
             
           // Adding body or contents to send
            body: JSON.stringify({
              email:e.target.email.value,
              password:e.target.password.value,
              first_name:e.target.firstname.value,
              last_name:e.target.lastname.value,
              phone:e.target.phone.value,
              
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
        <label htmlFor="name">First Name</label>
        <input value={firstname} onChange={(e)=> setFirstname(e.target.value)} name="firstname" id="firstname" placeholder="first name"/>
        <label htmlFor="name">Last Name</label>
        <input value={lastname} onChange={(e)=> setLastname(e.target.value)} name="lastname" id="lastname" placeholder="last name"/>
        <label htmlFor="email">email</label>
        <input value={email} onChange={(e)=> setEmail(e.target.value)} type="email" placeholder="nikita@gmail.com" id="email" name="email" />
        <label htmlFor="phone">Enter your phone number:</label>
        <input value={phone} onChange={(e)=> setPhone(e.target.value)} type="tel" id="phone" name="phone" ></input>
        <label htmlFor="password">password</label>
        <input value={password} onChange={(e)=> setPass(e.target.value)} type="password" placeholder="*******" id="password" name="password" />
        <button type="submit">Register</button>
        </form>
        <button onClick={()=> props.onFormSwitch('Login')}>Already have an account? Login here</button>
        </>
     
    )
}