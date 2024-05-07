import json
import torch
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Load intents data
with open('intents_1.json', 'r') as json_data:
    intents = json.load(json_data)

# Load model
FILE = "data.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]
model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

# Load prompts file
with open('prompts.json', 'r') as json_data:
    prompts_data = json.load(json_data)

# Initialize lists to store ground truth and predicted intents
y_true = []
y_pred = []

# Function to preprocess input sentence
def preprocess_sentence(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)
    return X

# Perform inference on prompts
for prompt_data in prompts_data:
    prompt = prompt_data['prompt']
    intent = prompt_data['intent']

    # Predict intent for the prompt
    X = preprocess_sentence(prompt)
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    predicted_intent = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # Check if predicted intent matches ground truth intent
    if predicted_intent == intent:
        y_true.append(1)  # Ground truth and predicted intent match
    else:
        if prob > 0.75:
            y_true.append(1)
        else:
            y_true.append(0)  # Ground truth and predicted intent don't match

    if intent == "false":
        y_pred.append(0)
    else:
        y_pred.append(1)

# Create confusion matrix

confusion_mat = confusion_matrix(y_true, y_pred, labels=[0, 1])

# Print confusion matrix
print("Confusion Matrix:")
print(confusion_mat)

# If you want to save the confusion matrix to a file, you can do so here
np.savetxt('confusion_matrix.csv', confusion_mat, delimiter=',', fmt='%d')



# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.set(font_scale=1.2)  # Adjust font scale if needed
sns.heatmap(confusion_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['False', 'True'], yticklabels=['False', 'True'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()


