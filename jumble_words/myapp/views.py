from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PlayerInfoForm, GuessForm
from .models import Player, GameSession, WordBank, GameResult
from datetime import datetime
import random

# Get MongoDB setting from Django settings
from django.conf import settings
USE_MONGODB = getattr(settings, 'USE_MONGODB', False)

# Fallback word list
WORDS = ["python", "debug", "object", "class", "binary", "stack", "queue", "server", "internet", "array"]

def jumble_word(word):
    chars = list(word)
    random.shuffle(chars)
    jumbled = ''.join(chars)
    return jumbled if jumbled != word else jumble_word(word)

def get_random_word():
    try:
        count = WordBank.objects.count()
        if count > 0:
            return WordBank.objects.skip(random.randint(0, count - 1)).first().word
    except Exception:
        pass
    return random.choice(WORDS)

def home(request):
    if request.method == "POST":
        form1 = PlayerInfoForm(request.POST, prefix="p1")
        form2 = PlayerInfoForm(request.POST, prefix="p2")
        if form1.is_valid() and form2.is_valid():
            try:
                p1 = form1.cleaned_data
                p2 = form2.cleaned_data

                game = GameSession(
                    player1_name=p1["name"], player1_age=p1["age"], player1_place=p1["place"],
                    player2_name=p2["name"], player2_age=p2["age"], player2_place=p2["place"],
                    current_player=p1["name"]
                )
                game.save()
                request.session["game_session_id"] = str(game.id)
                messages.success(request, "Game started successfully!")
                return redirect("play")

            except Exception as e:
                messages.error(request, f"MongoDB error: {e}")
                return redirect("home")
    else:
        form1 = PlayerInfoForm(prefix="p1")
        form2 = PlayerInfoForm(prefix="p2")
    return render(request, "myapp/home.html", {"form1": form1, "form2": form2})

def play(request):
    if USE_MONGODB and "game_session_id" in request.session:
        return play_mongodb(request)
    return redirect("home")

def play_mongodb(request):
    try:
        session_id = request.session["game_session_id"]
        game = GameSession.objects.get(id=session_id)

        if game.is_completed:
            return redirect("game_over")

        if request.method == "POST":
            form = GuessForm(request.POST)
            if form.is_valid():
                guess = form.cleaned_data["guess"].lower()
                if guess == game.current_word:
                    messages.success(request, f"🎉 Correct, {game.current_player}!")
                    if game.current_player == game.player1_name:
                        game.player1_score += 1
                    else:
                        game.player2_score += 1
                else:
                    messages.error(request, f"❌ Wrong! The word was '{game.current_word}'")

                # Switch turn
                game.current_player = game.player2_name if game.current_player == game.player1_name else game.player1_name
                game.current_round += 1

                if game.current_round > game.max_rounds:
                    game.is_completed = True
                    game.completed_at = datetime.utcnow()
                    if game.player1_score > game.player2_score:
                        game.winner = game.player1_name
                    elif game.player2_score > game.player1_score:
                        game.winner = game.player2_name
                    else:
                        game.winner = "It's a tie!"
                    game.save()

                    # Save result
                    GameResult(
                        game_session_id=str(game.id),
                        player1_name=game.player1_name, player1_score=game.player1_score,
                        player2_name=game.player2_name, player2_score=game.player2_score,
                        winner=game.winner, total_rounds=game.max_rounds
                    ).save()
                    return redirect("game_over")

                game.save()
                return redirect("play")
        else:
            # Start new round
            available = list(set([get_random_word() for _ in range(10)]) - set(game.used_words))
            if not available:
                game.used_words = []
                available = [get_random_word() for _ in range(5)]

            word = random.choice(available)
            game.current_word = word
            game.used_words.append(word)
            game.save()

            form = GuessForm()
            return render(request, "myapp/play.html", {
                "round_info": f"Round {game.current_round} of {game.max_rounds}",
                "jumbled_word": jumble_word(word),
                "current_player": game.current_player,
                "player1_name": game.player1_name,
                "player2_name": game.player2_name,
                "player1_score": game.player1_score,
                "player2_score": game.player2_score,
                "form": form
            })
    except GameSession.DoesNotExist:
        messages.error(request, "Game session not found.")
        return redirect("home")

def game_over(request):
    try:
        session_id = request.session["game_session_id"]
        game = GameSession.objects.get(id=session_id)
        return render(request, "myapp/game_over.html", {
            "player1_name": game.player1_name,
            "player2_name": game.player2_name,
            "player1_score": game.player1_score,
            "player2_score": game.player2_score,
            "winner": game.winner,
            "using_mongodb": True
        })
    except GameSession.DoesNotExist:
        messages.error(request, "Game not found.")
        return redirect("home")
