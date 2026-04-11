from flask import Flask, render_template, jsonify, request
import subprocess

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        topic = data.get("topic", "").strip() if data else ""

        if not topic:
            topic = "AI trends in 2026"

        result = subprocess.check_output(
            ["python3", "agent.py", topic],
            stderr=subprocess.STDOUT
        ).decode("utf-8", errors="replace")

        return jsonify({"result": result})

    except subprocess.CalledProcessError as e:
        error_output = e.output.decode("utf-8", errors="replace")
        return jsonify({"result": f"Python hatası:\n{error_output}"}), 500

    except Exception as e:
        return jsonify({"result": f"Genel hata: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
