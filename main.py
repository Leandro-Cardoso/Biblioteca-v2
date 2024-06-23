from os import system

from library import Library
from file import File
from user import User, Author, Librarian, Admin
from document import Document

def main() -> None:
    library = Library('biblioteca')
    admins_file = File('admins', 'users')
    system('cls')

main()
