from django.shortcuts import render
import requests

def index(request):
    prediction = None
    if request.method == 'POST':
        query = request.POST.get('query')
        api_url = "https://23c5-103-218-25-193.in.ngrok.io/ask_question"
        response = requests.post(api_url, json={'question': query})
        prediction = response.json().get('answer')
    return render(request, 'index.html', {'prediction': prediction})
