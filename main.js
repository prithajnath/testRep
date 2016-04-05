//var main_number = $(".number").val();
var main_number = "5186451487";

var get_contacts = function(hashnumber){
    
    var contact_one = hashnumber.slice(0,10);
    var contact_two = hashnumber.slice(11,21);
    
    
};


var create_hash = function(number){
    
    var hash;
    
    if(number<main_number){
        
        hash = String(number)+String(main_number);
        
    }else{
        
        hash = String(main_number)+String(number);
        
    }
    
    return hash;
    
};