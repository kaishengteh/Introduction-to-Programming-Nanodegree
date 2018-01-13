import fresh_tomatoes
import media

despicable_me_3 = media.Movie ('Despicable Me 3', 
                               'This threequel is an amusing, kid-friendly mix of sibling interaction and irresistibly silly minion jokes.',
                               'https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg',
                               'https://www.youtube.com/watch?v=6DBi41reeF0',
                               '2017')

ratatouille = media.Movie('Ratatouille', 
                        'Remy dreams of becoming a great French chef, but his family reminds him of one major hurdle: He is a rat.',
                        'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg', 
                        'https://www.youtube.com/watch?v=c3sBBRxDAqk',
                        '2007')

bean = media.Movie('Bean',
                     'The plot is an excuse for what is really a series of slapstick sketches involving very little dialogue but many funny faces and physical contortions, and a lot of potty humor and general grossness.',
                     'https://upload.wikimedia.org/wikipedia/en/3/37/Bean_movie_poster.jpg',
                     'https://www.youtube.com/watch?v=0ea8BerkI0w',
                     '1997')

furious_7 = media.Movie ('Furious 7',
                         'Furious 7 is another solid Fast and the Furious installment - one that (flaws aside) provides a nice farewell to star Paul Walker.',
                         'https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg',
                         'https://www.youtube.com/watch?v=Skpu5HaVkOc',
                         '2015')

skyfall = media.Movie ('Skyfall', 
                       'Scene to scene, moment to moment, the movie offers one of the richest and most interesting Bond adventures.',
                       'https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg',
                       'https://www.youtube.com/watch?v=6kw1UVovByw',
                       '2012')

finding_nemo = media.Movie ('Finding Nemo', 
                            'Finding Nemo is another example of post-conversion done right and, paired with the especially humorous Partysaurus Rex short.',
                            'https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg',
                            'https://www.youtube.com/watch?v=SPHfeNgogVs',
                            '2003')

# Open the 6 movie trailers and create html file
movies = [despicable_me_3, ratatouille, bean, furious_7, skyfall, finding_nemo]
fresh_tomatoes.open_movies_page(movies)
