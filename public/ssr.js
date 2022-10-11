let ssrSocket = new WebSocket("wss://SSR.foxnerdsaysmoo.repl.co/ssr");


ssrSocket.onopen = function(e) {
    console.log("[open] Connection established");
    console.log("Sending to server");
};

ssrSocket.onmessage = function(event) {
    console.log(`[message] Data received from server: ${event.data}`);
    let data = JSON.parse(event.data);
    for (i=0; i<data.length; i++) {
        let change = data[i];
        let element = document.getElementsByClassName(change[0])[0];
        switch (change[1]) {
            case "delete":
                element.parentNode.removeChild(e);
                break;
            case "write":
                element.innerHTML = change[2];
                break;
            case "append":
                element.innerHTML += change[2];
                break;
            case "insert":
                element.innerHTML = element.innerHTML.slice(0, change[3]) + change[2] + element.innerHTML.slice(change[3]);
                break;
            default:
                console.error(`Unknown method ${change[1]}`)
        }
    }
};

ssrSocket.onclose = function(event) {
    if (event.wasClean) {
        console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
    } else {
        // e.g. server process killed or network down
        // event.code is usually 1006 in this case
        console.log('[close] Connection died');
    }
};

ssrSocket.onerror = function(error) {
    console.log(`[error] ${error.message}`);
};
