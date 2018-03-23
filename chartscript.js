    
    var where = window.location.hostname;
    console.log(where);
    //#this connect fails on aws; yes
    
    var connection = new WebSocket('ws://'+where+':81/websocket');
    var tData =[];
    connection.onmessage = function(event) {
        var newData = JSON.parse(event.data);
        var updateObject =[{
            "Spent": newData.Spent,
        }]
        if (tData.length <= 40) {
            tData.push(newData.Spent);
        }
        if (tData.length > 40) {
            tData.shift();
        }
        var x = tData.join(', ');
        document.getElementById("tickerdata").innerHTML = x;
        console.log("x: "+x);
        // refresh baseline:
        var c = document.getElementById("canvas-chart");
        var ctx = c.getContext("2d");
        ctx.clearRect(0,0,400,200);
        //ctx.clearRect();
        ctx.strokeStyle='rgb(0,0,0)';
        ctx.moveTo(0,100);
        ctx.lineTo(400,100);
        ctx.stroke(); 

        // data trace
        ctx.strokeStyle='rgb(255,0,0)';
        ctx.beginPath();
        ctx.moveTo(0,100); 
        for(i=0; i<tData.length; i++){          
            ctx.lineTo(i*10, tData[i]);
        }
        //ctx.closePath();
        ctx.stroke();
        
    }