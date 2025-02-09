📌 Project Overview
In today's digital era, movie streaming platforms offer vast libraries, making it difficult for users to decide what to watch next. Our Movie Recommendation System simplifies this process by providing personalized movie suggestions based on user input. The system leverages IMDb’s Top 1000 Movies & TV Shows and identifies recommendations based on matching attributes such as genre, director, cast, and ratings.

*Note: Please install this database to be used for the project
https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows?fbclid=IwZXh0bgNhZW0CMTEAAR3BgW2H6G3-zMOwwBphAsMfMQXGNbnVrpJk9bx_YvLL-ghX_YSAF4DQ4TU_aem_knOWu1DJr1OeqOuMcatciQ

Features
- Tailored Movie Recommendations
Users can enter a movie title, and the system will recommend similar movies based on matching attributes.
Recommendations are prioritized using heaps and priority queues, ensuring relevant and refined suggestions.
- Sortable Movie Database

Users can browse and sort movies dynamically using different attributes:
- Title
- Release Year
- Runtime
- Director
- IMDb Rating
- Metascore
  
Algorithms Used
- MergeSort → Efficient sorting for the movie database.
- Binary Search → Fast and optimized search for user recommendations.
- Heaps & Priority Queues → Ranking and prioritizing recommendations based on relevance.

Tech Stack
- Python (Django)
- CSV Data Handling (for importing IMDb database)
- Django ORM (for querying movie data)
- HTML/CSS & JavaScript (for frontend UI)

Getting Started
- Clone the Repository git clone https://github.com/Tisme18/movie-recommendation-system.git
cd movie-recommendation-system
- Install Dependencies pip install -r requirements.txt
- Run Database Migrations python manage.py migrate
- Start the Development Server python manage.py runserver
- Access the Application Open http://127.0.0.1:8000/ in your browser.
