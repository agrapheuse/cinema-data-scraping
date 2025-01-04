class Movie:
    def __init__(self, uuid, image_url, title, director, category, description):
        self.uuid = uuid
        self.image_url = image_url
        self.title = title
        self.director = director
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            'image_url': self.image_url,
            'title': self.title,
            'director': self.director,
            'category': self.category,
            'description': self.description
        }
