// ===============================
// CodeVisionAI - Final script.js
// Analyzer + AI Output + Bot Panel
// ===============================

function analyzeCode() {

    // Get user input code
    const code = document.getElementById("user-input").value;

    // Validate input
    if (!code || code.trim() === "") {
        alert("Please paste some code first.");
        return;
    }

    // Show loading message
    document.getElementById("output").innerHTML =
        "<div style='color:#00ffd0;'>Analyzing your code...</div>";

    // Send code to backend Flask API
    fetch("https://codevisionai-1.onrender.com/analyze", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            code: code
        })

    })

    .then(response => response.json())

    .then(data => {

        // Build professional AI output panel
        let outputHTML = `
        
        <div style="
            margin-top:15px;
            padding:15px;
            background:#0f172a;
            border-radius:10px;
            border:1px solid #00ffd0;
            color:white;
            font-family: Consolas, monospace;
        ">

        <div style="color:#00ffd0; font-weight:bold; font-size:16px;">
        ⚡ CodeVision Bot Analysis
        </div>

        <br>

        <b style="color:#38bdf8;">Issues found:</b><br>
        ${data.explanation && data.explanation.length > 0
            ? "• " + data.explanation.join("<br>• ")
            : "No major issues detected."}

        <br><br>

        <b style="color:#38bdf8;">Refactored Code:</b><br>

        <pre style="
            background:#020617;
            padding:10px;
            border-radius:8px;
            overflow-x:auto;
            border:1px solid #1e293b;
        ">${data.refactored_code || "No refactoring available."}</pre>

        <br>

        <b style="color:#38bdf8;">Optimization Suggestions:</b><br>

        ${data.suggestions && data.suggestions.length > 0
            ? "• " + data.suggestions.join("<br>• ")
            : "No additional suggestions."}

        <br><br>

        <div style="color:#00ffd0;">
        ✔ Analysis complete. You can ask for detailed explanation using CodeVision Bot.
        </div>

        </div>

        `;

        // Display output
        document.getElementById("output").innerHTML = outputHTML;

    })

    .catch(error => {

        console.error("Error:", error);

        document.getElementById("output").innerHTML = `
        
        <div style="
            color:red;
            padding:10px;
            background:#220000;
            border-radius:8px;
        ">
        ❌ Error connecting to backend.<br>
        Make sure Flask server is running on port 5000.
        </div>
        
        `;
    });

}


// ===============================
// Connect Analyze Button
// ===============================

document.addEventListener("DOMContentLoaded", function () {

    const analyzeBtn = document.getElementById("analyzeBtn");

    if (analyzeBtn) {

        analyzeBtn.addEventListener("click", analyzeCode);

    }

});
// ===============================
// Chat Bot Function
// ===============================

async function sendMessage() {

    const inputBox = document.getElementById("userInput");

    if (!inputBox) return;

    const message = inputBox.value;

    if (message.trim() === "") return;

    try {

        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        const replyBox = document.getElementById("botReply");

        if (replyBox) {
            replyBox.innerText = data.reply;
        }

    } catch (error) {
        console.error("Chat error:", error);
    }
}
