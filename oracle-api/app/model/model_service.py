import torch
from transformers import BertTokenizer
from app.model.constants import BERT_BASE_CASED_MODEL, MAX_LEN, STATES
from app.model.state_mutability_classifier import StateMutabilityClassifier

class ModelService:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = BertTokenizer.from_pretrained(BERT_BASE_CASED_MODEL)
        classifier = StateMutabilityClassifier(len(STATES))
        # If want to locally load model
        # classifier.load_state_dict(torch.load("api/model/pytorch_model.bin", map_location=self.device))
        classifier = classifier.eval()
        self.classifier = classifier.to(self.device)

    def predict(self, text):
        encoded = self.tokenizer.encode_plus(
            text,
            max_length=MAX_LEN, add_special_tokens=True,
            return_token_type_ids=False, padding='max_length',
            return_attention_mask=True, return_tensors="pt",
        )

        with torch.no_grad():
            outputs = self.classifier(
                input_ids=encoded["input_ids"].to(self.device),
                attention_mask=encoded["attention_mask"].to(self.device),
            )
            _, preds = torch.max(outputs, dim=1)

        return STATES[preds]

model = ModelService()

def get_model():
    return model