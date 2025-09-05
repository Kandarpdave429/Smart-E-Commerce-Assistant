document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("askBtn").addEventListener("click", async () => {
    const question = document.getElementById("question").value;

    const response = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        question: question,
        context: "This smartphone has 8GB RAM and 128GB storage." // sample product context
      })
    });

    const data = await response.json();
    document.getElementById("answer").innerText = data.answer || "No answer";
  });
});
