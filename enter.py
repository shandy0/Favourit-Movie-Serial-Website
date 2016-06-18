import media
import index
Breaking_Bad = media.Movie("Breaking Bad",
                           "Breaking Bad is an American crime drama television series created and produced by Vince Gilligan",
                           "http://unspoiledpodcasts.com/wp-content/uploads/2014/09/Breaking-Bad.jpg",
                           "https://www.youtube.com/watch?v=lrcqbavlbyQ")
Friends = media.Movie("Friends",
                           "Friends is an American television sitcom",
                           "http://www.hercampus.com/sites/default/files/2014/11/09/Friends-season-10-014.jpg",
                           "https://www.youtube.com/watch?v=bvEnlf9g4co")


Game_of_Thrones=media.Movie("Game of Thrones",
                             "Game of Thrones is an American fantasy drama television series created by David Benioff and D. B. Weiss",
                           "http://www.wpaperhd.com/uploads/originals/2016/01/08/game-of-thrones-black-OE2R.jpg",
                           "https://www.youtube.com/watch?v=BpJYNVhGf1s")
                             
movies= [Breaking_Bad,Friends,Game_of_Thrones]
index.open_movies_page(movies)

