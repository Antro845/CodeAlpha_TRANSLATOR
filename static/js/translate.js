const inputText = document.getElementById("inputText");
const outputText = document.getElementById("outputText");
const statusBox = document.getElementById("status");

document.getElementById("translateBtn").onclick = async () => {
    const text = inputText.value.trim();
    if (!text) return;

    const source = document.getElementById("sourceLang").value;
    const target = document.getElementById("targetLang").value;

    statusBox.innerText = "Translating...";

    // 1️⃣ First try local OFFLINE translation
    let offlineResult = null;
    try {
        const res = await fetch("/offline-translate/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRF(),
            },
            body: JSON.stringify({ text, source, target }),
        });

        offlineResult = await res.json();

        if (offlineResult.success) {
            outputText.value = offlineResult.translation;
            statusBox.innerText = "Translated offline (Argos Translate)";
            return;
        }
    } catch {}

    // 2️⃣ Fallback → Try ONLINE translation
    try {
        const res = await fetch("/online-translate/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRF(),
            },
            body: JSON.stringify({ text, source, target }),
        });

        const data = await res.json();

        if (data.success) {
            outputText.value = data.translation;
            statusBox.innerText = "Translated online (LibreTranslate)";
        } else {
            statusBox.innerText = "Translation failed (offline & online)";
        }
    } catch {
        statusBox.innerText = "Translation failed (offline & online)";
    }
};

// Clear
document.getElementById("clearBtn").onclick = () => {
    inputText.value = "";
    outputText.value = "";
};

// Copy
document.getElementById("copyBtn").onclick = () => {
    navigator.clipboard.writeText(outputText.value);
    alert("Copied!");
};

// Speak
document.getElementById("speakBtn").onclick = () => {
    const msg = new SpeechSynthesisUtterance(outputText.value);
    speechSynthesis.speak(msg);
};

// Theme Switcher
document.getElementById("themeSwitcher").onchange = (e) => {
    document.body.className = e.target.value;
};

// CSRF Helper
function getCSRF() {
    return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken="))
        ?.split("=")[1];
}
