class Movie():
    def __init__(self):
        print("I am creating an movie")

    def watch_movie(self):
        duration = self.calc_duration()
        print("I'm watching a movie de", duration, "minutos")

    def calc_duration(self):
        return 130


movie1 = Movie()
movie1.watch_movie()
