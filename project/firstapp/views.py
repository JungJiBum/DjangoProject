from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from . import craw
from .models import webtoonData
import re
from django.core.paginator import Paginator


def main(request):
    lists = webtoonData.objects.all()   # 모든 데이터 조회
    paginator = Paginator(lists, 10)    # 글을 10개씩 출력
    # 메인으로 GET 요청이 들어오면 page 파라미터를 읽는다. 없는경우 1번 페이지를 디폴트세팅
    page = int(request.GET.get('page', 1))
    # class 'django.core.Paginator.Page'를 리턴한다.
    board_list = paginator.get_page(page)
    return render(request, 'main.html', {'title': '웹툰 항목', 'board_list': board_list})
    # data = {'lists': lists}
    # return render(request, 'main.html', data)


@csrf_exempt
def crawling(request):
    url = request.POST['webtoon_url']
    info = craw.data_print(url)

    # DB에 저장
    for t, l in info.items():
        numbers = re.sub(r'[^0-9]', '', l)
        webtoonData(title=t, title_numbers=numbers, week=l[-3:]).save()
    return HttpResponseRedirect(reverse('main'))


def deleteData(request, idx):
    db_article = webtoonData.objects.get(id=idx)
    db_article.delete()
    return HttpResponseRedirect(reverse('main'))


def viewData(request, idx):
    img = craw.img_view()
    db_article = webtoonData.objects.get(id=idx)
    print(type(img), type(db_article))
    src = img.get(str(db_article))  # 이미지 주소 값 가져오는중

    return HttpResponseRedirect(src)
