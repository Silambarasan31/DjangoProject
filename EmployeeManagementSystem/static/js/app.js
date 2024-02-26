var message_timeout = document.getElementById("message-timer");

setTimeout(function()

{
 if (message_timeout){
    message_timeout.style.display = "none";
 }
}, 1000);


function ageCalculate(){

    const dob =new Date(document.getElementById("dob").value)
    const current = new Date()
    let dob_year = dob.getFullYear();
    let year = current.getFullYear();
    let dob_month = dob.getMonth();
    let c_month = current.getMonth();

    if (c_month < dob_month){
        document.getElementById("age").value = year-dob_year-1
    }
    else if (c_month = dob_month){
        if (current.getDate()<dob.getDate()){
            document.getElementById("age").value = year-dob_year-1 
        }
        else{
            document.getElementById("age").value = year-dob_year
        }
        
    }
    else{
        document.getElementById("age").value = year-dob_year
    }
    
};

