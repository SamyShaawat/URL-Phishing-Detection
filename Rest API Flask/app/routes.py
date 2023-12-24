from flask import Blueprint, request, jsonify
from .model import model, tokenizer
from .utils import preprocess_input
import torch

routes_blueprint = Blueprint("routes", __name__)


@routes_blueprint.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    inputs = preprocess_input(text, tokenizer)

    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        prediction = predictions.argmax().item()

    return jsonify({"prediction": prediction})
