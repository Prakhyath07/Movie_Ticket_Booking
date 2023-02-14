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

![user_create](screenshots/Movies_list.png?raw=true "Login User")

4) Detail of movie along with available shows:
url: localhost:8000/movies/<int>

click on the highlighted url to get details of the show.

![user_create](screenshots/Movies_detail.png?raw=true "Login User")

5) Detail of Show along with available seats showing booked as false:
url: localhost:8000/shows/<int>

click on the highlighted url to book that particular seat (cannot book the seats with "booked:true" value as they are already booked).

![user_create](screenshots/Show_detail.png?raw=true "Login User")

6) Book Seat by clicking on POST:


![user_create](screenshots/Book_ticket.png?raw=true "Login User")
