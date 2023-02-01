from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'homepage.html')

def book (request):
    return render(request, 'bookspage.html')

def detail (request,id):
      
    books = {
        '1': 'Title: The Great Gatsby Detail: The Great Gatsby by F. Scott Fitzgerald: Set in the 1920s, this novel explores the decadence of the Jazz Age and the disillusionment of those who sought to attain the American Dream.',
        '2': 'Title: To Kill a Mockingbird  Detail: To Kill a Mockingbird by Harper Lee, A coming-of-age story set in the 1930s, this novel explores themes of racial injustice and the loss of innocence through the eyes of Scout Finch.',
        '3': 'Title: 1984 Detail: 1984 by George Orwell: A dystopian novel set in a totalitarian society, this book is a warning against government control and manipulation of information. ',
        '4': 'Title: Pride and Prejudice Detail: Pride and Prejudice by Jane Austen: A classic love story that explores societal norms and the biases that exist between classes in Regency England.',
        '5': 'Title: The Catcher in the rye Detail: "The Catcher in the Rye" is a novel written by J.D. Salinger and was first published in 1951. The story is narrated by Holden Caulfield, a teenage boy who has been expelled from prep school. The book is about Holden s experiences and struggles with depression, alienation, and growing up.'
    }
    
    book = books.get(id)

    return render(request,'detail.html',{'book':book})
   