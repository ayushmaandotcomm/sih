import os
import yaml
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.utils.data import DataLoader, Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

class SpamDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels
        self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(text, return_tensors='pt', padding='max_length', truncation=True, max_length=512)
        return {**encoding, 'labels': torch.tensor(label)}

def load_data(config):
    df = pd.read_csv(config['data_path'])
    texts = df['text'].tolist()
    labels = df['label'].tolist()
    return train_test_split(texts, labels, test_size=config['test_size'], random_state=42)

def train_model(train_loader, model, optimizer, device):
    model.train()
    for batch in train_loader:
        optimizer.zero_grad()
        input_ids = batch['input_ids'].squeeze(1).to(device)
        attention_mask = batch['attention_mask'].squeeze(1).to(device)
        labels = batch['labels'].to(device)
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

def evaluate_model(test_loader, model, device):
    model.eval()
    predictions, true_labels = [], []
    with torch.no_grad():
        for batch in test_loader:
            input_ids = batch['input_ids'].squeeze(1).to(device)
            attention_mask = batch['attention_mask'].squeeze(1).to(device)
            labels = batch['labels'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            preds = torch.argmax(logits, dim=1)
            predictions.extend(preds.cpu().numpy())
            true_labels.extend(labels.cpu().numpy())
    return accuracy_score(true_labels, predictions)

def main():
    with open('janmarg/backend/train/config/spam.yaml') as f:
        config = yaml.safe_load(f)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config['learning_rate'])

    texts_train, texts_test, labels_train, labels_test = load_data(config)
    train_dataset = SpamDataset(texts_train, labels_train)
    test_dataset = SpamDataset(texts_test, labels_test)

    train_loader = DataLoader(train_dataset, batch_size=config['batch_size'], shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=config['batch_size'], shuffle=False)

    for epoch in range(config['num_epochs']):
        train_model(train_loader, model, optimizer, device)
        accuracy = evaluate_model(test_loader, model, device)
        print(f'Epoch {epoch + 1}/{config["num_epochs"]}, Accuracy: {accuracy:.4f}')

    model.save_pretrained(config['model_save_path'])

if __name__ == '__main__':
    main()