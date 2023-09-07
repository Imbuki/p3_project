from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base


class Mentor(Base):
    __tablename__ = 'mentors'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))
    
    students = relationship('Student', back_populates='mentor')
    book = relationship('Book', back_populates='mentor')

    def __repr__(self):
        return f"<Mentor(id={self.id}, name={self.f_name} {self.surname}, book_id={self.book_id})>"
