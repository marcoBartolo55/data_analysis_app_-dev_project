import scrapy
import json
import os

class TmdbSpider(scrapy.Spider):
    name = "tmdb"
    allowed_domains = ["api.themoviedb.org"]

    language = "es-MX"
    start_page = 1
    max_pages = 10

    def start_requests(self):
        self.api_key = os.getenv("TMDB_API_KEY")
        if not self.api_key:
            raise RuntimeError("TMDB_API_KEY no está definida")

        url = (
            f"https://api.themoviedb.org/3/movie/popular"
            f"?api_key={self.api_key}&language={self.language}&page={self.start_page}"
        )
        yield scrapy.Request(url, callback=self.parse_popular)

    def parse_popular(self, response):
        data = json.loads(response.text)

        for movie in data["results"]:
            movie_id = movie["id"]

            details_url = (
                f"https://api.themoviedb.org/3/movie/{movie_id}"
                f"?api_key={self.api_key}&language={self.language}"
            )

            yield scrapy.Request(
                details_url,
                callback=self.parse_details,
                meta={"basic": movie}
            )

        current_page = data["page"]
        total_pages = data["total_pages"]

        if current_page < total_pages and current_page < self.max_pages:
            next_page = current_page + 1
            next_url = (
                f"https://api.themoviedb.org/3/movie/popular"
                f"?api_key={self.api_key}&language={self.language}&page={next_page}"
            )
            yield scrapy.Request(next_url, callback=self.parse_popular)

    def parse_details(self, response):
        movie = json.loads(response.text)
        movie_id = movie["id"]

        credits_url = (
            f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
            f"?api_key={self.api_key}&language={self.language}"
        )

        yield scrapy.Request(
            credits_url,
            callback=self.parse_credits,
            meta={"movie": movie}
        )

    def parse_credits(self, response):
        data = json.loads(response.text)
        movie = response.meta["movie"]

        director = None
        for person in data["crew"]:
            if person["job"] == "Director":
                director = person["name"]
                break
            
        yield {
            "id": movie["id"],
            "title": movie["title"],
            "rating": movie["vote_average"],
            "release_date": movie["release_date"],
            "runtime": movie["runtime"],
            "genres": [g["name"] for g in movie["genres"]],
            "votes": movie["vote_count"],
            "budget": movie["budget"],
            "revenue": movie["revenue"],
            "language": movie["original_language"]
        }


        


    
