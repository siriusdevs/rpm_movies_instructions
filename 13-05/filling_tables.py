import random
import uuid
import psycopg2

from datetime import datetime
from psycopg2.extras import execute_batch

dsn = {
    'dbname': 'postgres',
    'user': 'app',
    'password': '123qwe',
    'host': 'localhost',
    'port': 5432,
    'options': '-c search_path=content',
}

now = datetime.utcnow()

with psycopg2.connect(**dsn) as conn, conn.cursor() as cur:

    #Заполнение таблицы Person
    snatch = []
    breaking_bad = []
    sm_barrels = []

    ritchie_id = str(uuid.uuid4())
    vaughn_id = str(uuid.uuid4())
    jones_id = str(uuid.uuid4())
    statham_id = str(uuid.uuid4())

    snatch.append((ritchie_id, 'Guy Ritchie', 'director'))
    snatch.append((vaughn_id, 'Matthew Vaughn', 'producer'))
    snatch.append((str(uuid.uuid4()), 'Benicio del Toro', 'actor'))
    snatch.append((str(uuid.uuid4()), 'Dennis Farina', 'actor'))
    snatch.append((jones_id, 'Vinnie Jones', 'actor'))
    snatch.append((str(uuid.uuid4()), 'Brad Pitt', 'actor'))
    snatch.append((str(uuid.uuid4()), 'Rade Šerbedžija', 'actor'))
    snatch.append((statham_id, 'Jason Statham', 'actor'))

    breaking_bad.append((str(uuid.uuid4()), 'Vince Gilligan', 'director'))
    breaking_bad.append((str(uuid.uuid4()), 'Bryan Cranston', 'actor'))
    breaking_bad.append((str(uuid.uuid4()), 'Aaron Paul', 'actor'))
    breaking_bad.append((str(uuid.uuid4()), 'Dean Norris', 'actor'))
    breaking_bad.append((str(uuid.uuid4()), 'Bob Odenkirk', 'actor'))

    sm_barrels.append((ritchie_id, 'Guy Ritchie', 'director'))
    sm_barrels.append((vaughn_id, 'Matthew Vaughn', 'producer'))
    sm_barrels.append((jones_id, 'Vinnie Jones', 'actor'))
    sm_barrels.append((statham_id, 'Jason Statham', 'actor'))
    sm_barrels.append((str(uuid.uuid4()), 'Jason Flemyng', 'actor'))
    sm_barrels.append((str(uuid.uuid4()), 'Dexter Fletcher', 'actor'))
    sm_barrels.append((str(uuid.uuid4()), 'Nick Moran', 'actor'))

    query = 'INSERT INTO person (id, full_name, created, modified) VALUES (%s, %s, %s, %s)'
    data = [(pk, name, now, now) for pk, name, _ in snatch]
    execute_batch(cur, query, data)
    data = [(pk, name, now, now) for pk, name, _ in breaking_bad]
    execute_batch(cur, query, data)   
    data = [(pk, name, now, now) for pk, name, _ in sm_barrels[4:]]
    execute_batch(cur, query, data)

    conn.commit()

    #Заполнение таблицы PersonFilmWork
    person_film_work_data = []

    cur.execute('SELECT id, title FROM film_work')
    film_work_dict = {}
    for data in cur.fetchall():
        film_work_dict[data[1]] = data[0]

    for person_id, _, role in snatch:
        person_film_work_data.append((str(uuid.uuid4()), film_work_dict['Snatch'], person_id, role, now))
    for person_id, _, role in breaking_bad:
        person_film_work_data.append((str(uuid.uuid4()), film_work_dict['Breaking bad'], 
            person_id, role, now))
    for person_id, _, role in sm_barrels:
        person_film_work_data.append((str(uuid.uuid4()), film_work_dict['Lock, Stock and Two Smoking Barrels'],
            person_id, role, now))
    
    query = 'INSERT INTO person_film_work (id, film_work_id, person_id, role, created) VALUES (%s, %s, %s, %s, %s)'
    execute_batch(cur, query, person_film_work_data)
    conn.commit()

