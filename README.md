Install Django: 
    pip install django

Change dir and target dir hms:
    cd Hospital-Management-System\hms

Run Server:
    Project\Hospital-Management-System> py manage.py runserver

Browse:
    http://localhost:8000/hospital/home

If geting ERRORS:
hospital.Post.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
Solve: python -m pip install Pillow

