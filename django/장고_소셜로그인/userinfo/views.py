from django.shortcuts import render, redirect
from django.contrib import auth
from django.views import View
def login(request) :
    return render(request, 'login.html')

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        
    return redirect('login')

class KakaoLoginTest(View):
    def get(self, request):
        REST_API_KEY = 'b1e41852263db673755ffeb47424911c'
        REDIRECT_URI = 'http://localhost:8000'

        API_HOST = f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code'

        return redirect(API_HOST)

