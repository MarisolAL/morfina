import json
import os
import random
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError

# Paths to the card files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_FILE = os.path.join(BASE_DIR, "data", "cards.json")
REAL_CARDS_FILE = os.path.join(BASE_DIR, "real_cards.json")

# Game logic
class Game:
    def __init__(self):
        self.black_card = None
        self.white_cards = []

    def draw_black_card(self, all_black_cards):
        self.black_card = random.choice(all_black_cards)

    def draw_white_cards(self, all_white_cards):
        self.white_cards = random.sample(all_white_cards, 3)

# Load cards from JSON files
def load_cards():
    try:
        # Load main cards
        with open(CARDS_FILE, "r") as f:
            cards = json.load(f)

        # Check for "spicy" cards if the file exists
        if os.path.exists(REAL_CARDS_FILE):
            with open(REAL_CARDS_FILE, "r") as f:
                real_cards = json.load(f)
            # Combine spicy cards with main cards
            cards["black_cards"].extend(real_cards.get("black_cards", []))
            cards["white_cards"].extend(real_cards.get("white_cards", []))

        return cards
    except Exception as e:
        print(f"Error loading cards: {e}")
        return None

# Initialize game instance
game = Game()

# Views
def index(request):
    return render(request, "game/index.html")

def draw_cards(request):
    cards = load_cards()
    if not cards:
        return HttpResponseServerError("Could not load cards.")

    # Draw cards
    game.draw_black_card(cards["black_cards"])
    game.draw_white_cards(cards["white_cards"])

    return JsonResponse({
        "black_card": game.black_card,
        "white_cards": game.white_cards
    })
