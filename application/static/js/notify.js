Pusher.logToConsole = true;

    var pusher = new Pusher('e271cf7723747ff31222', {
      cluster: 'eu',
      forceTLS: true
    });

var channel = pusher.subscribe('notify-channel');
    channel.bind('new-notification', function(data) {
      alert(JSON.stringify(data.msg));
      document.getElementById("notify_count").textContent += 1;
    });
    
