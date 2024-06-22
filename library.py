from document import Document
from event import Event
from itinerary import Itinerary

class Library():
    def __init__(self, name: str) -> None:
        self.name = name
        self.admins = self.get_admins()
        self.librarians = self.get_librarians()
        self.documents = self.get_documents()
    def get_admins(self) -> list:
        '''Retorna todos os admins da biblioteca.'''
        pass
    def get_librarians(self) -> list:
        '''Retorna todos os bibliotecários.'''
        pass
    def get_documents(self) -> list:
        '''Retorna todos os documentos registrados.'''
        pass
    def lend_document(self, document: Document, event: Event) -> None:
        '''Empresta um determinado documento para um determinado evento.'''
        pass
    def schedule_tour(self, itinerary: Itinerary) -> None:
        '''Agenda uma visita guiada, com um roteiro em específico.'''
