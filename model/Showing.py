class Showing:
    def __init__(self, date_time, cinema, movie, info_link, ticket_link):
        self.date_time = date_time
        self.cinemaId = cinema
        self.movieId = movie
        self.info_link = info_link
        self.ticket_link = ticket_link

    def to_dict(self):
        return {
            'date_time': self.date_time,
            'cinema': self.cinemaId,
            'movie': self.movieId,
            'info_link': self.info_link,
            'ticket_link': self.ticket_link,
        }
