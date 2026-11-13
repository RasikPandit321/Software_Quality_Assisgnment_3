"""Flask application for hand-sign digit recognition."""

# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_result

# Instantiating flask app
app = Flask(__name__)

# Limit the maximum request size to 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024


# Home route
@app.route("/")
def main():
    """Display the homepage for uploading hand-sign images."""
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """Process an uploaded image and display its predicted digit."""
    try:
        img = preprocess_img(request.files['file'].stream)
        pred = predict_result(img)
        return render_template("result.html", predictions=str(pred))

    except (KeyError, OSError, ValueError):
        error = "File cannot be processed."
        return render_template("result.html", err=error)


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=False)
