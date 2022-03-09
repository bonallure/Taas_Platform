var form = document.getElementById('registrationForm')
form.addEventListener('submit',(e) => {e.preventDefault();})
function validateRegistrationForm() 
{
    var FName = document.forms["registrationForm"]["FName"].value;
    var LName = document.forms["registrationForm"]["LName"].value;  
    var DOB = document.forms["registrationForm"]["DOB"].value;    
    var email = document.forms["registrationForm"]["email"].value;    
    var username = document.forms["registrationForm"]["username"].value;    
    var password = document.forms["registrationForm"]["password"].value;
  
    var emailReg = /^[a-z]([a-z]|[\-_.])*@[a-z]+.[a-z]{2,4}/i;

    if (FName == "" || LName =="" || DOB =="" || username == "" || password == "")
    {
      alert("Please fill out the form completely.");
    }
    else if (!(email).match(emailReg))
    {
      alert("Invalid email format: try again");
    }
    else
    {
      sendForm();
    }
    
}
function sendForm()
{
  //create form variable
  var form = document.getElementById('registrationForm');

  //capture form data
  var user = {};
  
  var i;
  for (i = 0; i <form.length; i++)
  {
    if (form.elements[i].name != ""){ 
      user[form.elements[i].name] =  form.elements[i].value;
    }
  }
  //POST the form data
  var formAction = 'https://demand.team11.sweispring21.tk/common-services/registrationForm';
  var xmlreq = new XMLHttpRequest();
  xmlreq.open('POST', formAction, true );
  xmlreq.send(JSON.stringify(user));
  xmlreq.onreadystatechange = function (){
    if (this.readyState === XMLHttpRequest.DONE && xmlreq.status === 200 ){
        var data = JSON.parse(xmlreq.response);
        
        if(form == document.getElementById('registrationForm'))
        {
          window.location.href = "https://demand.team11.sweispring21.tk/logInForm.html";
          alert("Registration successful",data);
        }
        else if(form == document.getElementById('FMRegistrationForm'))
        {
          window.location.href = "https://demand.team11.sweispring21.tk/FMLogInForm.html";
        }
        
        
    
    }
  }; 
  
}


