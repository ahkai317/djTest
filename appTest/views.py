from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('''
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>

            <!-- bootstrap -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        </head>

        <body>

            <nav class="navbar bg-dark navbar-dark p-3 navbar-expand-lg">
                <div class="container">
                    <a href="" class="navbar-brand">Zentropy</a>

                    <!-- component -->
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                        data-bs-target="#navbarSupportedContent">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item">
                                <a href="" class="nav-link">About</a>
                            </li>
                            <li class="nav-item">
                                <a href="" class="nav-link">Q & A</a>
                            </li>
                            <li class="nav-item">
                                <a href="" class="nav-link">Contact Us</a>
                            </li>
                            <li class="nav-item">
                                <a href="" class="nav-link">Support Us</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <div class="p-5 text-center border-bottom">
                <h1>Bootstrap Test</h1>
                <div class="col-lg-6 mx-auto">
                    <p class="lead m-4">
                        test 00test 00test 00test 00test 00,test 00test 00
                        test 00test 00test 00,test 00test 00,test 00test 0
                        0,test 00test 00test 00test 00test 00test.
                    </p>
                    <button class="btn btn-primary btn-lg">See more</button>
                </div>
            </div>

            <div class="p-5">
                <div class="container">
                    <div class="row g-4">
                        <div class="col-lg">
                            <div class="card shadow-lg">
                                <!-- <img src="zentropy.png" alt="" class="card-img-top"> -->
                                <img src="https://picsum.photos/300/200/?random=10">
                                <div class="card-body">
                                    <h3 class="card-title">Logo 01</h3>
                                    <p class="card-text">Test logo ver.01</p>
                                    <button class="btn btn-primary">Click</button>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg">
                            <div class="card shadow-lg">
                                <img src="https://picsum.photos/300/200/?random=15">
                                <div class="card-body">
                                    <h3 class="card-title">Logo 01</h3>
                                    <p class="card-text">Test logo ver.01</p>
                                    <button class="btn btn-primary">Click</button>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg">
                            <div class="card shadow-lg">
                                <img src="https://picsum.photos/300/200/?random=20">
                                <div class="card-body">
                                    <h3 class="card-title">Logo 01</h3>
                                    <p class="card-text">Test logo ver.01</p>
                                    <button class="btn btn-primary">Click</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <footer class="p-4 border-top">
                <div class="container align-items-center justify-content-between d-flex">
                    <p class="mb-0 text-muted">
                        &copy;2022 Zentropy. All Right Reserved.
                    </p>
                    <ul class="nav">
                        <li class="nav-item">
                            <a href="" class="nav-link text-muted">More Info</a>
                        </li>
                        <li class="nav-item">
                            <a href="" class="nav-link text-muted">Back</a>
                        </li>
                    </ul>
                </div>
            </footer>

            <!-- bootstrap -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ"
                crossorigin="anonymous"></script>
        </body>

        <style>
            .my-col {
                background-color: bisque;
                height: 400px;
            }
        </style>

        </html>
''')


def user_list(request):
    # return HttpResponse('User list')
    return render(request, 'user_list.html')

def user_add(request):
    # return HttpResponse('Add more users...')
    return render(request, 'user_add.html')

# ======================================================================
from appTest.models import StockTest
#from appTest import models
def orm(request):
    # test for ORM database operations

    ## 1. CREATE
    # models.StockTest.objects.create() # from appTest import models
    # StockTest.objects.create(date='2021-10-25', stock='2330.TW',
    #                          open_p=597.0, high_p=597.0, low_p=590.0, close_p=593.0, adj_close=587.372986, volume=16785568)

    ## 2. DELETE
    # StockTest.objects.filter(stock='2330.TW').delete() # .filter() ?????? WHERE
    # StockTest.objects.all().delete()

    ## 3. SELECT (type = queryset ?????? list in list)
    # data_list = StockTest.objects.all()
    # print(data_list)

    # x = []
    # for obj in data_list:
    #     x = [obj.id, obj.date, obj.stock, obj.open_p, obj.high_p,
    #           obj.low_p, obj.close_p, obj.adj_close, obj.volume]
    #     print(x)

    # data_list2 = StockTest.objects.filter(id=2)
    # print(data_list2)

    ## 4. UPDATE
    # StockTest.objects.all().update(stock='2330.Taiwan')
    # StockTest.objects.filter(id=2).update(stock='2330.TW')

    # return HttpResponse('Succeed'+ str(x))
    return HttpResponse('<h1> SUCCEED~ d(OuO </h1>')

# ======================================================================
def tpl(request):

    name = '??????'
    role = ['?????????', '?????????', '????????????']
    user_info = {'name': '??????', 'salary': 8000, 'role': '??????'}

    data_list = [
        {'name': '??????', 'salary': 8000, 'role': '??????'},
        {'name': '??????', 'salary': 8000, 'role': '??????'},
        {'name': 'pinju', 'salary': '?????????????????????????????????', 'role': '???????????????'}
    ]

    return render(request, 'tpl.html', {
            'n1': name, 'n2': role, 'n3': user_info, 'n4': data_list
        }
    )

# ======================================================================
def news(request):
    # 1. ?????????????????? or ???????????????
    # 2. ??????, ????????????
    # 2-1 ???????????????(?????????????????????)???????????? :
    # https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20220330&st=env
    # ????????????: https://ctee.com.tw/livenews/aj
    # 2-2 import requests
    import requests
    from bs4 import BeautifulSoup
    # =======================================================================
    # pos = requests.post('https://www.google.com/recaptcha/api2/reload?k=6LfPEYYaAAAAAF89tLx5E86IDmM2XVD9oyWFL0Ga')
    # print(pos)

    # res = requests.get('https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20220330&st=env')
    # data_lists = res.json()
    # print(res)
    # ======================================================================

    # ??????????????????
    re = requests.get('https://ctee.com.tw/livenews/aj/page/1')
    soup = BeautifulSoup(re.text,'html.parser')
    content = soup.select('div.item-content')
    # url01 = soup.select('div.item-content')[0].select('a')[1]['href']
    # title01 = soup.select('div.item-content')[0].select('a')[1].text
    url_list = []
    title_list = []
    for i in range(0,50):
        url_list.append(soup.select('div.item-content')[i].select('a')[1]['href'])
        title_list.append(soup.select('div.item-content')[i].select('a')[1].text)

    news_dict = dict(zip(url_list, title_list))

    return render(request, 'news.html', {'url': url_list, 'title': title_list, 'news': news_dict})

# ======================================================================
from django.shortcuts import redirect

def something(request):
    # 1. ?????????????????? GET/POST
    print(request.method)

    # 2. ???URL???????????? /something/?n1=123&n2=999
    print(request.GET) # <QueryDict: {n1=123,n2=999}>

    # 3. ????????????????????????
    print(request.POST) # <QueryDict: {}>

    # 4. [??????] HttpResponse('????????????'), ??????????????????????????????
    # return HttpResponse('????????????')

    # 5. [??????] ????????????HTML?????????, ???views.py????????????, ???url.py??????????????????
    # return render(request, 'something.html', {'title': '??????'})

    # 6. [??????] ????????????????????????????????????
    return redirect('https://www.google.com')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    # if ???????????????(??????GET????????????????????????)
    elif request.method == 'POST':
        print(request.GET)
        # ??????????????????django?????????????????????????????????????????????
        print(request.POST)

        username = request.POST.get('user')
        password = request.POST.get('pwd')

        if username == 'admin' and password == 'admin':
            # return HttpResponse('<h1> SUCCEED~ d(OuO </h1>')
            return redirect('https://www.google.com')
        else:
            error_msg = 'User Not Found... (QnQ'
            # return HttpResponse('<h1> User Not Found... (QnQ </h1>')
            return render(request, 'login.html', { 'error_msg': error_msg }) # ????????????, ?????????????????????

# ======================================================================
from appTest.models import UserInfoTest

def info_list(request):

    user_data_list = UserInfoTest.objects.all()
    print(user_data_list) # <QuerySet [<UserInfoTest: UserInfoTest object (1)>]>
    print(user_data_list[0].name) # admin
    print(user_data_list[0].password) # admin

    # return HttpResponse('<h1> SUCCEED~ d(OuO </h1>')
    return render(request, 'info_list.html', {'user_data_list': user_data_list})

def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')

    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')

    UserInfoTest.objects.create(name=name, password=pwd, age=age)

    # return HttpResponse('<h1> HELLO, New User~ d(OuO </h1>')
    return redirect('/info/list')

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfoTest.objects.filter(id=nid).delete()
    return HttpResponse('<h1> User has been delete~ d(OuO </h1>')

# ======================================================================
# ======================================================================
# 0410 DRF --from: Django-Vue??????????????????

# # 0410 DRF????????????
# def article_list(request):
#     return HttpResponse("Hello World!")

from appTest.models import Article
from appTest.serializers import ArticalListSerializer

from django.http import JsonResponse

# def article_list(request):
#     articles = Article.objects.all()
#     serializer = ArticalListSerializer(articles, many=True)
#     return JsonResponse(serializer.data, safe=False)

# 0415 APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticalListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticalListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##0415 ??????class???view
##from rest_framework.response import Response ?????????
from rest_framework.views import APIView
##from rest_framework import status ?????????
from django.http import Http404
## from article.models import Article ?????????(appTest)
from appTest.serializers import ArticleDetailSerializer
#class ArticleDetail(APIView):
#    '''????????????View'''
#    def get_object(self, pk):
#        '''???????????????'''
#        try:
#            # pk = primary key, ????????? id
#            return Article.objects.get(pk=pk)
#        except:
#            raise Http404
#
#    def get(self, request, pk):
#        article = self.get_object(pk)
#        serializer = ArticleDetailSerializer(article)
#        # ?????? Json ??????
#        return Response(serializer.data)
#
#    def put(self, request, pk):
#        article = self.get_object(pk)
#        serializer = ArticleDetailSerializer(article, data=request.data)
#        # ?????????????????????????????????, ?????????????????? 400
#        if serializer.is_valid():
#            # ?????????????????????????????????????????????, ?????????????????????
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, pk):
#        article = self.get_object(pk)
#        article.delete()
#        # ???????????????, ??????204
#        return Response(status=status.HTTP_204_NO_CONTENT)


#0416 ???DRF Mixin ???????????????CRUD??????
from rest_framework import mixins
from rest_framework import generics

class ArticleDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    '''????????????View'''
    queryset = Article.objects.all()
    serializer_class =