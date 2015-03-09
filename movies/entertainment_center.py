import fresh_tomatoes
import media

# Instances of class Movie
the_legend_of_1900 = media.Movie("The Legend of 1900", "1998", "R", "165 min",
                                 "Some dude lives his whole life on a ship",
                                 "http://upload.wikimedia.org/wikipedia/en/5/50/Leggenda_pianista.jpg",
                                 "http://youtu.be/LA8v9MamhJE")

avatar = media.Movie("Avatar", "2009", "PG-13", "162 min",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://youtu.be/5PSNL1qE6VY")

a_beautiful_mind = media.Movie("A Beautiful Mind", "2001", "PG-13", "135 min",
                               "A genius struggles with schizophrenia",
                               "http://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                               "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

star_trek_4 = media.Movie("Star Trek IV", "1986", "PG", "119 min",
                          "Kirk and pals go back in time to save Earth",
                          "http://upload.wikimedia.org/wikipedia/en/6/68/Star_Trek_IV_The_Voyage_Home.png",
                          "http://youtu.be/VW7neKZFKE0")

enemy_at_the_gates = media.Movie("Enemy At The Gates", "2001", "R", "131 min",
                                 "A shepherd from the Ural Mountains finds himself on the front lines of the Battle of Stalingrad.",
                                 "http://upload.wikimedia.org/wikipedia/en/a/ab/Enemy_at_the_gates_ver2.jpg",
                                 "http://youtu.be/4O-sMh_DO6I")

the_fifth_element = media.Movie("The Fifth Element", "1997", "PG-13", "126 min",
                                "Bruce Willis save the world. Again.",
                                "http://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
                                "http://youtu.be/VkX7dHjL-aY")

# Group all movie instances together in a list
movies = [the_legend_of_1900, avatar,a_beautiful_mind, star_trek_4, enemy_at_the_gates, the_fifth_element]

fresh_tomatoes.open_movies_page(movies)

