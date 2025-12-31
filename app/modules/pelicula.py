class peli:
    def __init__(
        self,
        id,
        title,
        rating,
        release_date,
        runtime,
        genres,
        votes,
        budget,
        revenue,
        language,
        directors=None,
        writers=None,
    ):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_date = release_date
        self.runtime = runtime
        self.genres = genres
        self.votes = votes
        self.budget = budget
        self.revenue = revenue
        self.language = language
        self.directors = directors or []
        self.writers = writers or []

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "rating": self.rating,
            "release_date": self.release_date,
            "runtime": self.runtime,
            "genres": self.genres,
            "votes": self.votes,
            "budget": self.budget,
            "revenue": self.revenue,
            "language": self.language,
            "directors": [d.to_dict() for d in self.directors],
            "writers": [w.to_dict() for w in self.writers],
        }
