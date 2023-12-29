from transformers import AutoModelForSequenceClassification, AutoTokenizer


def load_model():
    model = AutoModelForSequenceClassification.from_pretrained(
        "./models/savedModel_11430"
    )
    tokenizer = AutoTokenizer.from_pretrained("./models/savedTokenizer_11430")
    return model, tokenizer


model, tokenizer = load_model()
