#This is the Personal Movie Tracker (PMT) application.
#It allows users to add, view, search, and delete movies from their personal collection.
#Movies are stored in a list of dictionaries, with each dictionary representing a movie and its details

import json #So I can make .json files and mutate them
import os #So I can control where the movies.json file is made
import requests #For API integration to OMBd
from dotenv import load_dotenv #To load environment variables from a .env file
load_dotenv()  # Load environment variables from .env file
OMDB_API_KEY = os.getenv('OMDB_API_KEY')  # Get OMDB API key from environment variable
OMDB_API_URL = os.getenv('OMDB_API_URL')  # Get OMDB API

# __file__ is a special variable that contains the path to the current script
# Example: '/Users/p/Documents/Code/Python Playground/Day 4/Personal Movie Tracker (PMT)/pmt.py'

# os.path.abspath(__file__) converts it to absolute path (full path from root)
# In case __file__ is relative like 'pmt.py', this makes it complete
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# os.path.join() combines directory + filename in a safe, cross-platform way
MOVIES_FILE = os.path.join(SCRIPT_DIR, 'movies.json')

#Helper Functions
def load_movies():
    try:
        with open(MOVIES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_movies():
    with open(MOVIES_FILE, 'w') as file:
        json.dump(movies, file, indent=4)

#Load all the movies when the program starts
movies = load_movies()

watched_indicator = '✓'
to_watch_indicator = '○'

def print_movie_list():
    #Display updated movie list for toggle_rating & toggle_status, just copied from view_movies function
    #Wanted to avoid infinite function calls so I just copied the for loop here
    for i, (title, info) in enumerate(movies.items(), start=1):
        status_icon = watched_indicator if info['status'] == 'watched' else to_watch_indicator
        print(f'{i} | {status_icon} | {title} | [{info['genre']}] - Rating: {info['rating']}')

#Function to fetch movie data from OMDB API
#Can integrate this into add_movies to autofill information later
def fetch_movie_data_from_omdb(movie_title):
    params = {
        'apikey' : OMDB_API_KEY,
        't' : movie_title, #Title search parameter
        'type' : 'movie' #Specify we are searching for movies
    }

    response = requests.get(OMDB_API_URL, params=params) #Make the API request
    data = response.json() #Parse the JSON response

    if data['Response'] == 'True':
        return data
    else:
        print(f'Error fetching data for "{movie_title}": {data["Error"]}')
        return None

#Toggle for movie rating using '✦' symbol
def toggle_rating(movie_title):
    if movie_title not in movies:
        print(f'"{movie_title}" not found in your movies')
        return
    if movies[movie_title]['status'] != 'watched':
        print(f'You can only rate movies marked as watched.')
        return
    rating = input('Enter a new rating (1-5): ').strip()
    if rating in ['1', '2', '3', '4', '5']:
        movies[movie_title]['rating'] = '✦' * int(rating)
        print(f'✓ Updated rating for "{movie_title}" to {movies[movie_title]["rating"]}')
        save_movies()
        print_movie_list()
    else:
        print('Invalid rating. Please enter a number between 1 and 5.')
    
#Toggle movie status between watched and to watch
def toggle_status(movie_title):
    if movie_title not in movies:
        print(f'"{movie_title}" not found in your list')
        return
    
    current_status = movies[movie_title]['status'] #Get current status

    if current_status == 'watched':
        movies[movie_title]['status'] = 'to watch'
        movies[movie_title]['rating'] = None #Reset rating when marking as to watch
        print(f'✓ Marked "{movie_title}" as to watch')
    else:
        movies[movie_title]['status'] = 'watched'
        toggle_rating(movie_title)  #Prompt for rating when marking as watched
        print(f'✓ Marked "{movie_title}" as watched')

    save_movies()
    print_movie_list()

# Function to delete movies from the movies.json file
def delete_movie():
    movie_title = input("Enter movie to delete: ").strip()
    if movie_title in movies:
        del movies[movie_title]
        save_movies()
        print(f"✓ Deleted '{movie_title}'")
    else:
        print("Movie not found")

#Menu to toggle status or change rating for the view movies function
def toggle_menu():
    while True:
        print('\n1. Would you like to toggle the status of a movie?')
        print('\n2. Would you like to change the rating of a movie?')
        print('\n3. Would you like to delete a movie?')
        print('\n4. Return to Main Menu')

        choice = input('Enter a number (1-4): ').strip()
        if choice == '1' : 
            movie_title = input('Enter the movie title to toggle status: ').strip()
            toggle_status(movie_title)
        elif choice == '2':
            movie_title = input('Enter the movie title to change rating: ').strip()
            toggle_rating(movie_title)
        elif choice == '3':
            delete_movie()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

#Function to add movies to the movies.json file
def add_movies():
    movie = input('Enter the movie name: ')
    status = 'to watch'
    genre = input('Enter the movie genre: ')

    if movie in movies:
        print(f'"{movie}" is already in your list!')
        return
    
    rating = None

    movies[movie] = {
        'status': status,
        'genre': genre,
        'rating': rating
        }
    
    save_movies()
    print(f'✓ Added "{movie}" to your movie list!')
    print_movie_list()
    


#Function to view movies from the movies.json file
def view_movies(): 
    #Check if there are any movies to display
    if not movies:
        print('No movies in your list. Add some first!')
        return
    
    #Display filter options
    print('\n What would you like to view?')
    print('='*60)
    print('1. All Movies')
    print('2. Watched Movies')
    print('3. To Watch Movies')
    
    #Get user choice for filtering
    filter_choice = input('Enter choice (1-3): ').strip()
    if filter_choice == '1':
        filtered_movies = movies
        header = 'ALL MOVIES:'
    if filter_choice == '2':
        filtered_movies = {title: info for title, info in movies.items() if info['status'] == 'watched'}
        header = 'WATCHED MOVIES:'
    elif filter_choice == '3':
        filtered_movies = {title: info for title, info in movies.items() if info['status'] == 'to watch'}
        header = 'TO WATCH MOVIES:'
    
    #Check if filter resulted in empty list
    if not filtered_movies:
        print('No movies found for the selected filter.')
        return
    
    #Display the filtered movies
    print('='*60)
    print(f'\n{header}'.center(60))
    print('='*60)

    #This for loop allows me to get all the movies with 3 lines of code in a for loop accessing a dict within a dict which is filtered above
    for i, (title, info) in enumerate(filtered_movies.items(), start=1):
        status_icon = watched_indicator if info['status'] == 'watched' else to_watch_indicator
        print(f'{i} | {status_icon} | {title} | [{info['genre']}] - Rating: {info['rating']}')
    toggle_menu()
    
def show_movie_stats():
    total_movies = len(movies)
    watched_movies = sum(1 for stat in movies.values() if stat['status'] == 'watched')
    to_watch_movies = total_movies - watched_movies
    print(f'\nTotal Movies: {total_movies} ')
    print(f'|| Watched Movies: {watched_movies} ')
    print(f'|| To Watch Movies: {to_watch_movies}')
    print(f'|| Watched Percentage: { (watched_movies / total_movies * 100) if total_movies > 0 else 0:.2f}% ') #Avoid division by zero

    print('\nMovies by Genre:')
    genre_count = {}
    for stat in movies.values():
        genre = stat['genre']
        genre_count[genre] = genre_count.get(genre, 0) + 1
    for genre, count in genre_count.items():
        print(f'|| {genre}: {count}')


    

#Time to build the main menu:
#As of right now I believe this should be the first thing to make in order to layout the program flow
#While its running we need to display the title, 1. add movie, 2. view movies, 3. mark as watched, 4.exit)
#^Subject to change

def main_menu():
    while True:
        print('\n🎬 MOVIE TRACKER 🎬')
        print('1. Add A Movie')
        print('2. View All Movies') 
        print('3. Your Movie Stats')
        print('4. Exit')
    
        choice = input('\nEnter choice (1-4): ').strip()

        if choice == '1':
            add_movies()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            show_movie_stats()
        elif choice == '4':
            print('Goodbye')
            break
        else:
            print('Invalid choice')
        
main_menu()