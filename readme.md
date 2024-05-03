# Anki Deck Automation Script

A Python script which automates the process of populating Anki decks using data from Google Sheets and packaging the contents into an apkg file.

### What is Anki?

Anki is a free and open-source flashcard program. It uses techniques from cognitive science such as active recall testing and spaced repetition to aid the user in memorisation. The name comes from the Japanese word for "memorisation"

### Why you may like this Script

You may find this script useful if you are creating your own flashcards using Google Sheets. This script is especially useful as it automates much of the deck creation process. With it, you can focus solely on adding cards to your deck and training your memory, without worrying about the technicalities of creating Anki decks manually.

## Installation

Make sure that Python 3 is installed on your machine 
```bash
C:\> python -V
```

Install the Requirements text file

```bash
pip install -r requirements. txt 
```

## Connecting to your spreadsheet
Get set up with Google Cloud Services
https://developers.google.com/sheets/api/quickstart/python
Authenticate using the service account credentials
https://developers.google.com/workspace/guides/create-credentials#service-account

You can use the Authentication type of your choice but you will need to make the amendments necessary as indicated by Google documentation.

Copy and paste your Google Sheets ID
```
# Open the Google Sheets document by its ID
sheet_id = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
sheet = client.open_by_key(sheet_id)
```



## Usage
To personalise the format of your ANKI flashcards you will need to make changes to the model. You can find out more on how to personalise this here: https://github.com/kerrickstaley/genanki

Here is an example of an ANKI that is translating from BR-PT to Japanese 

```
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
```
You will also need to make sure that the fields you have changed in the model are amended here.
```
for row in data[1:]:  # Exclude header row
        print("Row from Google Sheets:", row)  # Print the row to console log
        id, word, reading, furigana, meaning, example, translation = row
        note = genanki.Note(
            model=model,
            fields=[id, word, reading, furigana, meaning, example, translation]
        )
        deck.add_note(note)

    # Save the Anki deck as an .apkg file
    genanki.Package(deck).write_to_file('PTBR_to_JP.apkg')
```

## Contributions
This script may not be actively maintained in the future so of course make changes and share updated versions as needed.

## License
Distributed under the MIT License. See LICENSE.txt for more information.


