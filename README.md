# Movie_Ticket_Booking

### way to use the application

1) create account: 
url: localhost:8000/user

![user_create](screenshots/create_user.png?raw=true "Create User")

2) Login using the credentials:
url: localhost:8000/user/login

![user_create](screenshots/login.png?raw=true "Login User")

3) List of all the movies:
url: localhost:8000

click on the highlighted url to get details of the movie.

![user_create](screenshots/Movies_list.png?raw=true "Movies List")

4) Detail of movie along with available shows and few analytics like Total collection of the movie, total shows and total tickets sold:
url: localhost:8000/movies/<int>

click on the highlighted url to get details of the show.

![user_create](screenshots/Movies_detail.png?raw=true "Movie Detail")

5) Detail of Show along with available seats showing booked as false:
url: localhost:8000/shows/<int>

click on the highlighted url to book that particular seat (cannot book the seats with "booked:true" value as they are already booked).

![user_create](screenshots/Show_detail.png?raw=true "Show Detail")

6) Book Seat by clicking on POST:


![user_create](screenshots/Book_ticket.png?raw=true "Book Ticket")

7) For booking multiple seats click on multi url in show detail page:
    In the next page you will be prompted to enter the number of seats you would like to book and submitting it will book the seats such that there is no gap between seats and if such seats are not available it will show other movie and its timing where seats are available together

![user_create](screenshots/multiple.png?raw=true "Multiple Ticket")


### Endpoints for CRUD of movie, theatre, layout...:

1) Theatre:
    theatres/create
    theatres/<int:pk>
    theatres/<int:pk>/update
    theatres/<int:pk>/delete

2) Movie:
    movies/create
    movies/<int:pk>
    movies/<int:pk>/update
    movies/<int:pk>/delete

3) Auditorium:
    halls/create
    halls/<int:pk>
    halls/<int:pk>/update
    halls/<int:pk>/delete

4) Layout (Here on entering seats per row(minimum 6) and number of rows an layout with max 6 aisle seats will be created):
    halls/create

5) Seats:
    seats/create
    seats/<int:pk>
    seats/<int:pk>/update
    seats/<int:pk>/delete

6) Shows:
    shows/create
    shows/<int:pk>
    shows/<int:pk>/update
    shows/<int:pk>/delete
