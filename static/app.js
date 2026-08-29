
const method = document.getElementById("method");
const url = document.getElementById("url");
const sendButton = document.getElementById("sendButton");
const responseOutput = document.getElementById("responseOutput");
const statusCode = document.getElementById("statusCode");
const responseTime = document.getElementById("responseTime");
const copyButton = document.getElementById("copyButton");
const themeButton = document.getElementById("themeButton");

function parseJSON(value, fallback = {}) {
    if (!value.trim()) {
        return fallback;
    }

    try {
        return JSON.parse(value);
    } catch {
        throw new Error("Invalid JSON input.");
    }
}

document.querySelectorAll(".tab").forEach((button) => {
    button.addEventListener("click", () => {
        document.querySelectorAll(".tab").forEach((item) => {
            item.classList.remove("active");
        });

        document.querySelectorAll(".tab-content").forEach((item) => {
            item.classList.remove("active");
        });

        button.classList.add("active");
        document.getElementById(button.dataset.tab).classList.add("active");
    });
});

sendButton.addEventListener("click", async () => {
    try {
        const headers = parseJSON(
            document.getElementById("headersInput").value
        );

        const params = parseJSON(
            document.getElementById("paramsInput").value
        );

        const bodyText = document.getElementById("bodyInput").value.trim();

        const body = bodyText ? parseJSON(bodyText, null) : null;

        statusCode.textContent = "Sending...";
        responseTime.textContent = "";
        responseOutput.textContent = "";

        const start = performance.now();

        const response = await fetch("/api/request", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                method: method.value,
                url: url.value,
                headers,
                params,
                body
            })
        });

        const result = await response.json();

        const elapsed = Math.round(performance.now() - start);

        if (!response.ok) {
            throw new Error(result.detail || "Request failed.");
        }

        statusCode.textContent =
            `${result.status_code} ${result.reason}`;

        responseTime.textContent = `${elapsed} ms`;

        responseOutput.textContent =
            typeof result.body === "object"
                ? JSON.stringify(result.body, null, 2)
                : result.body;

    } catch (error) {
        statusCode.textContent = "Error";
        responseOutput.textContent = error.message;
    }
});

copyButton.addEventListener("click", async () => {
    await navigator.clipboard.writeText(responseOutput.textContent);
    copyButton.textContent = "Copied";

    setTimeout(() => {
        copyButton.textContent = "Copy";
    }, 1500);
});

const savedTheme = localStorage.getItem("api-tester-theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark");
    themeButton.textContent = "☀️";
}

themeButton.addEventListener("click", () => {
    document.body.classList.toggle("dark");

    const dark = document.body.classList.contains("dark");

    localStorage.setItem(
        "api-tester-theme",
        dark ? "dark" : "light"
    );

    themeButton.textContent = dark ? "☀️" : "🌙";
});
