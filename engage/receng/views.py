from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

#Sign Up view
def signup(request):
    if request.method =='POST':
        #collects input
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        genres = request.POST.getlist('genreOptions')
        langs = request.POST.getlist('langOptions')

        if password == password2:
            #if username already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used.')
                return redirect('signup')
            else:
                #registering new user
                user = User.objects.create_user(username=username, password=password)
                user.save()

                #collect and store the preferences input
                if '0' in genres: action=5
                else: action = 0
                if '1' in genres: comedy=5
                else: comedy = 0
                if '2' in genres: drama=5
                else: drama = 0
                if '3' in genres: fantasy=5
                else: fantasy = 0
                if '4' in genres: horror=5
                else: horror = 0
                if '5' in genres: romance=5
                else: romance = 0
                if '6' in genres: scifi=5
                else: scifi = 0
                if '7' in genres: thriller=5
                else: thriller = 0

                if 'Telugu' in langs: telugu = True
                else: telugu = False
                if 'Hindi' in langs: hindi = True
                else: hindi = False
                if 'English' in langs: english = True
                else: english = False

                #creating the profile model object
                profile_ = Profile.objects.create(action=action, comedy=comedy, drama=drama, fantasy=fantasy,
                                            horror=horror, romance=romance, scifi=scifi, thriller=thriller,
                                            telugu=telugu, hindi=hindi, english=english)
                profile_.userid = user.id #to list the user and profile objects
                movies = Movie.objects.all()
                for movie in movies:
                    profile_.to_watch.add(movie)
                profile_.save() #registered the profile object

                #redirects to the login page for the registered user to login
                return redirect('login')
        else:
            messages.info(request, 'Cannot confirm Password')
            return redirect('signup') #stays in sgnup page
    else:  
        #if the request method is not POST, template is rendered
        return render(request, 'signup.html')

# Login view
def login(request):
    if request.method == 'POST':
        #collecting input credentials
        username = request.POST['username']
        password = request.POST['password']
        #checking login credentials
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            #getting pref input of logged in user
            prof = Profile.objects.get(userid = user.id)
            
            movies = prof.to_watch.all() #contains list of movies in to-watch list
            pList = []
            mList = []
            topMovies = [] #to pass to the template
    
            for movie in movies:

                #calculating priority of each movie (O(n) complexity)
                priority = 0.0
                # adds score as to the extent the movie belongs to a genre times the extend of user likage of the genre
                priority += prof.action*movie.action
                priority += prof.comedy*movie.comedy
                priority += prof.drama*movie.drama
                priority += prof.fantasy*movie.fantasy
                priority += prof.horror*movie.horror
                priority += prof.romance*movie.romance
                priority += prof.scifi*movie.scifi
                priority += prof.thriller*movie.thriller
        
                priority += float(movie.rating) #includes the rating score
        
                #if the movie language is preferred by the user
                if movie.lang == 'Telugu' and prof.telugu: priority += 2
                elif movie.lang == 'Hindi' and prof.hindi: priority += 2
                elif movie.lang == 'English' and prof.english: priority += 2

                pList.append(priority)
                mList.append(movie)

            pmList = list(zip(pList, mList))
            pmList.sort(reverse=True, key=lambda x: x[0]) #list is sorted
            
            for i in range(min(5,len(pmList))):
                topMovies.append(pmList[i][1])

            return render(request, 'page.html', {'topMovies':topMovies}) #sends data to the html page
        else:
            #if login credentials are invalid
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        #if the request method is not POST, template is rendered
        return render(request, 'login.html')