# MealsRater_API_Django 🍽️

A Django REST Framework API that allows authenticated users to rate meals.  
Each user can submit only one rating per meal, and the system updates the rating if the user resubmits.

## 🚀 Features

- 🧾 List available meals with details
- ⭐ Submit or update your rating for a meal
- 🔐 User authentication & token-based access
- 📊 Each meal displays average rating and number of ratings
- 🛠️ Admin panel to manage meals and user data

## ⚙️ Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite (development)
- Postman (testing)

## 📂 How to Run the Project

```bash
git clone https://github.com/mousa8080/MealsRater_API_Django.git
cd MealsRater_API_Django
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
