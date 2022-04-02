CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created timestamp with time zone
);

SET search_path TO content,public; 

CREATE EXTENSION "uuid-ossp";

INSERT INTO content.film_work (id, title, type, creation_date, rating) SELECT content.uuid_generate_v4(), 'some name', case when RANDOM() < 0.3 THEN 'movie' ELSE 'tv_show' END ,
 date::DATE, floor(random() * 100)
FROM generate_series(
  '1900-01-01'::DATE,
  '2021-01-01'::DATE,
  '1 hour'::interval
) date; 

CREATE INDEX film_work_creation_date_idx ON content.film_work(creation_date); 

CREATE UNIQUE INDEX some_name_idx ON some_table (some_unique_field) 

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role TEXT NOT NULL,
    created timestamp with time zone
); 

CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id); 

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY key,
    name TEXT NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY key,
    film_work_id uuid NOT NULL,
    genre_id uuid NOT NULL,
    created timestamp with time zone
);

CREATE UNIQUE INDEX film_work_genre_idx ON content.genre_film_work (film_work_id, genre_id);
