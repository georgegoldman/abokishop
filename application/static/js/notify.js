Pusher.logToConsole = true;

    var pusher = new Pusher('e271cf7723747ff31222', {
      cluster: 'eu',
      forceTLS: true
    });

    var channel = pusher.subscribe('my-channel');
    channel.bind('my-event', function(data) {
      alert(JSON.stringify(data.message));
    });

function notify(user, stock) {
  var user = user;
  var stock = stock
  data = {
    user: user,
    stock: stock
  };

  fetch(`${window.origin}/notify?`, {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(data),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
  .then(function (response){
    if (response.status != 200) {
      console.log(`your response was not 200: ${response.status}` );
      return ;
    }
    response.json().then(function (data){
      alert(data.msg);
    })
  })
}