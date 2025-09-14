from PIL import Image

class CategoryClassifier:
    def __init__(self, model_path: str):
        import torch
        from torchvision import models, transforms

        self.device = torch.device("cpu")
        # Example: using a ResNet18 architecture
        self.model = models.resnet18(pretrained=False)
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, 7)  # 7 categories
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.eval()
        self.model.to(self.device)
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def classify(self, image_path: str):
        import torch
        image = Image.open(image_path).convert("RGB")
        image = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(image)
            _, predicted = torch.max(outputs, 1)

        return predicted.item()

    def get_category_label(self, category_index: int):
        categories = ['news-photo', 'document', 'meme', 'ad', 'screenshot', 'portrait', 'scene']
        return categories[category_index] if category_index < len(categories) else 'unknown'