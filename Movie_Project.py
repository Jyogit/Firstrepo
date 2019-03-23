class Movie:
    def __init__(self,fileName):
        self.fileName = fileName
        print("Welcome to ABC Movie Database")

    def read_File(self):
        open_file = open(self.fileName)
        from csv import reader
        read_file = reader(open_file)
        self.movie_data = list(read_file)
        self.movie_data = self.movie_data[1:]


    def view_Coll(self):
        print("----------------------------------------------------------")
        print("                 ABC Movie Database                         ")
        print("----------------------------------------------------------")
        from tabulate import tabulate
        print(tabulate(self.movie_data,headers = ["Movie Name","Year","Director"]))


    def add_Movie(self,movie_name,movie_year,movie_director):
        self.movie_data.append([movie_name,movie_year,movie_director])



    #def write_File(self):
    #    from csv import writer
     #   with open(self.fileName,'a') as fd:
     #       wr = writer(fd)
     #       wr.writerows(self.updated_row)

    def find_Movie(self,movie_name):
        movie_found = False
        for row in self.movie_data:
            if movie_field in row:
                movie_found = True
                print("Movie: {}".format(row[0]))
                print("Year: {}".format(row[1]))
                print("Director: {}".format(row[2]))

        if not movie_found:
            print("{} is not present in the movie collection ".format(movie_name))

movie = Movie("movie_list.csv")
movie.read_File()
while True:
    print()
    print("Enter 1 to see the movie collection")
    print("Enter 2 to add a movie to the collection")
    print("Enter 3 to find a movie")
    print("Enter 4 to exit")
    userChoice = int(input())
    print()
    if userChoice is 1:
        print()
        print("The Movie Collection")
        movie.view_Coll()
        print()
    elif userChoice is 2:
        print()
        print("Enter movie name: ")
        movie_name = input()
        print("Enter the movie year: ")
        movie_year = int(input())
        print("Enter the movie director: ")
        movie_director = input()
        movie.add_Movie(movie_name,movie_year,movie_director)
        movie.view_Coll()
        #movie.write_File()
        print()
    elif userChoice is 3:
        print()
        print("Enter the field to find movie: Name, Year, Director")
        movie_field = input()
        movie.find_Movie(movie_field)
        print()
    elif userChoice is 4:
        quit()
