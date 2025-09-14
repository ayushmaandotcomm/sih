def evaluate_spam_model(model, test_data):
    # Evaluate the spam classification model on the test data
    model.eval()
    total = 0
    correct = 0

    with torch.no_grad():
        for text, label in test_data:
            output = model(text)
            predicted = output.argmax(dim=1)
            total += label.size(0)
            correct += (predicted == label).sum().item()

    accuracy = correct / total
    return accuracy

def main():
    # Load the trained spam classifier model
    model = load_model('path/to/trained/spam_classifier.pth')
    
    # Load the test dataset
    test_data = load_test_data('path/to/test_data')

    # Evaluate the model
    accuracy = evaluate_spam_model(model, test_data)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')

if __name__ == '__main__':
    main()