const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const button = document.getElementById("captureBtn");
const statusText = document.getElementById("status");

navigator.mediaDevices
.getUserMedia({
    video: true
})
.then(stream => {
    video.srcObject = stream;
});

button.addEventListener("click", async () => {

    statusText.innerText = "Verifying...";

    const context =
        canvas.getContext("2d");

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    context.drawImage(
        video,
        0,
        0
    );

    const blob =
        await new Promise(resolve =>
            canvas.toBlob(resolve, "image/jpeg")
        );

    const formData =
        new FormData();

    formData.append(
        "image",
        blob,
        "capture.jpg"
    );

    const response =
        await fetch(
            "/verify",
            {
                method: "POST",
                body: formData
            }
        );

    const data =
        await response.json();

    if (data.success) {

        window.location.href =
            "/dashboard/" +
            data.username;

    } else {

        statusText.innerText =
            "Access Denied";
    }
});