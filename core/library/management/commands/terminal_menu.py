from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from library.models import Book, Loan
from datetime import date

class Command(BaseCommand):
    help = 'Library Management Menu'

    def handle(self, *args, **kwargs):
        user = None

        while True:
                # Login Screen
                username = input('Type your username: ')
                password = input('Type your password: ')

                # Verifies Login
                try:
                    user = User.objects.get(username=username)

                    if user.check_password(password):
                        print(f'Welcome, {user.username}!')
                        break
                    else:
                        print('Wrong password...')
                        desist_pass = input('Do you want to try again? [y/n]: ').lower()
                        if desist_pass == 'n':
                            print('Exiting...')
                            break

                except User.DoesNotExist:
                    print('User not found.')
                    desist_user = input('Do you want to try again? [y/n]: ').lower()
                    if desist_user == 'n':
                        print('Exiting...')
                        break
                            
        while True:
            # After Login Menu
            print('1. List Available Books')
            print('2. Borrow Book')
            print('3. Return Book')
            print('4. Exit')

            choice = input('Select an option: ')

            if choice == '1':
                # List Available Books
                books = Book.objects.all()
                print('Available Books')
                for book in books:
                    print(f'- {book.title}')

            elif choice == '2':
                # Borrow Book
                books = Book.objects.all()
                print('Select the number book you wanna borrow, please.')
                for idx, book in enumerate(books, 1):
                    print(f'{idx}. {book.title}')

                try:
                    book_number = int(input('Type the number of the book: '))
                    if book_number < 1 or book_number > len(books):
                        print('Invalid Number')
                        continue

                    book = books[book_number -1]

                    if Loan.objects.filter(book=book, return_date=None).exists():
                        print(f'The book "{book.title}" is alread borrowed!')
                    else:
                        loan = Loan(book=book, user=user, loan_date=date.today())
                        loan.save()
                except ValueError:
                    print('Please, enter a valide number.')
            
            elif choice == '3':
                # Return Book
                book_title = input('Type the book title to return: ')
                try:
                    loan = Loan.objects.filter(book__title=book_title, user=user, return_date=None).first()
                    if loan:
                        loan.return_date = date.today()
                        loan.save()
                        print(f'The book "{book_title}" was succesfully returned.')
                    else:
                        print(f'You do not have the book "{book_title}" borrowed.')
                except Loan.DoesNotExist:
                    print(f'Loan does not found for the book "{book_title}"')
            elif choice == '4':
                print('Exiting...')
                break
            
            else:
                print('Invalid option.')
