import torch
from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer
import pandas as pd

# Load tokenizer and model
tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
model = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")

# data = pd.read_csv('Ai_respone/data1.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings1.pt')

# data = pd.read_csv('Ai_respone/data2.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings2.pt')

# data = pd.read_csv('Ai_respone/data3.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings3.pt')

# data = pd.read_csv('Ai_respone/data4.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings4.pt')

data = pd.read_csv('Ai_respone/data5.csv')
questions = list(data.loc[:,'question'])
encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

torch.save(question_embeddings, 'Ai_respone/question_embeddings5.pt')

# data = pd.read_csv('Ai_respone/data6.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings6.pt')

# data = pd.read_csv('Ai_respone/data7.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings7.pt')

# data = pd.read_csv('Ai_respone/data8.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings8.pt')


# data = pd.read_csv('Ai_respone/data9.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings9.pt')

# data = pd.read_csv('Ai_respone/data10.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings10.pt')

# data = pd.read_csv('Ai_respone/data11.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings11.pt')

# data = pd.read_csv('Ai_respone/data12.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings12.pt')

# data = pd.read_csv('Ai_respone/data13.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings13.pt')

# data = pd.read_csv('Ai_respone/data14.csv')
# questions = list(data.loc[:,'question'])
# encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
# question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

# torch.save(question_embeddings, 'Ai_respone/question_embeddings14.pt')