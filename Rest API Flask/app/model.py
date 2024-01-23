from transformers import AutoModelForSequenceClassification, AutoTokenizer


def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(
        "./models/savedModel_20000"
    )
    tokenizer = AutoTokenizer.from_pretrained("./models/savedTokenizer_20000")
    return model, tokenizer


model, tokenizer = load_model()
