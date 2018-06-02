import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/az/thumb/1/15/Avatar_poster.jpg/280px-Avatar_poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print(avatar.storyline)
#avatar.show_trailer()
true_stories = media.Movie("True Stories",
                           "A small but growing Texas town, filled with strange and musical characters, celebrates its sesquicentennial and converge on a local parade and talent show",
                           "https://ia.media-imdb.com/images/M/MV5BYWU0Njc3YTYtNDEyYi00ZWNhLTk5YWQtYzhhNTM5OTYzOTVhXkEyXkFqcGdeQXVyNzc5MjA3OA@@._V1_SY1000_CR0,0,657,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=mhRgCsQf3CU",)
#true_stories.show_trailer()
#print(true_stories.storyline)
twelve_monkeys = media.Movie("Twelve Monkeys",
                             "a convict is sent back in time to gather information about the man-made virus",
                             "https://ia.media-imdb.com/images/M/MV5BN2Y2OWU4MWMtNmIyMy00YzMyLWI0Y2ItMTcyZDc3MTdmZDU4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=6q-qEW6CNPE")
forbidden_planet = media.Movie("Forbidden Planet",
                               "An invisible force begins murdering human colonists on a distant planet",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BOTdmODZkNmQtYjU4Mi00MTcyLTg5YmEtNmVjMWU1M2Y5NzgyXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY1200_CR74,0,630,1200_AL_.jpg",
                               "https://www.youtube.com/watch?v=F17CCRoMttQ")
the_godfather = media.Movie("The Godfather",
                            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son",
                            "https://ia.media-imdb.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,700,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")
jackie_brown = media.Movie("Jackie Brown",
                           "A middle-aged woman finds herself in the middle of a huge conflict that will either make her a profit or cost her life",
                           "https://ia.media-imdb.com/images/M/MV5BNmY5ODRmYTItNWU0Ni00MWE3LTgyYzUtYjZlN2Q5YTcyM2NmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,683,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=J9Bd4ShuEAw")

movies = [toy_story, avatar, true_stories, twelve_monkeys, forbidden_planet, the_godfather, jackie_brown]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
