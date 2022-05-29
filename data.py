import html
import requests

url = 'https://opentdb.com/api.php?amount=10&type=boolean'
respond = requests.get(url = url)
questions = respond.json()['results']
question_data = [{'text':html.unescape(question['question']), 'answer':question['correct_answer']} for question in questions]
