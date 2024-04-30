import csv
import json
import random
import gc
import sys

def generate_intents(csv_file, output_file):
    intents = {"intents": []}
    row_counter = 0

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames

        for row in reader:
            if row_counter >= 100:  # Check if 100 rows have been processed
                sys.exit("Reached 100 rows. Exiting program.")  # Exit the program
            game_name = row['name']

            for column in columns:
                if column == 'name':  # Skip the 'name' column
                    continue

                tag = column.replace('_', ' ').capitalize()
                patterns = [
                    f"What is {tag} of {game_name}?",
                    f"Tell me about the {tag} in {game_name}",
                    f"Any {tag} for {game_name}?",
                    f"What can you tell me about {tag} in {game_name}?",
                    f"Give me some insights about {tag} in {game_name}",
                    f"Do you have any details on {tag} for {game_name}?",
                    f"Could you provide information on {tag} for {game_name}?",
                    f"Tell me more about the {tag} aspect of {game_name}",
                    f"Can you elaborate on {tag} in {game_name}?",
                    f"I'd like to learn more about {tag} in {game_name}",
                    f"What's the deal with {tag} in {game_name}?"
                ]

                custom_questions = []
                if column == "release_date":
                    custom_questions = [
                        f"When was {game_name} released?",
                        f"What is the launch date of {game_name}?"
                    ]
                elif column == "english":
                    custom_questions = [
                        f"Is {game_name} available in English?",
                        f"Can I play {game_name} in English?",
                        f"Is {game_name} in English"
                    ]
                elif column == "developer":
                    custom_questions = [
                        f"Who developed {game_name}?",
                        f"What studio was responsible for creating {game_name}?",
                        f"Which developers worked on {game_name}?",
                        f"Who is the developer of {game_name}"
                    ]
                elif column == "publisher":
                    custom_questions = [
                        f"Who published {game_name}?",
                        f"What company released {game_name}?",
                        f"Which publishers were involved with {game_name}?",
                        f"Who is the publisher of {game_name}"
                    ]
                elif column == "platforms":
                    custom_questions = [
                        f"On which platforms can I play {game_name}?",
                        f"Is {game_name} available on PC?",
                        f"Can I play {game_name} on console?",
                        f"What are the platforms for {game_name}"
                    ]
                elif column == "required_age":
                    custom_questions = [
                        f"What is the age requirement for {game_name}?",
                        f"Is {game_name} suitable for all ages?",
                        f"Play of what age can play {game_name}"
                    ]
                elif column == "categories":
                    custom_questions = [
                        f"What type of game is {game_name}?",
                        f"What categories does {game_name} belong to?",
                        f"Is {game_name} a multiplayer game?",
                        f"What are the categories of {game_name}"
                    ]
                elif column == "genres":
                    custom_questions = [
                        f"What genre is {game_name}?",
                        f"Is {game_name} an RPG?",
                        f"Does {game_name} fall under the action genre?",
                        f"Does {game_name} belong to _ genre",
                        f"What the genre of {game_name}"
                    ]
                elif column == "steamspy_tags":
                    custom_questions = [
                        f"What are the popular tags for {game_name}?",
                        f"What SteamSpy tags are associated with {game_name}?",
                        f"What are the tags of {game_name}"
                    ]
                elif column == "positive_ratings":
                    custom_questions = [
                        f"How many positive ratings does {game_name} have?",
                        f"What is the positive feedback count for {game_name}?",
                        f"What are the positive rating of {game_name}"
                    ]
                elif column == "negative_ratings":
                    custom_questions = [
                        f"How many negative ratings does {game_name} have?",
                        f"What is the negative feedback count for {game_name}?",
                        f"What are the negative rating of {game_name}"
                    ]
                elif column == "average_playtime":
                    custom_questions = [
                        f"What is the average playtime for {game_name}?",
                        f"How long do people typically play {game_name}?"
                    ]
                elif column == "median_playtime":
                    custom_questions = [
                        f"What is the median playtime for {game_name}?",
                        f"How long do most people spend playing {game_name}?"
                    ]
                elif column == "owners":
                    custom_questions = [
                        f"How many people own {game_name}?",
                        f"What is the ownership range for {game_name}?"
                    ]
                elif column == "price":
                    custom_questions = [
                        f"How much does {game_name} cost?",
                        f"What is the price of {game_name}?",
                        f"Is {game_name} free or paid?",
                        f"What is the cost for {game_name}"
                    ]
                elif column == "detailed_description":
                    custom_questions = [
                        f"Can you give a detailed description of {game_name}?",
                        f"What are the detailed features of {game_name}?",
                        f"Explain {game_name} in detail"
                    ]
                elif column == "about_the_game":
                    custom_questions = [
                        f"What is {game_name} about?",
                        f"Give me a summary of {game_name}.",
                        f"Tell me about {game_name}"
                    ]
                elif column == "short_description":
                    custom_questions = [
                        f"What is the short description of {game_name}?",
                        f"Give me a brief overview of {game_name}.",
                        f"Provide shot description of {game_name}"
                    ]
                elif column == "pc_requirements":
                    custom_questions = [
                        f"What are the PC requirements for {game_name}?",
                        f"Can you list the system needs for running {game_name} on a PC?",
                        f"What spec do I need to run {game_name} on PC?"
                    ]
                elif column == "mac_requirements":
                    custom_questions = [
                        f"What are the Mac requirements to play {game_name}?",
                        f"What specs do I need on my Mac to play {game_name}?",
                        f"Can you list the system needs for running {game_name} on mac?"
                    ]
                elif column == "linux_requirements":
                    custom_questions = [
                        f"How can I run {game_name} on a Linux system?",
                        f"What does it take to play {game_name} on Linux?",
                        f"What specs do I need on my linux to play {game_name}?",
                        f"Can you list the system needs for running {game_name} on linux?"
                    ]
                elif column == "minimum_requirements":
                    custom_questions = [
                        f"What are the minimum system specifications for {game_name}?",
                        f"What's the least powerful setup I could play {game_name} on?",
                        f"What are the least spec I need for {game_name}"
                    ]
                elif column == "recommended_requirements":
                    custom_questions = [
                        f"What are the recommended specifications for the best experience of {game_name}?",
                        f"What system setup do you recommend for playing {game_name}?"
                    ]
                elif column == "release_year":
                    custom_questions = [
                        f"When was {game_name} released?",
                        f"In what year did {game_name} come out?"
                    ]

                noMatchResponses = [
                    f"Unfortunately, I don't have any information about {tag} on {game_name}."
                ]
                patterns.extend(custom_questions)

                # Custom Responses
                if column == 'english':
                    response = 'Yes The Game is in English' if row[column] == 1 else 'No, the game is not in English'
                else:
                    response = f"You asked about {tag.lower()} in {game_name}. Here's what I found: {row[column]}" if row[
                    column] or row[column] == [] else noMatchResponses

                intent = {"tag": game_name+"_"+column, "patterns": patterns, "responses": [response]}
                intents["intents"].append(intent)

            row_counter += 1




            if row_counter  % 100 == 0:
                print(f"Written Rows {row_counter}")
                # Write intents to JSON file
                write_intents_to_json(intents, output_file)
                del intents  # Delete the intents dictionary to free up memory
                gc.collect()  # Trigger garbage collection to release memory
                intents = {"intents": []}  # Reset intents for the next batch



def write_intents_to_json(intents, output_file):
    with open(output_file, 'a') as outfile:
        json.dump(intents, outfile, indent=4)
        outfile.write('\n')  # Add a newline after each JSON object

# Example usage:
generate_intents('test_data.csv', 'intents_1.json')

