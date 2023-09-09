const scan_btn = document.getElementById("scan-btn");
const prompt_text = document.getElementById("card-prompt-text");
const fileInput = document.getElementById("qr-code");

scan_btn.addEventListener('click', () => {
    fileInput.click();
})

function fetchRequest(file, formData) {
    prompt_text.innerText = "Scanning QR Code...";
    prompt_text.style = "color: black";
    fetch("http://api.qrserver.com/v1/read-qr-code/", {
        method: 'POST', body: formData
    }).then(res => res.json()).then(result => {
        result = result[0].symbol[0].data;
        prompt_text.innerText = result ? "Please scan your qr card" : "Couldn't scan QR Code";
        prompt_text.style = result ? "color: black;" : "color: red";
        if(!result) return;
        location.href = 'Fingerprint_auth.html';
    }).catch(() => {
        prompt_text.innerText = "Couldn't scan QR Code";
    });
}

fileInput.addEventListener("change", async e => {
    let file = e.target.files[0];
    if(!file) return;
    let formData = new FormData();
    formData.append('file', file);
    fetchRequest(file, formData);
});
