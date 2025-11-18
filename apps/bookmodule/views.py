
from django.shortcuts import render 
from django.http import HttpResponse
from .models import Booklap
from django.db.models import Q
from .models import Booklap, Address, Student
from .models import Booklab
from django.db.models import Sum
from .models import Publisher
from django.db.models import Min
from .models import Publisher, Booklab
from django.db.models import Avg, Min, Max
from django.db.models import Count, Q


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html" , {"name": name})  



 
def index2(request, val1 = 0):  
    return HttpResponse("value1 = "+str(val1))
def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)


def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links_view(request):
    return render(request, 'bookmodule/html5/links.html')

def formatting_view(request):
    return render(request, 'bookmodule/html5/formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/html5/listing.html')

def tabels_view(request):
    return render(request, 'bookmodule/html5/tabels.html')

def search_view(request):
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')




# Task 3
def simple_query(request):
    mybooks = Booklap.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookoflist.html', {'books': mybooks})

# Task 4
def complex_query(request):
    mybooks = (
        Booklap.objects
        .filter(author__isnull=False)
        .filter(title__icontains='and')  
        .filter(edition__gte=2)
        .exclude(price__lte=100)
    )[:10]
    if mybooks:
     return render(request, 'bookmodule/bookoflist.html', {'books': mybooks})
    return render(request, 'bookmodule/index.html')


def lab8_task1(request):
    books = Booklap.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': books})

def lab8_task2(request):
    books = Booklap.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': books})


def lab8_task3(request):
    books = Booklap.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': books})


def lab8_task4(request):
    books = Booklap.objects.order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': books})

from django.db.models import Count, Sum, Avg, Max, Min

def lab8_task5(request):
    data = Booklap.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/lab8_task5.html', {'data': data})

def lab8_task7(request):
    data = Address.objects.annotate(total_students=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'data': data})




def task1_view(request):
    books = Booklab.objects.all()
    total_qty = books.aggregate(total=Sum('quantity'))['total'] or 0

    for book in books:
        if total_qty > 0:
            book.availability_percent = round((book.quantity / total_qty) * 100, 2)
        else:
            book.availability_percent = 0

    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

def task2_view(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('booklab__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})


def task3_view(request):
    oldest_books = []
    publishers = Publisher.objects.all()

    for pub in publishers:
        oldest = pub.booklab_set.order_by('pubdate').first()
        if oldest:
            oldest_books.append({'publisher': pub, 'book': oldest})

    return render(request, 'bookmodule/lab9_task3.html', {'oldest_books': oldest_books})


def task4_view(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('booklab__price'),
        min_price=Min('booklab__price'),
        max_price=Max('booklab__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

def task5_view(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('booklab', filter=Q(booklab__rating__gte=4))
    )
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})


def task6_view(request):
    publishers = Publisher.objects.annotate(
        book_count=Count(
            'booklab',
            filter=Q(booklab__price__gt=50, booklab__quantity__lt=5, booklab__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})





# ======================================================
# PART 1 — CRUD بدون Django Forms
# ======================================================
# ======================================================
# PART 1 — CRUD بدون Django Forms (على Booklab)
# ======================================================
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booklab
from .forms import BooklabForm

def listbooks_p1(request):
    books = Booklab.objects.all()
    return render(request, 'bookmodule/lab9_part1/listbooks.html', {'books': books})


def addbook_p1(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')   
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        pubdate = request.POST.get('pubdate')
        rating = request.POST.get('rating')

        if quantity == '':
            quantity = 1
        if rating == '':
            rating = 1
        if price == '':
            price = 0.0

        Booklab.objects.create(
            title=title,
            price=float(price),
            quantity=int(quantity),
            pubdate=pubdate,
            rating=int(rating),
        )
        return redirect('lab9_part1_listbooks')

    return render(request, 'bookmodule/lab9_part1/addbook.html')


def editbook_p1(request, id):
    book = get_object_or_404(Booklab, id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        pubdate = request.POST.get('pubdate')
        rating = request.POST.get('rating')

        if price != '':
            book.price = float(price)
        if quantity != '':
            book.quantity = int(quantity)
        if pubdate != '':
            book.pubdate = pubdate
        if rating != '':
            book.rating = int(rating)

        book.save()
        return redirect('lab9_part1_listbooks')

    return render(request, 'bookmodule/lab9_part1/editbook.html', {'book': book})


def deletebook_p1(request, id):
    book = get_object_or_404(Booklab, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('lab9_part1_listbooks')

    return render(request, 'bookmodule/lab9_part1/deletebook.html', {'book': book})


# ======================================================
# PART 2 — CRUD باستخدام Django Forms (على Booklab)
# ======================================================

def listbooks_p2(request):
    books = Booklab.objects.all()
    return render(request, 'bookmodule/lab9_part2/listbooks.html', {'books': books})


def addbook_p2(request):
    if request.method == 'POST':
        form = BooklabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2_listbooks')
    else:
        form = BooklabForm()

    return render(request, 'bookmodule/lab9_part2/addbook.html', {'form': form})



def editbook_p2(request, id):
    book = get_object_or_404(Booklab, id=id)

    if request.method == 'POST':
        form = BooklabForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9_part2_listbooks')
    else:
        form = BooklabForm(instance=book)

    return render(request, 'bookmodule/lab9_part2/editbook.html', {'form': form, 'book': book})


def deletebook_p2(request, id):
    book = get_object_or_404(Booklab, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('lab9_part2_listbooks')

    return render(request, 'bookmodule/lab9_part2/deletebook.html', {'book': book})
