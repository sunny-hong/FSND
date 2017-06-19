import media
import fresh_tomatoes


# 6 movie_name instances
# 4 Instance Variables: media.Movie("title", "desc", "poster", "trailer")
toy_story = media.Movie("Toy Story 3",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/2010/posters/toy_story_three_ver10.jpg",  # NOQA
                        "https://youtu.be/JcpWXaA2qeg?t=7s")

the_internship = media.Movie("The Internship",
                            "Two middle-aged men applies for internships",
                            "http://www.impawards.com/2013/posters/internship_ver8.jpg",  # NOQA
                            "https://youtu.be/cdnoqCViqUo?t=7s")

up = media.Movie("Up", "A man fulfills his dream to fly",
                "http://funfilledflicks.com/wp-content/uploads/2013/05/Up-Official-Movie-Poster.jpg",  # NOQA
                "https://youtu.be/qas5lWp7_R0?t=7s")

bad_moms = media.Movie("Bad Moms",
                        "Three mothers ditch their conventional"
                        " responsibilities",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIwNzE5MTgwNl5BMl5BanBnXkFtZTgwNjM4OTA0OTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=IHBLbGvwO6I")

midnight = media.Movie("Midnight in Paris",
                        "A writer visits Gilded Age in Paris",
                        "http://sonyclassics.com/midnightinparissag/_images/gfx-midnight_cover.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=FAfR8omt-CY"
                        )
darkknight = media.Movie("Dark Knight",
                        "Batman fights for injustice in Gotham through"
                        " psychological and physical tests.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=wzMW991EHGg")

# Array of movie instances
movies = [toy_story, the_internship, up, bad_moms, midnight, darkknight]
# Calls fresh_tomatoes.py file's "open_movies_page" function.
fresh_tomatoes.open_movies_page(movies)
