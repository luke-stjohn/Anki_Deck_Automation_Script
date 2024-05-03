

import random
import genanki
import gspread
from google.oauth2.service_account import Credentials

# Define the scopes for Google Sheets API
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# Load credentials from the service account file
credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)

# Authorise the client
client = gspread.authorize(credentials)

# Open the Google Sheets document by its ID
sheet_id = "1wsXV69WujpA4j98bK9yy7re0WKlFpQwHMj_s2u3utIU"
sheet = client.open_by_key(sheet_id)

#Anki Requires a unique 10 digit ID for its decks and models inorder to keep track
model_id = random.randint(1000000000, 1999999999)
deck_id = random.randint(1000000000, 1999999999)

def create_anki_deck(data):
    # Define Anki model with a one card template
    model = genanki.Model(
        model_id,
        'Single Card Model',
        fields=[
            {'name': 'ID'},
            {'name': 'Word'},
            {'name': 'Reading'},
            {'name': 'Furigana'},
            {'name': 'Meaning'},
            {'name': 'Example'},
            {'name': 'Translation'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Word}} ({{Reading}})<br>{{Furigana}}<br>{{Example}}',
                'afmt': '{{Meaning}}<br>{{Translation}}',
            }
        ]
    )

    # Create a new deck
    deck = genanki.Deck(
        deck_id,
        'PT-BR to JP'
    )

    # Iterate over the Google Sheets Document to create Anki notes
    for row in data[1:]:  # Excludes header row to not create fields as a card
        id, word, reading, furigana, meaning, example, translation = row
        note = genanki.Note(
            model=model,
            fields=[id, word, reading, furigana, meaning, example, translation]
        )
        deck.add_note(note)

    # Save the Anki deck as an .apkg file
    genanki.Package(deck).write_to_file('PTBR_to_JP.apkg')

# View Data from the Google Sheets document in the console
data = sheet.sheet1.get_all_values()
print("Model_ID", model_id)
print("Deck_ID", deck_id)
print("Number of rows retrieved:", len(data)-1)  # Print the number of rows retrieved
print("Fields from Google Sheets:", sheet.sheet1.row_values(1))
for row in data[1:]:  # Print first 5 rows
    print("Data from GoogleSheets", row)

# Create Anki deck
create_anki_deck(data)



