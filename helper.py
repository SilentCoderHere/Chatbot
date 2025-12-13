from re import fullmatch, sub
from time import strftime

from levenshtein import levenshtein


def getCorrectSentence(sentence: str, words: list[str]) -> str:
    correctedSentence = ""
    for word in sentence.split():
        minDistance = float("inf")
        correctWord = ""
        for wordFromJson in words:
            distance = levenshtein(word, wordFromJson)
            if distance < minDistance:
                minDistance = distance
                correctWord = wordFromJson
        correctedSentence += correctWord + " "
    return correctedSentence.strip()


def isMathMessage(text: str) -> bool:
    return bool(fullmatch(r"[0-9+\-*/^%\s\(\)]+", text))


def getResponse(sentence: str, words: list[str]) -> str:
    if isMathMessage(sentence):
        sentence = sub(r"\^", "**", sentence)
        try:
            return eval(sentence)
        except ZeroDivisionError:
            return "I can't divide by zero."
        except Exception:
            return "I can't do that."

    sentence = getCorrectSentence(sentence, words)
    sentence_lower = sentence.lower()
    words_in_sentence = set(sentence_lower.split())  # For faster checking

    # Main responses using all() for keyword matching
    if all(word in words_in_sentence for word in ["how", "are", "you"]):
        return "I'm doing great, thanks for asking! How about you?"

    elif any(word in sentence_lower for word in ["hello", "hi", "hey", "howdy"]):
        return "Hi there! What's up?"

    elif all(word in words_in_sentence for word in ["what", "name"]) or all(
        word in words_in_sentence for word in ["your", "name"]
    ):
        return "I'm ChatBot! Nice to meet you."

    elif all(word in words_in_sentence for word in ["what", "do"]) or all(
        word in words_in_sentence for word in ["what", "can"]
    ):
        return "I can chat, tell jokes, give the time/date, and do simple math!"

    elif "time" in words_in_sentence:
        return f"It's {strftime('%H:%M')}"

    elif "date" in words_in_sentence or "today" in words_in_sentence:
        return f"Today is {strftime('%B %d, %Y')}"

    elif "day" in words_in_sentence:
        return f"It's {strftime('%A')}"

    elif all(word in words_in_sentence for word in ["who", "made"]) or all(
        word in words_in_sentence for word in ["who", "created"]
    ):
        return "I was made by a developer."

    elif all(word in words_in_sentence for word in ["good", "morning"]):
        return "Good morning! Have a great day."

    elif all(word in words_in_sentence for word in ["good", "afternoon"]):
        return "Good afternoon!"

    elif all(word in words_in_sentence for word in ["good", "evening"]):
        return "Good evening!"

    elif all(word in words_in_sentence for word in ["good", "night"]):
        return "Good night! Sleep well."

    elif "thank" in sentence_lower or "thanks" in sentence_lower:
        return "You're welcome!"

    elif all(word in words_in_sentence for word in ["i'm", "fine"]) or all(
        word in words_in_sentence for word in ["i'm", "good"]
    ):
        return "Glad to hear that!"

    elif "bored" in words_in_sentence:
        return "Want to chat or hear a joke?"

    elif "tired" in words_in_sentence:
        return "Maybe take a break!"

    elif "hungry" in words_in_sentence:
        return "Time for a snack!"

    elif "joke" in words_in_sentence:
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif "old" in words_in_sentence or "age" in words_in_sentence:
        return "I was created recently!"

    elif all(word in words_in_sentence for word in ["where", "from"]) or all(
        word in words_in_sentence for word in ["where", "live"]
    ):
        return "I live in the cloud!"

    elif "sleep" in words_in_sentence:
        return "Nope, I'm always here!"

    elif all(word in words_in_sentence for word in ["favorite", "color"]) or all(
        word in words_in_sentence for word in ["favourite", "colour"]
    ):
        return "I like blue!"

    elif all(word in words_in_sentence for word in ["favorite", "food"]) or all(
        word in words_in_sentence for word in ["favourite", "food"]
    ):
        return "I don't eat, but pizza seems popular!"

    elif "fact" in words_in_sentence:
        return "Honey never spoils!"

    elif "ai" in sentence_lower or "artificial" in sentence_lower:
        return "AI helps computers do smart things."

    elif any(word in sentence_lower for word in ["bye", "goodbye", "see you"]):
        return "Bye! Have a great day!"

    elif any(word in sentence_lower for word in ["yes", "yep", "sure", "ok", "okay"]):
        return "Alright!"

    elif any(word in sentence_lower for word in ["no", "nope"]):
        return "Okay, no problem."

    elif any(word in sentence_lower for word in ["cool", "awesome", "great", "nice"]):
        return "Thanks!"

    elif any(word in sentence_lower for word in ["lol", "haha", "funny"]):
        return "Glad you liked it!"

    elif any(word in sentence_lower for word in ["wow", "omg"]):
        return "Right?"

    elif any(word in sentence_lower for word in ["oops", "my bad"]):
        return "No worries!"

    # Default
    else:
        if sentence_lower.endswith("?"):
            return "Good question! I'm still learning."
        else:
            return "I'm not sure how to respond to that."
