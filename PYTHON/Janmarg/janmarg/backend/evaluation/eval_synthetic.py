def evaluate_synthetic_model(model, dataloader, device):
    model.eval()
    total_correct = 0
    total_samples = 0
    all_confidences = []
    all_labels = []

    with torch.no_grad():
        for images, labels in dataloader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)

            total_samples += labels.size(0)
            total_correct += (predicted == labels).sum().item()

            # Collect confidence scores
            confidences = torch.softmax(outputs, dim=1)
            all_confidences.extend(confidences.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    accuracy = total_correct / total_samples
    return accuracy, all_confidences, all_labels


def main():
    # Load model and data
    model = torch.load('path_to_your_model.pth')
    dataloader = ...  # Initialize your dataloader here
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    accuracy, confidences, labels = evaluate_synthetic_model(model, dataloader, device)

    print(f'Accuracy: {accuracy * 100:.2f}%')
    # Further evaluation metrics can be added here


if __name__ == "__main__":
    main()