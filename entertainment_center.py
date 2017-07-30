# Import movie website program #
import fresh_tomatoes

# Import Movie Class #
from media import Movie


# Create Movie Objects #
matrix = Movie("The Matrix",
               "A computer hacker learns from mysterious rebels about the"
               "true nature of his reality and his role in the war"
               "against its controllers.",
               "https://upload.wikimedia.org/wikipedia/en/c/c1/"
               "The_Matrix_Poster.jpg",
               "https://youtu.be/Q8g9zL-JL8E")

pulp_fiction = Movie("Pulp Fiction",
                     "The lives of two mob hit men, a boxer, a gangster's"
                     " wife, and a pair of diner bandits intertwine in four"
                     "tales of violence and redemption.",
                     "https://upload.wikimedia.org/wikipedia/en/3/3b/"
                     "Pulp_Fiction_%281994%29_poster.jpg",
                     "https://youtu.be/s7EdQ4FqbhY")

fight_club = Movie("Fight Club",
                   "An insomniac office worker, looking for a way to change"
                   "his life, crosses paths with a devil-may-care soap maker,"
                   "forming an underground fight club that evolves into"
                   "something much, much more.",
                   "https://upload.wikimedia.org/wikipedia/en/f/fc/"
                   "Fight_Club_poster.jpg",
                   "https://youtu.be/SUXWAEX2jlg")

inception = Movie("Inception",
                  "A thief, who steals corporate secrets through"
                  "use of dream-sharing technology,is given the inverse task"
                  "of planting an idea into the mind of a CEO.",
                  "https://upload.wikimedia.org/wikipedia/en/2/2e/"
                  "Inception_%282010%29_theatrical_poster.jpg",
                  "https://youtu.be/YoHD9XEInc0")

dark_knight = Movie("The Dark Knight",
                    "When the menace known as the Joker emerges from his ,"
                    "mysterious past he wreaks havoc and chaos on"
                    " the people of Gotham, the Dark Knight must accept"
                    "one of the greatest psychological and physical"
                    "tests of his ability to fight injustice.",
                    "https://upload.wikimedia.org/wikipedia/en/8/8a/"
                    "Dark_Knight.jpg",
                    "https://youtu.be/EXeTwQWrcwY")

interstellar = Movie("Interstellar",
                     "A team of explorers travel through a wormhole in"
                     "space in an attempt to ensure humanity's survival.",
                     "https://upload.wikimedia.org/wikipedia/en/b/bc/"
                     "Interstellar_film_poster.jpg",
                     "https://youtu.be/Lm8p5rlrSkY")


# Create Movie array for open_movies_page f(x) #
movies = [matrix, pulp_fiction, fight_club, inception, 
          dark_knight, interstellar]
# Call open_movies_page f(x) and pass movies array #
fresh_tomatoes.open_movies_page(movies)
