from django.core.management.base import BaseCommand
from myapp.models import WordBank


class Command(BaseCommand):
    help = 'Populate the MongoDB word bank with initial words'

    def handle(self, *args, **options):
        # Words from the original views.py
        words = [
            "python", "computer", "programming", "algorithm", "variable", "function", 
            "keyboard", "monitor", "software", "developer", "database", "internet", 
            "network", "security", "hardware", "interface", "compile", "debug", 
            "syntax", "package", "library", "framework", "server", "client", 
            "protocol", "encryption", "iteration", "recursion", "exception", "boolean",
            "array", "string", "integer", "float", "class", "object", "inheritance", 
            "polymorphism", "encapsulation", "abstraction", "thread", "process", 
            "cache", "cookie", "session", "bit", "byte", "pixel", "resolution", 
            "graphics", "algorithm", "data", "cloud", "storage", "virtual", "compile", 
            "execute", "binary", "hexadecimal", "stack", "queue", "tree", "graph", 
            "hash", "database", "query", "index", "transaction", "commit", "rollback"
        ]

        # Clear existing words to avoid duplicates
        WordBank.drop_collection()
        self.stdout.write(self.style.WARNING('Cleared existing word bank'))

        # Categorize words by difficulty based on length and complexity
        easy_words = []
        medium_words = []
        hard_words = []

        for word in set(words):  # Remove duplicates
            if len(word) <= 5:
                easy_words.append(word)
            elif len(word) <= 8:
                medium_words.append(word)
            else:
                hard_words.append(word)

        # Add easy words
        for word in easy_words:
            WordBank(
                word=word,
                difficulty_level='easy',
                category='programming'
            ).save()

        # Add medium words
        for word in medium_words:
            WordBank(
                word=word,
                difficulty_level='medium',
                category='programming'
            ).save()

        # Add hard words
        for word in hard_words:
            WordBank(
                word=word,
                difficulty_level='hard',
                category='programming'
            ).save()

        total_words = len(set(words))
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated word bank with {total_words} words:\n'
                f'- Easy: {len(easy_words)} words\n'
                f'- Medium: {len(medium_words)} words\n'
                f'- Hard: {len(hard_words)} words'
            )
        )
