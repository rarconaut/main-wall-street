from main-wall-street.app import db

def create_tables():
    # db.drop_all()
    db.create_all()
