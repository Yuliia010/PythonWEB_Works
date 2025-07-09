from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
writers_info = {
    'Hemingway': {
        'name': 'Ernest Hemingway',
        'bio': 'Some info about Hemingway...',
        'books': {
            'The_Old_Man_and_the_Sea': {
                'title': 'The Old Man and the Sea',
                'description': 'A story about an old fisherman...',
            },
            'The_Sun_Also_Rises': {
                'title': 'The Sun Also Rises',
                'description': 'A novel about post-war generation...',
            },
        }
    },
    'Shakespeare': {
        'name': 'William Shakespeare',
        'bio': 'Some info about Shakespeare...',
        'books': {
        }
    },
}

top_books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'description': 'A novel about...'},
    {'title': '1984', 'author': 'George Orwell', 'description': 'An anti-utopia...'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'description': 'A story about...'},
]

def home(request):
    return render(request, 'Task1/home.html')

def writers(request):
    writer = request.GET.get('writers')
    year = request.GET.get('year')
    if writer and year:
        return render(request, 'Task1/books_by_year_stub.html', {
            'writer_name': writer,
            'year': year,
        })
    else:
        writers_list = [{'slug': key, 'name': val['name']} for key, val in writers_info.items()]
        return render(request, 'Task1/writers.html', {'writers': writers_list})

def books(request):
    books_list = [{'rank': i + 1, 'title': book['title']} for i, book in enumerate(top_books)]
    return render(request, 'Task1/books.html', {'books': books_list})

def book_detail(request, book_rank):
    index = book_rank - 1
    if 0 <= index < len(top_books):
        book = top_books[index]
        return render(request, 'Task1/book_detail.html', {'book': book, 'rank': book_rank})
    else:
        return redirect('books')
    
def writer_detail(request, writer_name):
    writer = writers_info.get(writer_name)
    if not writer:
        return redirect('writers')

    books = []
    for slug, info in writer.get('books', {}).items():
        books.append({
            'slug': slug,
            'title': info['title'],
        })

    return render(request, 'Task1/writer_detail.html', {
        'writer_name': writer_name,
        'writer': writer,
        'books': books,
    })

def writer_book_detail(request, writer_name, book_slug):
    writer = writers_info.get(writer_name)
    if not writer:
        return redirect('writers')

    book = writer['books'].get(book_slug)
    if not book:
        return redirect('writer_detail', writer_name=writer_name)

    return render(request, 'Task1/book_detail.html', {
        'writer': writer,
        'writer_name': writer_name,
        'book': book,
    })
