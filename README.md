# Chatbot Dataset Builder
I needed dataset for my new chatbot. So I used other datasets's Q&amp;As and dialogues, prepared and saved them in a custom format <br />
Q&amp;A and Dialogue's format in each row in dataset: <br />
In single answer case: "question", "answer" <br />
In multiple answer case: "question", "answer - answer - answer" <br />

<br /><br />

# TODO

### General
- [x] pylint all files

List of training data for convert into dataset

### ambigqa (https://nlp.cs.washington.edu/ambigqa/)
- [x] Training_data/train_light.json
- [x] Training_data/dev_light.json
- [x] Training_data/nqopen-dev.json
- [x] Training_data/nqopen-test.json
- [x] Training_data/nqopen-train.json
- [x] Training_data/train.json

### Cornell Movie-Dialog Corpus ~ CMDC (https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)
- [x] Training_data/movie_lines.txt

### Ubuntu-dialogue-corpus ~ UDC (https://www.kaggle.com/rtatman/ubuntu-dialogue-corpus)
- [x] Training_data/dialogueText.csv
