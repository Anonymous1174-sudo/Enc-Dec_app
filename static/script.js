function encryptData() {
    let data = document.getElementById("data").value;
    let method = document.getElementById("method").value;

    fetch("/encrypt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ data, method })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").value = data.result || "Encryption failed!";
    })
    .catch(error => console.error("Error:", error));
}

function decryptData() {
    let data = document.getElementById("data").value;
    let method = document.getElementById("method").value;

    fetch("/decrypt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ data, method })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").value = data.result || "Decryption failed!";
    })
    .catch(error => console.error("Error:", error));
}

function copyText() {
    let resultField = document.getElementById("result");
    resultField.select();
    document.execCommand("copy");
    alert("Copied to clipboard!");
}
