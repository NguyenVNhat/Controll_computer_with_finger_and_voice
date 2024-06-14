import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Define the function
def answer_question13(input_question):
    # Read questions from the text file
    with open('Ai_respone/data14.txt', 'r', encoding='utf-8') as file:
        questions = file.readlines()
    
    # Strip any leading/trailing whitespace characters from each question
    questions = [question.strip() for question in questions]
    
    # Load the question embeddings
    question_embeddings = torch.load('Ai_respone/question_embeddings14.pt')
    
    # Encode the input question
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    
    # Compute similarities
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    
    return questions[most_similar_index]

# Example usage:
input_question = "Dã tràng se cát"
print(answer_question13(input_question))
