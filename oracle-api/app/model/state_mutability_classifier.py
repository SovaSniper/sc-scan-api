from transformers import BertModel
from torch import nn
from app.model.constants import PRE_TRAINED_MODEL_NAME

class StateMutabilityClassifier(nn.Module):
  def __init__(self, n_classes):
    super(StateMutabilityClassifier, self).__init__()
    self.bert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME, return_dict=False)
    self.drop = nn.Dropout(p=0.3)
    self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

  def forward(self, input_ids, attention_mask):
    _, pooled_output = self.bert(
      input_ids=input_ids,
      attention_mask=attention_mask
    )
    output = self.drop(pooled_output)
    return self.out(output)
