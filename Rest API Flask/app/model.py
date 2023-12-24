from transformers import AutoModelForSequenceClassification, AutoTokenizer


def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(
        "./models/savedModel_10000"
    )
    tokenizer = AutoTokenizer.from_pretrained("./models/savedTokenizer_10000")
    return model, tokenizer


model, tokenizer = load_model()
