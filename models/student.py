from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String, nullable=False)
    l_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    class_ = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    
    mentor_id = Column(Integer, ForeignKey('mentors.id'))
    mentor = relationship('Mentor', back_populates='students')
    
    book = relationship('Book', back_populates='student')

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.f_name} {self.l_name} {self.surname}, class_={self.class_}, book_id={self.book_id}, mentor_id={self.mentor_id})>"
