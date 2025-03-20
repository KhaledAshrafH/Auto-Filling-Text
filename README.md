# Auto Filling Text with N-Gram Models

This project is an auto-filling text program implemented in Python using N-gram models. The program suggests the next word based on the input given by the user. It utilizes N-gram models, specifically Trigrams and Bigrams, to generate predictions.

.

## Dataset Information

The project includes both English and Arabic versions in a single GUI program. The datasets used for training the N-gram models are as follows:

**English Dataset:**
- Number of words: 10,000,618
- Number of articles: 14,441
- Number of tokens: 11,468,564

**Arabic Dataset:**
- Number of words: 1,919,107
- Number of articles: 6,499
- Number of tokens: 2,008,268

The dataset included in the repository has been preprocessed and converted into the following files:

- `10_million_words.txt`: English dataset containing 10 million words from 14,441 articles.
- `2_million_arabic_words.txt`: Arabic dataset containing 2 million words from 6,499 articles.

## N-Gram Models

The auto-filling text program utilizes N-gram models to predict the next word based on the input text. Two models are implemented: Trigrams and Bigrams.

### Trigrams Model

The Trigrams model considers three consecutive words in the text and predicts the next word based on the context. The program tokenizes the text, generates all possible trigrams, and counts the frequency of each word that appears after a particular trigram. This information is used to calculate the probabilities of each trigram. The trigrams are sorted based on their probabilities to suggest the most likely next word given a specific input.

### Bigrams Model

The Bigrams model, implemented using the `AutoFillingGeneral` class from the `AutoFillingGeneral` module, considers two consecutive words to predict the next word. The process of generating bigrams and calculating probabilities is similar to the Trigrams model.

## GUI Interface

The project includes a user-friendly GUI implemented using the `tkinter` library. The GUI allows users to interact with the auto-filling text program and provides the following features:

- Input Field: Users can enter their text input.
- Suggestions Display: The program suggests the next words based on the input provided.

## Code Structure

The main code for the auto-filling text program is provided below:

```python
import nltk
import re
from tkinter import *
from PIL import Image, ImageTk
from AutoFillingGeneral import AutoFilling as generalAF  # For Bigrams

# Function to read the dataset from a file
def read_corpus(file_path):
    # Code omitted for brevity

# AutoFilling class for Trigrams model
class AutoFilling:
    # Code omitted for brevity

# --------------------------------The Main---------------------------------------

# Reading the English dataset
corpus = read_corpus('10_million_words.txt')  # Contains 10 million words from 14,441 articles

AutoFillingObj = AutoFilling(corpus)  # Generate Trigrams
AutoFillingObj.tokenize()
AutoFillingObj.generate_trigrams()
AutoFillingObj.calculate_prob()

AutoFillingObjBi = generalAF(corpus, 2)  # Generate Bigrams
AutoFillingObjBi.tokenize()
AutoFillingObjBi.generate_ngrams()
AutoFillingObjBi.calculate_prob()

# Reading the Arabic dataset
corpusAr = read_corpus('2_million_arabic_words.txt')  # Contains 2 million words from 6,499 articles

AutoFillingObjAr = AutoFilling(corpusAr)  # Generate Trigrams
AutoFillingObjAr.tokenize()
AutoFillingObjAr.generate_trigrams()
AutoFillingObjAr.calculate_prob()

AutoFillingObjArBi = generalAF(corpusAr, 2)  # Generate Bigrams
AutoFillingObjArBi.tokenize()
AutoFillingObjArBi.generate_ngrams()
AutoFillingObjArBi.calculate_prob()

# # --------------------------------GUI Code------------------------------------------
# .....
# ... (GUI code omitted for brevity)
```

The code consists of the following main components:

1. Reading the Dataset: The read_corpus function is used to read the dataset from a file. This function preprocesses the text, removes unnecessary characters, and returns the corpus.

2. AutoFilling Class: The AutoFilling class represents the auto-filling text program using the Trigrams model. It tokenizes the text, generates trigrams, and calculates the probabilities of each trigram. The class provides methods for tokenization, trigram generation, and probability calculation.

3. Main Execution: The main section of the code initializes the necessary objects and data structures for both the English and Arabic datasets. It creates instances of the AutoFilling class for both languages and generates trigrams and bigrams. The probabilities are calculated for both models.

4. GUI Code: The GUI code is not shown in the README file for brevity. However, it is implemented using the tkinter library and provides an interface for users to interact with the auto-filling text program. It includes an input field and suggestions display.

## Installation and Usage

To run the auto-filling text program, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/KhaledAshrafH/Auto-Filling-Text.git
   ```

2. Install the required dependencies.
   
3. Run the program:
   ```
   python main.py
   ```

The GUI interface will open, allowing you to enter text and receive auto-fill suggestions based on the selected N-gram model.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Team

This Project was created by a team of three computer science students at Faculty of Computers and Artificial Intelligence Cairo University. The team members are:

- [Khaled Ashraf Hanafy Mahmoud - 20190186](https://github.com/KhaledAshrafH).
- [Samah Moustafa Hussien Mahmoud - 20190248](https://github.com/Samah-20190248).
- [Ayatullah Esam El-din Mohamed - 20190123](https://github.com/oshaesam1).

## Acknowledgment

- This Project is based on Natural Language Processing (NLP) Course at Faculty of Computers and Artificial Intelligence Cairo University. We would like to thank Dr. Hanaa Bayomi Ali for his guidance and support throughout this course.

- The [News Articles Corpus Dataset](https://www.kaggle.com/datasets/sbhatti/news-articles-corpus) used in this project.
  
- The AutoFillingGeneral class for the Bigrams model is imported from the AutoFillingGeneral module.
  
## License

The Project is released under the [MIT License](LICENSE.md).




  
