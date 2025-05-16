import ollama
from flask import Flask, request, render_template

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["user_input"]

        # Get AI response
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": user_input}]
        )

        # Extract response text
        response_text = response.get("message", {}).get("content", "Error: No response received.")

        # Detect if response is code  
        if "```" in response_text:  # AI usually formats code in triple backticks
            formatted_response = f"<pre><code>{response_text}</code></pre>"
        else:
            formatted_response = response_text.replace("\n", " ").strip()  # Normal text response

        return render_template("index.html", user_input=user_input, response=formatted_response)

    return render_template("index.html", user_input="", response="")

if _name_ == "_main_":
    app.run(debug=True)