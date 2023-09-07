import click
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from models.student import Student
from models.mentor import Mentor
from models.book import Book
from models import Base
from datetime import datetime, timedelta

cli = click.Group()


DATABASE_URL = "sqlite:///school_management.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('f_name')
@click.argument('l_name')
@click.argument('surname')
@click.argument('class_')
@click.argument('book_id')
def add_student(f_name, l_name, surname, class_, book_id):
    new_student = Student(
        f_name=f_name,
        l_name=l_name,
        surname=surname,
        class_=class_,
        book_id=book_id
    )
    session.add(new_student)
    session.commit()
    click.echo(f"Added student: {f_name} {l_name} {surname}")

@cli.command()
@click.argument('student_id')
def remove_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        click.echo(f"Removed student with ID: {student_id}")
    else:
        click.echo("Student not found.")

@cli.command('list-students')
def list_students():
    """List all students along with their mentor."""
    with Session() as session:
        # Fetch students along with their associated mentor using a JOIN
        results = session.query(Student, Mentor).outerjoin(Mentor, Student.mentor_id == Mentor.id).all()

        for student, mentor in results:
            mentor_name = "Unassigned" if mentor is None else f"{mentor.f_name} {mentor.surname}"
            click.echo(f"ID: {student.id}, Name: {student.f_name} {student.l_name} {student.surname}, Class: {student.class_}, Book ID: {student.book_id}, Mentor: {mentor_name}")


@cli.command()
@click.argument('student_id')
@click.argument('new_class')
def update_student_class(student_id, new_class):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.class_ = new_class
        session.commit()
        click.echo(f"Updated student's class to: {new_class}")
    else:
        click.echo("Student not found.")

@cli.command()
@click.argument('f_name')
@click.argument('surname')
def add_mentor(f_name, surname):
    new_mentor = Mentor(
        f_name=f_name,
        surname=surname
    )
    session.add(new_mentor)
    session.commit()
    click.echo(f"Added mentor: {f_name} {surname}")

@cli.command()
def list_mentors():
    mentors = session.query(Mentor).all()
    for mentor in mentors:
        student_names = [f"{student.f_name} {student.surname}" for student in mentor.students] 
        if student_names:
            students_str = ', '.join(student_names)
            click.echo(f"ID: {mentor.id}, Name: {mentor.f_name} {mentor.surname} is mentoring {students_str}")
        else:
            click.echo(f"ID: {mentor.id}, Name: {mentor.f_name} {mentor.surname} is mentoring no one.")

@cli.command()
@click.argument('book_name')
@click.argument('book_type')
@click.argument('author')
def add_book(book_name, book_type, author):
    # Create the book object without borrowed_date and return_date
    new_book = Book(
        name=book_name,
        type=book_type,
        author=author
    )
    
    # Add to session and commit
    session.add(new_book)
    session.commit()

    click.echo(f"Added book: {book_name} by {author}")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('book_id', type=int)
def assign_book_to_student(student_id, book_id):
    student = session.query(Student).filter_by(id=student_id).first()
    book = session.query(Book).filter_by(id=book_id).first()
    
    if student and book:
        # Check if the book is already assigned
        if book.status == "borrowed":
            click.echo("The book is already taken, choose another book.")
            return

        # Set the borrowed_date, calculate the return_date, and update the status
        borrowed_date = datetime.now()
        return_date = borrowed_date + timedelta(weeks=2)

        book.borrowed_date = borrowed_date
        book.return_date = return_date
        book.status = "borrowed"  # Updating the status of the book

        student.book_id = book.id

        session.commit()

        click.echo(f"Assigned book: {book.name} to student: {student.f_name} {student.surname}")
    else:
        click.echo("Invalid student or book ID.")


@cli.command()
def list_books():
    books = session.query(Book).all()
    for book in books:
        click.echo(f"ID: {book.id}, Name: {book.name}, Type: {book.type}, Status: {book.status}")

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    Base.metadata.create_all(engine)
    click.echo('Initialized the database.')

cli.add_command(init_db_command)

@click.command('assign-student')
@click.argument('student_id', type=int)
@click.argument('mentor_id', type=int)
def assign_student_to_mentor(student_id, mentor_id):
    with Session() as session:
        student = session.query(Student).filter_by(id=student_id).first()
        mentor = session.query(Mentor).filter_by(id=mentor_id).first()

        # Check if the student or mentor exists
        if not student:
            click.echo(f"Student with ID {student_id} not found!")
            return
        if not mentor:
            click.echo(f"Mentor with ID {mentor_id} not found!")
            return

        # Check the number of students assigned to the mentor
        students_mentored = session.query(Student).filter_by(mentor_id=mentor.id).all()
        if len(students_mentored) >= 2:
            click.echo(f"Mentor {mentor.f_name} {mentor.surname} already has 2 students assigned!")
            return

        # Assign the student to the mentor
        student.mentor_id = mentor.id
        session.commit()

        click.echo(f"Assigned student: {student.f_name} {student.surname} to mentor: {mentor.f_name} {mentor.surname}")


cli.add_command(assign_student_to_mentor)

'''
@cli.command()
def add_status_column():
    """Temporary command to add status column to books table."""
    from sqlalchemy import text

    with Session() as session:
        session.execute(text('ALTER TABLE books ADD COLUMN status VARCHAR(255) DEFAULT "not borrowed"'))
        session.commit()
    click.echo("Status column added successfully.")
    '''

@cli.command('list-borrowed-books')
def list_borrowed_books():
    """List all borrowed books."""
    borrowed_books = session.query(Book).filter_by(status='borrowed').all()

    if not borrowed_books:
        click.echo("No books have been borrowed.")
        return

    for book in borrowed_books:
        click.echo(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Borrowed Date: {book.borrowed_date}, Return Date: {book.return_date}")

cli.add_command(list_borrowed_books)

@cli.command()
@click.argument('mentor_id', type=int)
@click.argument('book_id', type=int)
def assign_book_to_mentor(mentor_id, book_id):
    """Assign a book to a mentor."""
    with Session() as session:
        mentor = session.query(Mentor).filter_by(id=mentor_id).first()
        book = session.query(Book).filter_by(id=book_id).first()

        # Check if the mentor and book exist
        if not mentor:
            click.echo(f"Mentor with ID {mentor_id} not found!")
            return
        if not book:
            click.echo(f"Book with ID {book_id} not found!")
            return

        # Check if the book is already assigned
        if book.borrowed_date:
            click.echo("The book is already taken, choose another book.")
            return

        # Set the borrowed_date and calculate the return_date
        borrowed_date = datetime.now()
        return_date = borrowed_date + timedelta(weeks=2)

        book.borrowed_date = borrowed_date
        book.return_date = return_date

        mentor.book_id = book.id  # This assumes you have a 'book_id' column in Mentor model

        session.commit()

        click.echo(f"Assigned book: {book.name} to mentor: {mentor.f_name} {mentor.surname}")

 
if __name__ == '__main__':
    cli()
