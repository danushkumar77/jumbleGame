from mongoengine import Document, StringField, IntField, DateTimeField, ListField, BooleanField
from datetime import datetime

class Player(Document):
    name = StringField(max_length=50, required=True)
    age = IntField(min_value=1, required=True)
    place = StringField(max_length=50, required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'players',
        'indexes': ['name', 'created_at']
    }

    def __str__(self):
        return f"{self.name} ({self.age}) from {self.place}"


class GameSession(Document):
    player1_name = StringField(max_length=50, required=True)
    player1_age = IntField(min_value=1, required=True)
    player1_place = StringField(max_length=50, required=True)

    player2_name = StringField(max_length=50, required=True)
    player2_age = IntField(min_value=1, required=True)
    player2_place = StringField(max_length=50, required=True)

    current_round = IntField(default=1)
    max_rounds = IntField(default=10)
    current_player = StringField(max_length=50, required=True)

    player1_score = IntField(default=0)
    player2_score = IntField(default=0)

    used_words = ListField(StringField(max_length=50))
    current_word = StringField(max_length=50)

    is_completed = BooleanField(default=False)
    winner = StringField(max_length=50, null=True)

    created_at = DateTimeField(default=datetime.utcnow)
    completed_at = DateTimeField(null=True)

    meta = {
        'collection': 'game_sessions',
        'indexes': ['created_at', 'is_completed']
    }

    def __str__(self):
        return f"{self.player1_name} vs {self.player2_name} - Round {self.current_round}"


class WordBank(Document):
    word = StringField(max_length=50, required=True, unique=True)
    difficulty_level = StringField(max_length=20, choices=['easy', 'medium', 'hard'], default='medium')
    category = StringField(max_length=30, default='general')
    times_used = IntField(default=0)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'word_bank',
        'indexes': ['word', 'difficulty_level']
    }

    def __str__(self):
        return self.word


class GameResult(Document):
    game_session_id = StringField(required=True)

    player1_name = StringField(max_length=50, required=True)
    player1_score = IntField(required=True)

    player2_name = StringField(max_length=50, required=True)
    player2_score = IntField(required=True)

    winner = StringField(max_length=50, null=True)
    total_rounds = IntField(required=True)

    game_duration_minutes = IntField(null=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'game_results',
        'indexes': ['created_at', 'winner']
    }

    def __str__(self):
        return f"{self.player1_name} vs {self.player2_name} - Winner: {self.winner}"
