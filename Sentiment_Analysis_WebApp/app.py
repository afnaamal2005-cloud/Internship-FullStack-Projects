
from flask import Flask, render_template, request

app = Flask(__name__)

positive_words = {"good","great","excellent","happy","love","awesome","amazing","best","positive","wonderful"}
negative_words = {"bad","terrible","awful","hate","worst","negative","poor","sad","angry","disappointing"}

def analyze_sentiment(text):
    words = text.lower().split()
    pos = sum(1 for w in words if w.strip(".,!?") in positive_words)
    neg = sum(1 for w in words if w.strip(".,!?") in negative_words)

    if pos > neg:
        return "Positive 😊"
    elif neg > pos:
        return "Negative 😞"
    return "Neutral 😐"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    text = ""
    if request.method == "POST":
        text = request.form.get("text", "")
        result = analyze_sentiment(text)
    return render_template("index.html", result=result, text=text)

if __name__ == "__main__":
    app.run(debug=True)
