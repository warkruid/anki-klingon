# input filename <language1>-<language2>.csv
# first line <language1>\t<language2>

import os
import getopt
import sys
import genanki
import csv
import random

from os.path import basename

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'i:v', ['input=', 'verbose', 'version=', ])
print('OPTIONS   :', options)

for opt, arg in options:
    if opt in ('-i', '--input'):
        input_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

dictionary_name=(os.path.splitext(input_filename)[0])
[ leftword, rightword ] = dictionary_name.split('-')

SIMPLE_MODEL = genanki.Model(
        1591007984,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
            ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<center><h1>{{Question}}</h1></center>',
                'afmt': '<center><h1>{{Question}}</h1></center><center><hr id="answer"><center><h1>{{Answer}}</h1></center>',
                },
            ])

deck_id=random.randrange(1 << 30, 1 << 31)
deck = genanki.Deck(deck_id, dictionary_name)
with open(input_filename) as csvfile:
    reader = csv.DictReader(csvfile,delimiter='\t')
    for row in reader:
        left_word = row[leftword]
        right_word = row[rightword]
        deck.add_note(genanki.Note(SIMPLE_MODEL,[left_word, right_word]))
my_package = genanki.Package(deck)
my_package.write_to_file('./anki-package/' + dictionary_name + '.apkg')
