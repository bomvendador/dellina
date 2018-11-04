from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from main.models import User, Role, UserProfile, PortfolioItem, PortfolioItemImages, PortfolioItemImagesBig, PortfolioItemImagesSmall
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def dash_panel_login_view(request):

    context = {
    }
    return render(request, 'login.html', context)


# @login_required(redirect_field_name=None, login_url='/dash_panel')
def dash_panel_index_view(request):
    if request.method == 'POST':
        login_ = request.POST['login']
        password = request.POST['password']
        # user = User()
        # user.password = password
        # user.email = email
        # user.save()
        print(login_ + ' ' + password)
        user = authenticate(username=login_, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print('logged')

            return HttpResponse(user.id)
        else:
            return HttpResponse('error')

    context = {}
    print("dfsdfsdfsdf")
    return render(request, 'base_dash_panel.html', context)


def check_login(request):

    context = {}
    print("dfsdfsdfsdf")
    return render(request, 'base_dash_panel.html', context)


@login_required(redirect_field_name=None, login_url='/dash_panel')
def add_user(request):
    context = {
        'roles': Role.objects.all()

    }

    return render(request, 'add_user.html', context)


@login_required(redirect_field_name=None, login_url='/dash_panel')
def portfolio_list(request):
    context = {
        'portfolio_list': PortfolioItem.objects.all()

    }

    return render(request, 'portfolio_list.html', context)


@login_required(redirect_field_name=None, login_url='/dash_panel')
def add_portfolio_item(request):

    if request.method == 'POST':
        data = request.POST
        name_ = data.get('name')
        short_name = data.get('short_name')
        client = data.get('client')
        period = data.get('period')
        sum_ = data.get('sum')
        vol = data.get('vol')
        project_id = data.get('project_id')
        if project_id:
            item = PortfolioItem.objects.get(id=project_id)
        else:
            item = PortfolioItem()
        item.client = client
        item.name = name_
        item.short_name = short_name
        item.period = period
        item.sum = sum_
        item.vol = vol
        item.save()
        image_num = 1

        for file_key in request.FILES.keys():
            print('fk' + str(file_key))
            for file in request.FILES.getlist(file_key):
                if image_num == 1:
                    item_img = PortfolioItemImages()
                    item_img.image = file
                    item_img.item = item
                    item_img.save()
                    item.main_image = file
                    item.save()
                elif image_num == 2 or image_num == 4 or image_num == 6 or image_num == 8:
                    item_img = PortfolioItemImagesBig()
                elif image_num == 3 or image_num == 5 or image_num == 7 or image_num == 9:
                    item_img = PortfolioItemImagesSmall()
                if image_num > 1:
                    item_img.item = item
                    item_img.name = file
                    item_img.image = file
                    # if first_time:
                    #     item.main_image = file
                    #     item.save()
                    #     first_time = False
                    item_img.save()
                image_num += 1
        return HttpResponse()



    # if request.method == 'POST':
    #     name_ = request.POST['name']
    #     client = request.POST['client']
    #     period = request.POST['period']
    #     sum_ = request.POST['sum']
    #     vol = request.POST['vol']
    #     item = PortfolioItem()
    #     item.client = client
    #     item.name = name_
    #     item.period = period
    #     item.sum = sum_
    #     item.vol = vol
    #     item.save()
    #     return HttpResponse('ok')
    context = {
        # 'roles': Role.objects.all()

    }

    return render(request, 'add_portfolio_item.html', context)


def portfolio_item_details(request, project_id):
    portfolio_item = PortfolioItem.objects.get(id=project_id)
    images_big = PortfolioItemImagesBig.objects.filter(item=portfolio_item)
    images_small = PortfolioItemImagesSmall.objects.filter(item=portfolio_item)
    image_main = PortfolioItemImages.objects.get(item=portfolio_item)
    context = {
        'portfolio_item': portfolio_item,
        'images_big': images_big,
        'images_small': images_small,
        'image_main': image_main
    }
    return render(request, 'portfolio_item_details.html', context)


def del_foto_from_gallery(request):
    if request.method == 'POST':
        data = request.POST
        project_id = data.get('project_id')
        item = PortfolioItem.objects.get(id=project_id)
        PortfolioItemImagesSmall.objects.filter(item=item).delete()
        PortfolioItemImagesBig.objects.filter(item=item).delete()
        item.main_image = ''
        item.save()
        return HttpResponse('ok')

