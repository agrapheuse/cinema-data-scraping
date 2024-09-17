class Movie:
    def __init__(self, date_time, cinema, country, city, image_url, name, info_link, director, category, ticket_link, description):
        self.date_time = date_time
        self.cinema = cinema
        self.country = country
        self.city = city
        self.image_url = image_url
        self.name = name
        self.info_link = info_link
        self.director = director
        self.category = category
        self.ticket_link = ticket_link
        self.description = description

    def to_dict(self):
        return {
            'date_time': self.date_time,
            'cinema': self.cinema,
            'country': self.country,
            'city': self.city,
            'image_url': self.image_url,
            'name': self.name,
            'info_link': self.info_link,
            'director': self.director,
            'category': self.category,
            'ticket_link': self.ticket_link,
            'description': self.description
        }
