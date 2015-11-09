from project import db, models

def init_db():
    db.create_all()
    for n in range(100):
        c = models.Cbom(name='cool_excel_' + str(n) + '_file.xls')
        db.session.add(c)
    db.session.commit()

init_db()