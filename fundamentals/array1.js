
// push to front of array
function push(){
    for (var z = arr.length-1; z>= 0; z --){
        arr[z+1] = arr[z];
    }
    arr[0] = val;
}

// pop to the ront

function pop(){
    var value = arr[0];
    for (var z = 1; z < arr.length; z++){
        arr[z-1]=arr[1]
    }
}


function insert(){
    for (var z = arr.length + 1; z >= index; z--){
        arr[z+1] = arr[z];
    }
    arr[index] =value
}