create_table_query = """
CREATE TABLE IF NOT EXISTS RawMovieData (
  uuid CHAR(36) NOT NULL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  director VARCHAR(255) NOT NULL,
  category VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  cinema_id CHAR(36) NOT NULL,
  date_time DATETIME NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  info_link VARCHAR(255) NOT NULL,
  ticket_link VARCHAR(255) NOT NULL
)
"""

delete_table_query = """
DROP TABLE IF EXISTS RawMovieData
"""

empty_table_query = """
TRUNCATE TABLE RawMovieData;
"""

alter_table_query = """
ALTER TABLE RawMovieData MODIFY description TEXT NOT NULL
"""

insert_query = """
INSERT INTO RawMovieData (uuid, title, director, category, description, cinema_id, date_time, image_url, info_link, ticket_link)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

