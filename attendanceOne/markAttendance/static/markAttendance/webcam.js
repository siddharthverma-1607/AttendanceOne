// Set constraints for the video stream
var constraints = { video: { facingMode: "user" }, audio: false };
// Define constants
const cameraView = document.querySelector("#camera--view"),
    cameraOutput = document.querySelector("#camera--output"),
    cameraSensor = document.querySelector("#camera--sensor"),
		submitImg = document.querySelector("#send"),
    cameraTrigger = document.querySelector("#camera--trigger")
// Access the device camera and stream to cameraView
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
        track = stream.getTracks()[0];
        cameraView.srcObject = stream;
    })
    .catch(function(error) {
        console.error("Oops. Something is broken.", error);
    });
}
// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function() {
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    cameraOutput.src = cameraSensor.toDataURL("image/jpeg");
    cameraOutput.classList.add("taken");		
};

// send data to python
// send.onclick = function(){	
//     var httpPost = new XMLHttpRequest(),
//         path = "",
//         data = JSON.stringify({image: cameraOutput.src});
//     httpPost.onreadystatechange = function(err) {
//             if (httpPost.readyState == 4 && httpPost.status == 200){
//                 console.log(httpPost.responseText);
//             } else {
//                 console.log(err);
//             }
//         };
//     // Set the content type of the request to json since that's what's being sent
//     // httpPost.setHeader('Content-Type', 'application/json');
//     httpPost.open("POST", path, true);
//     httpPost.send(data);
// };

// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);