function validate()
           {
           var password = document.getElementById("pwd1");
           var confirmpassword = document.getElementById("pwd2");

            if(password.value.trim()=="")
                {
                alert("please enter your password");
                return false;
                }
            else if(confirmpassword.value.trim()==""){
                alert("please re-enter your password to confirm");
                return false;
            }
            else if(password != confirmpassword){
                alert("passwords Do not match, please try again...");
                return false;
            }
            else{
                return true;
            }