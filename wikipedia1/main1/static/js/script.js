const form = document.getElementById("search-form");
const input = document.getElementById("search-input");
const button = document.getElementById("search-button");
const resultBox = document.getElementById("result");
const messageBox = document.getElementById("message");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    button.disabled = true;
    button.textContent = "Searching...";
    messageBox.textContent = "";

    try {
        const response = await fetch("", {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        });

        const data = await response.json();

        if (data.success) {
            resultBox.textContent = data.result;
        } else {
            resultBox.textContent = "";
            messageBox.textContent = data.error;
        }
    } catch (error) {
        resultBox.textContent = "";
        messageBox.textContent = "Something went wrong. Please try again.";
    } finally {
        button.disabled = false;
        button.textContent = "Search";
        input.focus();
    }
});