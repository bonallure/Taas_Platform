var form = document.getElementById('logInForm')
form.addEventListener('submit',(e) => {e.preventDefault();})
function validatelogInForm() 
{
	console.log("hello1");
    var username = document.forms["logInForm"]["username"].value;
    console.log("hello2");
    var password = document.forms["logInForm"]["password"].value;
    if (username == "" || password == "") {
      alert("Required field");
      
    }
    else
    {
      sendForm();
    }
}
function sendForm()
{
    var form = document.getElementById('logInForm');
    //capture form data
    var user = {}
    var i;
    for (i = 0; i <form.length; i++){
        if (form.elements[i].name != ""){
          user[form.elements[i].name] =  form.elements[i].value;
        }
    }
	// var formAction = 'https://demand.team11.sweispring21.tk/common-services/logInForm?';
	var url = new URL('https://demand.team11.sweispring21.tk/common-services/logInForm')
	var xmlreq = new XMLHttpRequest();
	//intiate request
	xmlreq.open('POST', url, true );
	xmlreq.send(JSON.stringify(user));
	xmlreq.onload = function ()
	{
		console.log(xmlreq.status)
		if(xmlreq.status == 200)
		{
			console.log(xmlreq.status);
			var data = JSON.parse(xmlreq.response);
			alert("Log-in successful",data);
			window.location.href = "https://demand.team11.sweispring21.tk/orderFormCOVID.html";
		}
		else
		{
			alert("error");
		}
	};

}
