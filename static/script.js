const form = document.getElementById("uploadForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent form from refreshing the page

    const formData = new FormData(form);
    resultDiv.textContent = "Loading..."; // Show a loading message

    try {
        const response = await fetch("/predict/", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();

        if (data.prediction !== undefined) {
            resultDiv.textContent = `Prediction: ${data.prediction}`;
        } else {
            resultDiv.textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        resultDiv.textContent = `Error: ${error.message}`;
    }
});