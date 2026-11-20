
from flask import Flask, render_template, request
from analyzer import analyze_logs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None
    filename = None

    if request.method == "POST":

        file = request.files.get("logfile")

        if not file or file.filename == "":
            error = "Please select a log file."

        else:
            try:
                content = file.read().decode("utf-8")

                result = analyze_logs(content)
                filename = file.filename

                if result["total"] == 0:
                    error = "No valid log records found."
                    result = None

            except Exception:
                error = "Unable to read the file."

    return render_template(
        "index.html",
        result=result,
        error=error,
        filename=filename
    )

if __name__ == "__main__":
    app.run(debug=True)
