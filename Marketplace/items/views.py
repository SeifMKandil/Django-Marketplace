from django.shortcuts import render,get_object_or_404,redirect
from .models import Item, Category
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required


def search(request):
    query = request.GET.get('query', ' ')
    category_id = request.GET.get('category','')
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,'item/search.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':category_id,
    })


def detail(request, pk):
    item=get_object_or_404(Item, pk=pk)

    return render(request,'item/detail.html',{
        'item' : item
    } )

@login_required
def newItem(request):
    if request.method == 'POST':
        form=NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item=form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail',pk=item.id)
    else:
        form = NewItemForm()

    return render(request,'item/newitem.html',{
        'form' : form,
        'title': 'Add New Item',
    } )

@login_required
def deleteitem(request,pk):
    item= get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')


@login_required
def editItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/newitem.html', {
        'form': form,
        'title': 'Edit item',
    })