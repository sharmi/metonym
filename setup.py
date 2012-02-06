from distutils.core import setup
setup(name='metonym',
      version='0.2',
      packages=['metonym'],
      scripts=['scripts/create_wordnet_graph'],
      author = "Sharmila Gopirajan Sivakumar",
      author_email = "siva.sharmi@gmail.com",
      description = ("Getting better path similarity measures from wordnet by graphing the synsets"),
      install_requires = [
            "nltk>=2.0.1rc1",
            "networkx>=1.5"
        ]
      )
