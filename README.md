#  Blog + Comment System API (No DRF)

A Django-based backend API for blogging, user authentication, and commenting — built **without Django REST Framework** using **function-based views** and `JsonResponse`.

---

##  Features

- User Registration and Login (session-based auth)
- Create blog posts (authenticated users only)
- View all posts
- View post details with comments
- Comment on posts (authenticated users only)

---

##  Tech Stack

- Python 3
- Django (core)
- SQLite (default)
- Function-based views (FBV)
- JsonResponse-based API

---

##  Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/blog-api.git
cd blog-api

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
```

---

## 📬 API Endpoints & Examples

### 🧑 Register

`POST /api/register/`
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "123456"
}
```

---

###  Login

`POST /api/login/`
```json
{
  "username": "johndoe",
  "password": "123456"
}
```

---

### ✍️ Create Post (Auth Required)

`POST /api/create-post/`
```json
{
  "title": "My First Blog",
  "content": "This is a test blog post"
}
```

---

###  List All Posts

`GET /api/posts/`

---

###  View Post Details with Comments

`GET /api/post/<id>/`

---

###  Comment on a Post (Auth Required)

`POST /api/post/<id>/comment/`
```json
{
  "text": "Awesome post!"
}
```

---

## 🔐 Authentication

- Uses Django's built-in `authenticate` + session login.
- Auth-required endpoints: create-post, comment.

---

##  Folder Structure

```
blog_api/
├── blog_api/
├── core/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

##  Author

Built by **Piyush Bhoyar**  
GitHub: [Piyush22070](https://github.com/Piyush22070)