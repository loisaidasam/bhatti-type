bhatti-type
===========

Library for converting regular text into Bhatti Type!

Simple example:
---------------

    $ python bhattitype.py "my name is bhatti and i know what i'm doing"
    
    q: my name is bhatti and i know what i'm doing
    result: my nmae is bhatti adn i nkow whta i'm doign

To run webserver (complete with API):
-------------------------------------

    $ pip install -r requirements.txt
    $ foreman start web

or:

    $ python webserver.py test

API usage:
----------

`/api/?q=<foo>`

[GET or POST]

params:

    q <str> input text

sample response:

    {
        q: "my name is bhatti and i know what i'm doing",
        result: "my nmae is bhatti adn i kwno whta i'm doign",
        status: "OK"
    }

Resources:
----------

- [http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings](http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings)
- [http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines](http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines)

Other ideas:
------------

- [http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/Grammar_and_Misc](http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/Grammar_and_Misc)
- [http://grammar.yourdictionary.com/spelling-and-word-lists/misspelled.html](http://grammar.yourdictionary.com/spelling-and-word-lists/misspelled.html)
- [http://grammar.yourdictionary.com/spelling-and-word-lists/150more.html](http://grammar.yourdictionary.com/spelling-and-word-lists/150more.html)
- [http://nltk.org/book/ch01.html](http://nltk.org/book/ch01.html)
