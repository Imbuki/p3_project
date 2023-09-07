from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from models import Base
import datetime

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    author = Column(String, nullable=False)
    borrowed_date = Column(Date, nullable=True)
    return_date = Column(Date, nullable=True)
    status = Column(String, default="not borrowed")

    student = relationship('Student', back_populates='book', uselist=False)
    mentor = relationship('Mentor', back_populates='book', uselist=False)

    def __repr__(self):
        return f"<Book(id={self.id}, name={self.name}, type={self.type}, author={self.author}, borrowed_date={self.borrowed_date}, return_date={self.return_date})>"
