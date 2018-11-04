from django.shortcuts import render, HttpResponse
from main.models import CompanyInfo, PortfolioItem, PortfolioItemImages, PortfolioItemImagesSmall,PortfolioItemImagesBig
from django.conf import settings
from templated_email import send_templated_mail

# Create your views here.


def company_info():
    context = {
        'company_tel': settings.PHONE_NUMBER,
        'company_email': settings.CONTACT_EMAIL,
        'company_address': settings.ADDRESS

    }
    return context


def index_view(request):
    portfolio_items = PortfolioItem.objects.all()
    context = {
        'company_tel': settings.PHONE_NUMBER,
        'company_email': settings.CONTACT_EMAIL,
        'company_address': settings.ADDRESS,
        'portfolio_items': portfolio_items,
    }
    return render(request, 'main_index.html', context)


def portfolio_details_view(request, project_id):
    portfolio_item = PortfolioItem.objects.get(id=project_id)
    images_big = PortfolioItemImagesBig.objects.filter(item=portfolio_item)
    images_small = PortfolioItemImagesSmall.objects.filter(item=portfolio_item)
    context = company_info()
    context.update({
        'images_small': images_small,
        'images_big': images_big,
        'portfolio_item': portfolio_item
    })

    return render(request, 'portfolio_details.html', context)


def contacts(request):
    context = company_info()
    context.update({
        'contacts': 'contacts'
    })
    return render(request, 'contacts.html', context)


def send_email(request, template, from_, to, context):
    send_templated_mail(template_name=template,
                        from_email=from_,
                        recipient_list=to,
                        context=context,
                        )
    return HttpResponse()


def message_from_site(request):
    if request.method == 'POST':
        data = request.POST
        name_ = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')
        subject = data.get('subject')
        return HttpResponse()


def goto_compet(request):
    context = company_info()
    portfolio_items = PortfolioItem.objects.all()
    context.update({
        'item_goto': 'compet',
        'portfolio_items': portfolio_items
    })
    return render(request, 'main_index.html', context)


def goto_project(request):
    context = company_info()
    portfolio_items = PortfolioItem.objects.all()
    context.update({
        'item_goto': 'project',
        'portfolio_items': portfolio_items
    })
    return render(request, 'main_index.html', context)


def goto_why_us(request):
    context = company_info()
    portfolio_items = PortfolioItem.objects.all()
    context.update({
        'item_goto': 'why_us',
        'portfolio_items': portfolio_items
    })
    return render(request, 'main_index.html', context)


def goto_directions(request):
    context = company_info()
    portfolio_items = PortfolioItem.objects.all()
    context.update({
        'item_goto': 'directions',
        'portfolio_items': portfolio_items
    })
    return render(request, 'main_index.html', context)


