from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

class SpamClassifier:
    def __init__(self, model_name='distilbert-base-uncased', num_labels=2):
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_name)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

    def classify(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        probabilities = torch.softmax(logits, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
        confidence = probabilities[0][predicted_class].item()
        return predicted_class, confidence

    def load_model(self, model_path):
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)

    def save_model(self, model_path):
        self.model.save_pretrained(model_path)
        self.tokenizer.save_pretrained(model_path)