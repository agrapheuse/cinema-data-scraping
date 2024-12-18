create_table_query = """
CREATE TABLE IF NOT EXISTS movies (
  uuid CHAR(36) NOT NULL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  director VARCHAR(255) NOT NULL,
  category VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  cinema VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  date_time DATETIME NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  info_link VARCHAR(255) NOT NULL,
  ticket_link VARCHAR(255) NOT NULL
)
"""

delete_table_query = """
DROP TABLE IF EXISTS movies
"""

empty_table_query = """
TRUNCATE TABLE movies;
"""

alter_table_query = """
ALTER TABLE movies MODIFY description TEXT NOT NULL
"""

insert_query = """
INSERT INTO movies (uuid, title, director, category, description, cinemaId, date_time, image_url, info_link, ticket_link)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

