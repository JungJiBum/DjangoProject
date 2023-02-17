from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import customer
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, 'sign.html')
    elif request.method == "POST":
        # 회원가입 처리 코드 -> 아래 코드에서 key가 없으면 에러가 발생하니 get메소드 사용하여 에러처리 해주자
        # username = request.POST['username']
        # password = request.POST['password']
        # re_password = request.POST['re-password']

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)

        res_data = {}  # 프론트에 던져줄 응답 데이터

        # 모든 값을 입력해야함
        if not (username and password and re_password and useremail):  # None은 False로 인식
            res_data['error'] = "모든 값을 입력해야 한다."
        # 비밀번호가 다르면 리턴
        elif password != re_password:
            # return HttpResponse("비밀번호가 다름")
            res_data['error'] = "비밀번호가 다름"
        # 같으면 저장
        else:
            res_data['error'] = "생성 완료"
            # 위 정보들로 인스턴스 생성
            user = customer(
                username=username,
                password=make_password(password),
                useremail=useremail
            )
            # 저장
            user.save()
    return render(request, 'sign.html', res_data)


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # 전송받은 이메일 비밀번호 확인
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 유효성 처리
        res_data = {}
        if not (username and password):
            res_data['error'] = "모든 칸을 입력해주세요."
        else:
            # 기존(DB)에 있는 customer 모델과 같은 값인 걸 가져온다.
            user = customer.objects.get(username=username)  # (필드명 = 값)
            # 비밀번호가 일치하는지 체크.
            if check_password(password, user.password):
                # 응답 데이터 세션에 user pk값인 id 추가. 나중에 쿠키에 저장됨
                request.session['user'] = user.id
                # 리다이렉트
                return redirect('/')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."
        return render(request, 'login.html', res_data)  # 응답 데이터 res_data로 전달


def home(request):
    # login함수에서 추가해준 request.session['user'] = customer.id
    user_pk = request.session.get('user')

    if user_pk:  # 세션에 user_pk 정보가 존재하면
        login_user = customer.objects.get(pk=user_pk)
        return HttpResponse(login_user.username+" 님이 접속하였습니다.")
    return HttpResponse("{} 님 환영합니다.".format(user_pk))


def logout(request):
    if request.session['user']:  # 로그인 중 이라면
        del (request.session['user'])

    return redirect('/')
