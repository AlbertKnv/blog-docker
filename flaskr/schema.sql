DROP TABLE IF EXISTS auth_user CASCADE;
DROP TABLE IF EXISTS blog_post CASCADE;

CREATE TABLE auth_user (
    id SERIAL PRIMARY KEY,
    username varchar(100) UNIQUE NOT NULL,
    password varchar(300) NOT NULL
);

CREATE TABLE blog_post (
    id SERIAL PRIMARY KEY,
    author_id integer NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title varchar(300) NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES auth_user (id)
);