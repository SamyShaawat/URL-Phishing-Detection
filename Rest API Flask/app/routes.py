from flask import Blueprint, request, jsonify
from .model import model, tokenizer
from .utils import preprocess_input
import torch

routes_blueprint = Blueprint("routes", __name__)


@routes_blueprint.route("/predict", methods=["POST"])
def predict():
    data = request.json
    url = data["URL"]
    inputs = preprocess_input(url, tokenizer)

    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        prediction = predictions.argmax().item()
        if prediction == 0:
            prediction = "This is a Safe link, you can click on it."
        else:
            prediction = "This is a Phishing link, do not click on it!!!"

    return jsonify({"prediction": prediction})
