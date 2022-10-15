 function searchproduct(id)
 {
    url = '/searchProduct/'+id
    
    $.ajax({
        url : url,
        
        beforeSend:function(){
            
        },
        success:function(result){
            $('.home_div').html(result)
                
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
 })
}

function addtokart(id){
    url = '/addkartView/'+id
   
    $.ajax({
        url : url,
        
        beforeSend:function(){
            
        },
        success:function(result){
                
            console.log(result)
            if(result.status==1){
                toastr.success('success full added to kart')
            }
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
        
    })

}

function viewKart(id){

    url = '/viewKart/'+id
   
    $.ajax({
        url : url,
        
        beforeSend:function(){
            $('.home_div').empty()
        },
        success:function(result){

            $('.home_div').html(result) 
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
        
    })

}
$(document).ready(function(){
    toastr.options = {
                    "closeButton":false,
                    "debug":false,
                    "newestOnTop":false,
                    "progressBar":true,
                    "positionClass":"toast-top-left",
                    "preventDuplicates":true,
                    "onclick":null,
                    "showDuration":"300",
                    "hideDuration":"1000",
                    "timeOut":"120000",
                    "extendedTimeOut":"1000",
                    "showEasing":"swing",
                    "hideEasing":"linear",
                    "showMethod":"fadeIn",
                    "hideMethod":"fadeOut"
                }

})



