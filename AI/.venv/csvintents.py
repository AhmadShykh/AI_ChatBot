import csv
import json
import random

def generate_intents(csv_file, output_file):
    intents = {"intents": []}

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames

        for row in reader:
            game_name = row['name']

            for column in columns:
                if column == 'name':  # Skip the 'name' column
                    continue

                tag = column.replace('_', ' ').capitalize()
                patterns = [
                    f"What are the {tag} of {game_name}?",
                    f"Tell me about the {tag} in {game_name}",
                    f"Any {tag} for {game_name}?",
                    f"What can you tell me about {tag} in {game_name}?",
                    f"Give me some insights about {tag} in {game_name}",
                    f"Do you have any details on {tag} for {game_name}?",
                    f"Could you provide information on {tag} for {game_name}?",
                    f"Tell me more about the {tag} aspect of {game_name}",
                    f"Can you elaborate on {tag} in {game_name}?",
                    f"I'd like to learn more about {tag} in {game_name}",
                    f"What's the deal with {tag} in {game_name}?",
                    f"Could you tell me something about {tag}?",
                    f"What do you know about {tag}?",
                    f"I'm curious about {tag}.",
                    f"Can you give me some details on {tag}?",
                    f"I'd like to know about {tag}.",
                    f"Tell me something interesting about {tag}.",
                    f"Give me some information on {tag}."
                ]

                custom_questions = []
                if column == "release date":
                    custom_questions = [

                    ]
                elif column == "english":
                    custom_questions = [

                    ]

                elif column == "developer":
                    custom_questions = [

                    ]

                elif column == "publisher":
                    custom_questions = [

                    ]

                elif column == "platforms":
                    custom_questions = [

                    ]

                elif column == "required age":
                    custom_questions = [

                    ]

                elif column == "categories":

                    custom_questions = [

                    ]
                elif column == "genres":
                    custom_questions = [

                    ]

                elif column == "steamspy tags":
                    custom_questions = [

                    ]

                elif column == "achievements":
                    custom_questions = [

                    ]

                elif column == "positive ratings":
                    custom_questions = [

                    ]

                elif column == "negative ratings":
                    custom_questions = [

                    ]

                elif column == "average playtime":
                    custom_questions = [

                    ]

                elif column == "median playtime":
                    custom_questions = [

                    ]

                elif column == "owners":
                    custom_questions = [

                    ]

                elif column == "price":
                    custom_questions = [

                    ]

                elif column == "detailed description":
                    custom_questions = [

                    ]

                elif column == "about the game":
                    custom_questions = [

                    ]

                elif column == "short description":
                    custom_questions = [

                    ]

                patterns.extend(custom_questions)
                response = row[column] if row[column] else choose_response(tag)

                intent = {"tag": column, "patterns": patterns, "responses": [response]}
                intents["intents"].append(intent)

    with open(output_file, 'w') as outfile:
        json.dump(intents, outfile, indent=4)

def choose_response(tag):
    responses = [
        f"Unfortunately, I don't have any information about {tag}.",
        f"I'm sorry, there's nothing to share about {tag}.",
        f"I don't have any data regarding {tag}.",
        f"I'm afraid I can't provide any details about {tag} at the moment.",
        f"Looks like there's no information available for {tag}.",
        f"Sorry, I couldn't find any details about {tag}.",
        f"I don't have any specifics about {tag} right now."
    ]
    return random.choice(responses)

# Example usage:
generate_intents('steam_cleaned.csv', 'intents_1.json')
