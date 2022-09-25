from django.http import HttpResponseRedirect as hrr
from django.http import JsonResponse
from django.shortcuts import render

import requests
import json


# Create your views here.
def main(request):
	if 'auth' in request.COOKIES:
		return render(request, 'main.html')

	else:
		return hrr('/login')

def register(request):
	if request.method == 'POST':
		pass

	else:
		return render(request, 'register.html')

def login(request):
	if request.method == 'POST':
		headers = {
			'Content-Type': 'application/json',
			'language': 'ru',
			'Time-Zone': 'Asia/Almaty',
			'Partner-name': 'tips'
		}
		data = json.dumps({
			'login': request.POST['login'],
			'password': request.POST['password']
		})

		result = requests.post('https://api.yii2-stage.test.wooppay.com/v1/auth', data = data, headers = headers)

		if result.status_code == 200:
			result = json.loads(result.text)
			return render(request, 'login_post.html', {'api_info': result, 'token': result['token']})

	else:
		return render(request, 'login.html')

def history(request):
	if request.method == 'POST':
		headers = {

		}

		return render(request, 'history.html')
	return hrr('/login')

def v1(request):
	if request.method == 'POST':
		headers = {
			'Content-Type': 'application/json',
			'language': 'ru',
			'Time-Zone': 'Asia/Almaty',
			'Partner-name': 'tips',
			'Authorization': request.POST['token']
		}

		return JsonResponse(
			requests.post(
				request.POST['url'],
				data = json.dumps(request.POST['data']),
				headers = headers
			).text, safe = False
		)