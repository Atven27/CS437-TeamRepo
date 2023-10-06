const { unescape } = require('querystring');

document.onkeydown = updateKey;
document.onkeyup = resetKey;

var server_port = 65432;
var server_addr = "192.168.86.103";   // the IP address of your Raspberry PI

// function client(){
    
//     const net = require('net');
//     var input = document.getElementById("myName").value;

//     const client = net.createConnection({ port: server_port, host: server_addr }, () => {
//         // 'connect' listener.
//         console.log('connected to server!');
//         // send the message
//         client.write(`${input}\r\n`);
//     });
    
//     // get the data from the server
//     client.on('data', (data) => {
//         document.getElementById("greet_from_server").innerHTML = data;
//         console.log(data.toString());
//         client.end();
//         client.destroy();
//     });

//     client.on('end', () => {
//         console.log('disconnected from server');
//     });


// }


function client_direction(dir){
    
    const net = require('net');
    var input = dir;

    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        client.write(`${input}`);
    });
    
    // get the data from the server
    client.on('data', (data) => {
        // document.getElementById("greet_from_server").innerHTML = data;
        handleCarInfo(unescape(data))
        console.log(data.toString());
        client.end();
        client.destroy();
    });

    client.on('end', () => {
        console.log('disconnected from server');
    });


}


function handleCarInfo(inputStr){
    var infoArr = inputStr.split(',');
    document.getElementById("direction").innerHTML = infoArr[0]
    document.getElementById("speed").innerHTML = infoArr[1]
    document.getElementById("distance").innerHTML = infoArr[2]
    document.getElementById("temperature").innerHTML = infoArr[3]
}


// function greeting(){

//     // get the element from html
//     var name = document.getElementById("myName").value;
//     // update the content in html
//     document.getElementById("greet").innerHTML = "Hello " + name + " !";
//     // send the data to the server 
//     // to_server(name);
//     client();

// }

// update data for every 1 second
function update_data(){
    // setInterval(function(){
    //     // get image from python server
    //     console.log('Attempting to send data to server!');
    //     client_direction("INFO");
    // }, 5000);

    console.log('Attempting to send data to server!');
    client_direction("INFO");
    setTimeout(update_data, 5000);
}


// for detecting which key is been pressed w,a,s,d
function updateKey(e) {

    e = e || window.event;

    if (e.keyCode == '87') {
        // up (w)
        document.getElementById("upArrow").style.color = "green";
        // send_data("87");
        client_direction("87");
    }
    else if (e.keyCode == '83') {
        // down (s)
        document.getElementById("downArrow").style.color = "green";
        // send_data("83");
        client_direction("83");
    }
    else if (e.keyCode == '65') {
        // left (a)
        document.getElementById("leftArrow").style.color = "green";
        // send_data("65");
        client_direction("65");
    }
    else if (e.keyCode == '68') {
        // right (d)
        document.getElementById("rightArrow").style.color = "green";
        // send_data("68");
        client_direction("68");
    }
}

// reset the key to the start state 
function resetKey(e) {

    e = e || window.event;

    document.getElementById("upArrow").style.color = "grey";
    document.getElementById("downArrow").style.color = "grey";
    document.getElementById("leftArrow").style.color = "grey";
    document.getElementById("rightArrow").style.color = "grey";
}