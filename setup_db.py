from project import db, models
import random
import string

def random_string(n):
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(n)
    )


def random_row(id):
    row = models.CbomRow(
        cbom_id=id,
        man_part_num=random_string(25),
        int_part_num=random_string(25),
        unit_price=random.randrange(1, 14),
        quantity=random.randint(1, 20)
    )
    return row

def init_db():
    # create boms
    for n in range(100):
        print('creating number ' + str(n))
        c = models.Cbom(name='come_on_' + str(n) + '_file.xls')
        db.session.add(c)
        db.session.commit()
        for _ in range(1, random.randint(1, 10)):
            row = random_row(c.id)
            db.session.add(row)

init_db()