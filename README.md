

# MENTORSHIP PROGRAM Project

This project demonstrates a simple relationship between books mentors and students using SQLAlchemy and SQLite.

## Project Structure

- `models.py`: Contains the SQLAlchemy ORM models for `Book`,`Mentor` and `students`.
- `main.py`: Contains the main application logic and CLI commands.
- `school.db`: SQLite database storing book and mentor data.

## Setup

### Prerequisites

- Python 3.8 or newer
- SQLAlchemy

### Installation

1. Clone the repository:

```bash
git clone <git@github.com:Imbuki/p3_project.git >
```

2. Navigate to the project directory:

```bash
cd path/to/project
```

3. Create a virtual environment:

```bash
python3 -m venv myenv
```

4. Activate the virtual environment:

- On macOS and Linux:

```bash
source myenv/bin/activate
```

- On Windows:

```bash
.\myenv\Scripts\Activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

### Database Initialization

Before running the application for the first time, ensure you create and initialize your SQLite database:

```bash
python main.py init_db
```

## Usage

To list all books:

```bash
python main.py list-books
```
To list all students:

```bash
python main.py list-students
```
To list all mentors

```bash
python main.py list-mentors
```
to assign mentors to students
```bash
python main.py assign-student
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT]

---

