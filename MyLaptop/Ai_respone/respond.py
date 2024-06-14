import torch
from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
model = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
import torch

data = pd.read_csv('Ai_respone/data1.csv')
data2 = pd.read_csv('Ai_respone/data2.csv')
data3 = pd.read_csv('Ai_respone/data3.csv')
data4 = pd.read_csv('Ai_respone/data4.csv')
data5 = pd.read_csv('Ai_respone/data5.csv')
data6 = pd.read_csv('Ai_respone/data6.csv')
data7 = pd.read_csv('Ai_respone/data7.csv')
data8 = pd.read_csv('Ai_respone/data8.csv')
data9 = pd.read_csv('Ai_respone/data9.csv')
data10 = pd.read_csv('Ai_respone/data10.csv')
data11 = pd.read_csv('Ai_respone/data11.csv')
data12 = pd.read_csv('Ai_respone/data12.csv')
data13 = pd.read_csv('Ai_respone/data13.csv')
data14 = pd.read_csv('Ai_respone/data14.csv')


def answer_question(input_question):
    questions = list(data.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings1.pt')

    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]


def answer_question2(input_question):
    questions = list(data2.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings2.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question3(input_question):
    questions = list(data3.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings3.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]



def answer_question4(input_question):
    questions = list(data4.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings4.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question5(input_question):
    questions = list(data5.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings5.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question6(input_question):
    questions = list(data6.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings6.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question7(input_question):
    questions = list(data7.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings7.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question8(input_question):
    questions = list(data8.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings8.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question9(input_question):
    questions = list(data9.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings9.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question10(input_question):
    questions = list(data10.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings10.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question11(input_question):
    questions = list(data11.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings11.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question12(input_question):
    questions = list(data12.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings12.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question13(input_question):
    questions = list(data13.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings13.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]

def answer_question14(input_question):
    questions = list(data14.loc[:,'question'])
    question_embeddings = torch.load('Ai_respone/question_embeddings14.pt')
    
    encoded_input = tokenizer(input_question, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]
def Allanswer_question(input_text):
    questions = []
    questions.append(answer_question(input_text))
    questions.append(answer_question2(input_text))
    questions.append(answer_question3(input_text))
    questions.append(answer_question4(input_text))
    questions.append(answer_question5(input_text))
    questions.append(answer_question6(input_text))
    questions.append(answer_question7(input_text))
    questions.append(answer_question8(input_text))
    questions.append(answer_question9(input_text))
    questions.append(answer_question10(input_text))
    questions.append(answer_question11(input_text))
    questions.append(answer_question12(input_text))
    questions.append(answer_question13(input_text))
    questions.append(answer_question14(input_text))
    
    encoded_questions = [tokenizer(question, return_tensors="pt")["input_ids"] for question in questions]
    question_embeddings = torch.cat([model(input_ids).pooler_output for input_ids in encoded_questions])

    encoded_input = tokenizer(input_text, return_tensors="pt")["input_ids"]
    input_embedding = model(encoded_input).pooler_output
    similarities = cosine_similarity(input_embedding.detach().numpy(), question_embeddings.detach().numpy())
    most_similar_index = similarities.argmax()
    return questions[most_similar_index]


def getAiresponedAll(input_question):
    answer = Allanswer_question(input_question)
    if data['question'].str.contains(answer).any():
        answer =  data[data['question'] == answer]['answer'].iloc[0]  
    if data2['question'].str.contains(answer).any():
        answer =  data2[data2['question'] == answer]['answer'].iloc[0]  
    if data3['question'].str.contains(answer).any():
        answer =  data3[data3['question'] == answer]['answer'].iloc[0]  
    if data4['question'].str.contains(answer).any():
        answer =  data4[data4['question'] == answer]['answer'].iloc[0]
    if data5['question'].str.contains(answer).any():
        answer =  data5[data5['question'] == answer]['answer'].iloc[0]
    if data6['question'].str.contains(answer).any():
        answer =  data6[data6['question'] == answer]['answer'].iloc[0]
    if data7['question'].str.contains(answer).any():
        answer =  data7[data7['question'] == answer]['answer'].iloc[0]
    if data8['question'].str.contains(answer).any():
        answer =  data8[data8['question'] == answer]['answer'].iloc[0]
    if data9['question'].str.contains(answer).any():
        answer =  data9[data9['question'] == answer]['answer'].iloc[0]
    if data10['question'].str.contains(answer).any():
        answer =  data10[data10['question'] == answer]['answer'].iloc[0]
    if data11['question'].str.contains(answer).any():
        answer =  data11[data11['question'] == answer]['answer'].iloc[0]
    if data12['question'].str.contains(answer).any():
        answer =  data12[data12['question'] == answer]['answer'].iloc[0]
    if data13['question'].str.contains(answer).any():
        answer =  data13[data13['question'] == answer]['answer'].iloc[0]
    if data14['question'].str.contains(answer).any():
        answer =  data14[data14['question'] == answer]['answer'].iloc[0]
    return str(answer)