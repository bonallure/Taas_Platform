function validateRegistrationForm() 
{
   
    var user_Id = document.forms["orderForm"]["user_Id"].value;
    var password = document.forms["orderForm"]["password"].value;
    var address = document.forms["adress"]["adress"].value;


    if ( user_Id == "" || password == "" || address == "")
    {
      alert("Please fill out the form completely.");
    }
    else
    {
      sendForm();
    }
    
}
function submit_order()
{
  //create form variable
  var form = document.getElementById('order_form');
  //capture form data
  var order = {};
  var i;
  for (i = 0; i <form.length; i++)
  {
    if (form.elements[i].name != ""){
      order[form.elements[i].name] =  new URLSearchParams(form.elements[i].value).toString();
    }
  }
  //POST the form data
  var form_action = 'http://localhost:8084/demand-back-end/order_api/v1/order';
  var xhr = new XMLHttpRequest();
  xhr.open("POST", form_action, true);
  // xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function() { // Call a function when the state changes.
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        document.getElementById('order_status').innerHTML = "We're working on finding you a vehicle.";
        //document.getElementById('order_div').innerHTML = "";
    }
  }
  xhr.send(JSON.stringify(order));
  return false;
}
