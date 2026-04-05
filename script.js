async function predictAQI() {
    const pm25 = document.getElementById("pm25").value;
    const pm10 = document.getElementById("pm10").value;
    const no2 = document.getElementById("no2").value;

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            pm25: Number(pm25),
            pm10: Number(pm10),
            no2: Number(no2)
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML =
        `AQI: ${data.AQI} <br> Suggestion: ${data.suggestion}`;
}