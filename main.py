# Install required libraries
!pip install transformers datasets azureml-sdk

# Load and preprocess data
from datasets import load_dataset
from transformers import AutoTokenizer

dataset = load_dataset("amazon_reviews_multi", "en")
dataset = dataset.map(lambda x: {"sentiment": int(x["stars"] >= 4)})

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
def preprocess_function(examples):
    return tokenizer(examples["review_body"], truncation=True, padding="max_length", max_length=512)
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Fine-tune the model
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    save_strategy="epoch",
    logging_dir="./logs",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
)

trainer.train()

# Save the fine-tuned model
model.save_pretrained("./fine-tuned-distilbert-sentiment")
tokenizer.save_pretrained("./fine-tuned-distilbert-sentiment")

# Evaluate the model
from sklearn.metrics import accuracy_score, f1_score

predictions = trainer.predict(tokenized_dataset["test"])
y_pred = predictions.predictions.argmax(axis=1)
y_true = tokenized_dataset["test"]["sentiment"]

accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred, average="weighted")

print(f"Accuracy: {accuracy:.2f}")
print(f"F1-Score: {f1:.2f}")

# Deploy the model
from azureml.core import Workspace, Model
from azureml.core.webservice import AciWebservice

ws = Workspace.from_config()
model = Model.register(ws, model_name="sentiment-analysis", model_path="./fine-tuned-distilbert-sentiment")

aci_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)
service = Model.deploy(ws, "sentiment-analysis-service", [model], aci_config)
service.wait_for_deployment(show_output=True)

# Test the API
import requests

input_data = {"review": "This product is amazing! It works perfectly and is very easy to use."}
response = requests.post(service.scoring_uri, json=input_data)
print(response.json())
