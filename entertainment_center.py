import media
import fresh_tomatoes

"""
My movies instances formatted in the order of:
title
extra movie information
poster
trailer
"""

big_lebowski = media.Movie("The Big Lebowski",
							"http://www.imdb.com/title/tt0118715/?ref_=nv_sr_1",
							"https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
							"https://www.youtube.com/watch?v=cd-go0oBF4Y")

tron_legacy = media.Movie("Tron: Legacy",
							"http://www.imdb.com/title/tt1104001/?ref_=nv_sr_1",
							"https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
							"https://www.youtube.com/watch?v=L9szn1QQfas")

the_fountain = media.Movie("The Fountain",
							"http://www.imdb.com/title/tt0414993/?ref_=nv_sr_1",
							"https://upload.wikimedia.org/wikipedia/en/e/ee/Fountain_poster_1.jpg",
							"https://www.youtube.com/watch?v=dAuxryJ6pv8")

dark_knight = media.Movie("The Dark Knight",
							"http://www.imdb.com/title/tt0468569/?ref_=nv_sr_1",
							"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
							"https://www.youtube.com/watch?v=EXeTwQWrcwY")

dude_wheres_my_car = media.Movie("Dude Where's My Car",
							"http://www.imdb.com/title/tt0242423/?ref_=nv_sr_3",
							"https://upload.wikimedia.org/wikipedia/en/d/df/Dude_Wheres_My_Car_movie.jpg",
							"https://www.youtube.com/watch?v=d1wuijgeaaY")

the_raid = media.Movie("The Raid 2",
							"http://www.imdb.com/title/tt2265171/?ref_=nv_sr_1",
							"https://upload.wikimedia.org/wikipedia/en/c/c3/The_Raid_2_Berandal_teaser_banner.jpeg",
							"https://www.youtube.com/watch?v=MG9uFX3uYq4")



movies = [big_lebowski, tron_legacy, the_fountain, dark_knight, dude_wheres_my_car, the_raid]
fresh_tomatoes.open_movies_page(movies)

