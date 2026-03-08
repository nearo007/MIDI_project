async function setPort() {
    const port = document.getElementById("select-port").value;
    const res = await fetch('/set-port', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({port})
    });

    return res.json();
}

document.getElementById('btn-setport').addEventListener('click', setPort);