# Contents of /janmarg/janmarg/backend/train/train_category.py

import os
import yaml
import torch
import torchvision.transforms as transforms
from torchvision import datasets, models
from torch import nn, optim
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report
from api.models.category_classifier import CategoryClassifier  # Assuming this is the model class

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def prepare_data(data_dir, batch_size):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    
    dataset = datasets.ImageFolder(root=data_dir, transform=transform)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return dataloader

def train_model(model, dataloader, criterion, optimizer, num_epochs):
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        
        for inputs, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(dataloader):.4f}')

def evaluate_model(model, dataloader):
    model.eval()
    all_preds = []
    all_labels = []
    
    with torch.no_grad():
        for inputs, labels in dataloader:
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.numpy())
            all_labels.extend(labels.numpy())
    
    print(classification_report(all_labels, all_preds))

def main():
    config = load_config('train/config/category.yaml')
    data_dir = config['data_dir']
    batch_size = config['batch_size']
    num_epochs = config['num_epochs']
    
    dataloader = prepare_data(data_dir, batch_size)
    
    model = CategoryClassifier(num_classes=config['num_classes'])
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config['learning_rate'])
    
    train_model(model, dataloader, criterion, optimizer, num_epochs)
    evaluate_model(model, dataloader)

if __name__ == '__main__':
    main()