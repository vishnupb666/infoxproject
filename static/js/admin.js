

function addCategory(){
    url = '/addcategory'
    $.ajax({
        url : url,
        beforeSend:function(){
            $('#admindash').empty()
        },
        success:function(result){
            $('#admindash').html(result)
            
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
        
    })

}



function viewUsers(){
    url = '/view_users'
    $.ajax({
        url : url,
        beforeSend:function(){
            $('#admindash').empty()
        },
        success:function(result){
            $('#admindash').html(result)
            
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
        
    })

}
//  Ajax jQuery
function upload() { 
    var data = new FormData($('#ajax').get(0));
    console.log(data)
    $.ajax({
        url: '/addcategory', // same url 'action' in form
        type: 'POST',
        data: data,
        contentType: 'multipart/form-data',
        processData: false,
        contentType: false,
        success: function(data) {
            alert('success');
            listCategory();
        }
    });
    
}
// function saveCategory(){
    
//     var name = $('#category').val()
//     var image = $('#image').val()
//     var formdata = new FormData()
//     formdata.append('name',name);
//     formdata.append('file',image);

//     $.ajax({
//         url : "/addcategory", // the endpoint,commonly same url
//         type : "POST", // http method
//         contentType: 'multipart/form-data',
//         data :formdata,
//          // data sent with the post request
//             // handle a successful response
//             success : function(json) {
//             console.log(json); // another sanity check
//             listCategory()
//             },
//             // handle a non-successful response
//             error : function(xhr,errmsg,err) {
//             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//             }
//         });
// }

function listCategory(){

    url = '/listCategory'
    $.ajax({
        url : url,
        beforeSend:function(){
            
        },
        success:function(result){
                $('#listdata').html(result)
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
        
    })

}
function addCategory(){
    url = '/addcategory'
    $.ajax({
        url : url,
        beforeSend:function(){
            $('#admindash').empty()
        },
        success:function(result){
            $('#admindash').html(result)
            
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
        
    })

}

function addProduct(){
    url = '/addproduct'
    $.ajax({
        url : url,
        beforeSend:function(){
            $('#admindash').empty()
        },
        success:function(result){
            $('#admindash').html(result)
            
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
        
    })

}
function productUpload() { 
    var data = new FormData($('#product').get(0));
    console.log(data)
    $.ajax({
        url: '/addproduct', // same url 'action' in form
        type: 'POST',
        data: data,
        contentType: 'multipart/form-data',
        processData: false,
        contentType: false,
        success: function(data) {
            alert('success');
            listProduct()
        
        }
    });
    
}
function listProduct(){

    url = '/listProduct'
    data= {id:id}
    $.ajax({
        url : url,
        data:data,
        beforeSend:function(){
            $('#cat_view').empty()
        },
        success:function(result){
                $('.home_div').html(result)
            // setTimeout(editItem(id,fname,lname,email,image,uname,course,date,gender), 1000);
        },
        
    })

}



