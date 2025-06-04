# 🎯 Word Jumble Game

A fun, interactive two-player word jumble game built with Django and MongoDB. Players take turns unscrambling words to score points!

## 🚀 Features

- **Two-Player Gameplay**: Competitive word unscrambling between two players
- **MongoDB Integration**: Persistent game sessions and player data
- **Session Fallback**: Automatic fallback to session storage if MongoDB is unavailable
- **Word Bank Management**: Organized word collection with difficulty levels
- **Game Statistics**: Track wins, losses, and performance
- **Responsive Design**: Beautiful, animated UI with CSS animations

## 🛠️ Tech Stack

- **Backend**: Django 5.2.1
- **Database**: MongoDB with MongoEngine ODM
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS with animations
- **Session Management**: Django sessions (fallback)

## 📋 Prerequisites

- Python 3.8+
- MongoDB (optional - app works without it)
- pip (Python package manager)

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd jumble_words
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your settings
# For basic setup, you can use the defaults
```

### 5. MongoDB Setup (Optional)

**Option A: Local MongoDB**
1. Install MongoDB Community Server
2. Start MongoDB service
3. Update `.env` file:
   ```
   USE_MONGODB=True
   MONGODB_HOST=localhost
   MONGODB_PORT=27017
   MONGODB_DB_NAME=jumble_words_db
   ```

**Option B: MongoDB Atlas (Cloud)**
1. Create free account at MongoDB Atlas
2. Create a cluster and get connection string
3. Update `.env` file with your connection details

**Option C: Skip MongoDB**
- Leave `USE_MONGODB=False` in `.env`
- Game will use session storage (works perfectly!)

### 6. Run the Application
```bash
# If using MongoDB, populate the word bank
python manage.py populate_wordbank

# Start the development server
python manage.py runserver
```

### 7. Access the Game
Open your browser and go to: `http://127.0.0.1:8000/`

## 🎮 How to Play

1. **Start Game**: Enter player names, ages, and locations
2. **Take Turns**: Players alternate unscrambling words
3. **Score Points**: Correct answers earn points
4. **Win**: Player with most points after 10 rounds wins!

## 🔧 Configuration

### Environment Variables (.env)

```bash
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# MongoDB Settings
USE_MONGODB=False
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_DB_NAME=jumble_words_db
MONGODB_USERNAME=
MONGODB_PASSWORD=
```

## 📁 Project Structure

```
jumble_words/
├── jumble_words/          # Django project settings
│   ├── settings.py        # Main configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI configuration
├── myapp/                # Main application
│   ├── models.py         # MongoDB models
│   ├── views.py          # Game logic
│   ├── forms.py          # Django forms
│   ├── urls.py           # App URLs
│   ├── templates/        # HTML templates
│   ├── static/           # CSS, JS, images
│   └── management/       # Custom commands
├── requirements.txt      # Python dependencies
├── .env.example         # Environment template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🚀 Deployment

### Heroku Deployment

1. **Prepare for Heroku**:
   ```bash
   # Install Heroku CLI
   # Create Procfile
   echo "web: gunicorn jumble_words.wsgi" > Procfile
   
   # Install gunicorn
   pip install gunicorn
   pip freeze > requirements.txt
   ```

2. **Deploy**:
   ```bash
   heroku create your-app-name
   heroku config:set SECRET_KEY="your-production-secret-key"
   heroku config:set DEBUG=False
   git push heroku main
   ```

### Other Platforms

The app is ready for deployment on:
- **Railway**
- **Render**
- **DigitalOcean App Platform**
- **AWS Elastic Beanstalk**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Future Enhancements

- [ ] Multiplayer support (3+ players)
- [ ] Difficulty levels
- [ ] Timed rounds
- [ ] Leaderboards
- [ ] Word categories
- [ ] Mobile app version
- [ ] Real-time multiplayer with WebSockets

## 🐛 Troubleshooting

### Common Issues

1. **MongoDB Connection Error**:
   - Set `USE_MONGODB=False` in `.env` to use session storage
   - Check MongoDB service is running

2. **Secret Key Error**:
   - Generate new secret key: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

3. **Static Files Not Loading**:
   - Run `python manage.py collectstatic`

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Open an issue on GitHub
3. Contact the maintainers

---

**Happy Gaming! 🎮**
