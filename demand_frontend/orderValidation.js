
function ValidateEmail(email)
{
    var mailformat = /^w+([.-]?w+)*@w+([.-]?w+)*(.w{2,3})+$/;
    if(inputText.value.match(mailformat))
    {
    alert("You have entered a valid email address!");    //The pop up alert for a valid email address
    document.form1.text1.focus();
    return true;
    }
    else
    {
    alert("You have entered an invalid email address!");    //The pop up alert for an invalid email address
    document.form1.text1.focus();
    return false;
}

function validateOrderForm() 
{
    var fName = document.forms["orderFormCOVID"]["fName"].value;
    var lName = document.forms["orderFormCOVID"]["lName"].value;
    var email = document.forms["orderFormCOVID"]["email"].value;
    var DOB = document.forms["orderFormCOVID"]["DOB"].value;
    var username = document.forms["orderFormCOVID"]["userId"].value;
    var password = document.forms["orderFormCOVID"]["Password"].value;
    var phoneNumber = document.forms["orderFormCOVID"]["Phone_number"].value;
    
    if (fName == "" || lName =="" || DOB =="" || ValidateEmail(email) || createId == "" || password == "") {
      alert("Required field");
      return false;
    }
    
}

}