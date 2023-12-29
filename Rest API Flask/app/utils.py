def preprocess_input(text, tokenizer, max_length=128):
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=max_length,
        padding="max_length",  # Changed from pad_to_max_length
        truncation=True,  # Explicitly enable truncation
        return_attention_mask=True,
        return_tensors="pt",
    )
    return inputs
