def evaluate_category_model(model, dataloader, device):
    model.eval()
    total_correct = 0
    total_samples = 0
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for images, labels in dataloader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            _, preds = torch.max(outputs, 1)

            total_correct += (preds == labels).sum().item()
            total_samples += labels.size(0)

            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    accuracy = total_correct / total_samples
    return accuracy, all_preds, all_labels


def main():
    import torch
    from torchvision import datasets, transforms
    from torch.utils.data import DataLoader
    from backend.api.models.category_classifier import CategoryClassifier

    # Load model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = CategoryClassifier()
    model.load_state_dict(torch.load('path/to/model.pth'))
    model.to(device)

    # Prepare dataloader
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    test_dataset = datasets.ImageFolder('path/to/test/data', transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    # Evaluate model
    accuracy, preds, labels = evaluate_category_model(model, test_loader, device)
    print(f'Accuracy: {accuracy * 100:.2f}%')


if __name__ == "__main__":
    main()