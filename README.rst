social-regexes
==============
Given input, returns identified social network with corresponding user id

-------------
Installation:
pip install socialregexes

------
Usage:
    $ python socialregexes/socialregexes.py https://twitter.com/guillem_lefait not_an_url guillem.lefait@removemegmail.com https://github.com/glefait
    ('twitter', 'guillem_lefait')
    None
    ('email', 'guillem.lefait@removemegmail.com')
    ('github', 'glefait')
