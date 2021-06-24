from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from auth.token import account_activation_token

# Create your views here.
def signup(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 비밀번호 확인도 같다면
        if request.POST['password1'] ==request.POST['password2']:
            # 유저 만들기
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.is_active = False # 유저 비활성화
            user.save()
            current_site = get_current_site(request) 
            message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return redirect("home")

    # 포스트 방식 아니면 페이지 띄우기
    return render(request, 'accounts/signup.html')



def login(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 정보 가져와서 
        username = request.POST['username']
        password = request.POST['password']
        # 로그인
        user = auth.authenticate(request, username=username, password=password)
        # 성공
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        # 실패
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 유저 로그아웃
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')

# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("home")
    else:
        return render(request, 'home.html', {'error' : '계정 활성화 오류'})