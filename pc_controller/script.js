const socket = new WebSocket('ws://10.20.1.1:8765'); // Replace with your Pi's IP address

socket.onopen = () => {
    console.log("Connected to the WebSocket server.");
};

socket.onclose = (event) => {
    console.log('Connection closed', event);
};

socket.onerror = (error) => {
    console.error('WebSocket error:', error);
};


let keys = {
    'w':'0',
    'a':'0',
    's':'0',
    'd':'0',
}

// Keyboard controls (W, A, S, D)
document.addEventListener('keydown', (event) => {
    if (socket.readyState === WebSocket.OPEN) {
        switch (event.key) {
            case 'w':  // Move forward
                keys.w = '1'
                break;
            case 'a':  // Turn left
                keys.a = '1'
                break;
            case 's':  // Stop
                keys.s = '1'
                break;
            case 'd':  // Turn right (optional)
                keys.d = '1'
                break;
            default:
                break;
        }
        socket.send(keys.a + keys.w + keys.s + keys.d)
        // socket.send(JSON.stringify(keys))
    }
});


document.addEventListener('keyup', (event) => {
    if (socket.readyState === WebSocket.OPEN) {
        switch (event.key) {
            case 'w':  // Move forward
                keys.w = '0'
                break;
            case 'a':  // Turn left
                keys.a = '0'
                break;
            case 's':  // Stop
                keys.s = '0'
                break;
            case 'd':  // Turn right (optional)
                keys.d = '0'
                break;
            default:
                break;
        }
       socket.send(keys.a + keys.w + keys.s + keys.d)

        // socket.send(JSON.stringify(keys))
    }
});
