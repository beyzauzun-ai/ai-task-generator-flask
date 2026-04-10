from flask import Flask, render_template, jsonify, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        topic = data.get("topic", "").strip()

        if not topic:
            topic = "AI trends in 2026"

        result = subprocess.check_output(
            ["python", "agent.py", topic],
            stderr=subprocess.STDOUT
        ).decode("cp1254", errors="replace")

        return jsonify({"result": result})

    except subprocess.CalledProcessError as e:
        return jsonify({
            "result": "Python hatası:\n" + e.output.decode("cp1254", errors="replace")
        })

if __name__ == "__main__":
    app.run(debug=True)
