
# Regex
import re

# NLTK
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Spacy
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

# TextBlob
from textblob import TextBlob

# --------------------------------------------------
# FUNCTIONS

def remove_nan(data, column_name):
    '''Returns data where values in column_name are not empty (NaN).'''
    
    data = data[data[column_name].notna()]
    
    return data


def clean_translation(text):
    '''Returns the (Translated by Google) English text, removes the (Original) text from the text.
       sep specifies what separator to separate the text by.'''
    
    sep = "(Original)"
    
    if sep in text:
        translation, separator, original = text.partition(sep)
        text = translation
    
    text = text.replace("(Translated by Google)", '')
    
    return text

def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"                 # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

#def sent_tok(text):
#    '''Sentence tokenize.
#    Returns list of sentences in review.'''
#    
#    sentences = sent_tokenize(text)
#    
#    return sentences


def clean_string(text):
    '''Remove punctuation and special characters.''' 
    
    text = text.lower()  
    text = text.replace("\n", '')                            # Remove \n
    text = text.replace("(translated by google)", '')        # Remove (translated by google)
    text = re.sub("n’t", ' not', text)                       # Change n't to not
    text = re.sub("'re", ' are', text)                       # Change 're to are
    text = re.sub(r'[^\w\s]', '', text)                      # Remove punctuation
    text = re.sub(" +", " ", text)                           # Remove multiple spaces
    text = re.sub(r"http.*?(?=\s)", "", text)                # Remove URL's
    text = re.sub("'"," ", text)                             # Remove apostrophes
        
    return text

def get_lang_detector(nlp, name):

    return LanguageDetector()

def remove_non_ENG(text):
    
    nlp = spacy.load("en_core_web_sm")
    Language.factory("language_detector", func=get_lang_detector)
    nlp.add_pipe('language_detector', last=True)

    doc = nlp(text)
    lang = doc._.language['language']
    score = doc._.language['score']
    
    if str(lang) == 'en':
        return text


def remove_stopwords(text):
    '''Remove stopwords.'''
    
    stop_words = stopwords.words('english')
    
    filtered_text = ' '.join([word for word in text.split() if word not in (stop_words)])
    
    return filtered_text


def lemmatize_string(text):
    '''Lemmatize words in a list.'''
    
    lemmatizer = WordNetLemmatizer()
    
    lemmatized_sentence = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
       
    return lemmatized_sentence


def word_tok(text):
    '''Word tokenize.
    Returns list of words in review.'''
    
    words = word_tokenize(text)
    
    return words


#def rating_to_sent(text):
#    '''Change Rating to integer score from 1 to 5.'''
#    
#    texts = str(text)
#    text = text.replace("stars", '')
#    text = text.replace("star", '')
#    text = text.replace(" ", '')
#    score = int(text)
#    
#    '''Change score to positive, negative or neutral'''
#    
#    if score > 3:
#        return 'positive'
#    elif score < 3:
#        return 'negative'
#    else:
#         return 'neutral'  
    
    
def abs_date(text):
    '''Change relative date to absolute date'''
    
    text = str(text)
    text = text.replace(" ago", "")
    text = text.replace("years", "year")
    text = text.replace("months", "month")
    text = text.replace("weeks", "week")
    text = text.replace("days", "day")
    text = text.replace("hours", "hour")
    text = text.replace("minutes", "minute")
    
    num, metric = text.split(' ')
    
    if num == 'a' or num =='an':
        num = 1
    
    num = int(num)
    
    if "year" in metric:
        text = 2022 - num
    elif "month" in metric and num > 3:
        text = 2021
    elif "month" in metric and num < 4:
        text = 2022
    elif "day" in metric or "week" in metric or "hour" in metric or "minute" in metric:
        text = 2022
    
    date = int(text)
    
    return date


#def split_train_test(data):
#    '''Split dataset into train and test set.'''
#    
#    shuffled_data = data.sample(frac=1)
#    
#    shape = shuffled_data.shape[0]
#    
#    train_size = round(shape * 0.9)
#   test_size = round(shape * 0.1)
#    
#    train_set = data[:train_size]
#    test_set = data[test_size:]
#    
#    return train_set, test_set

def correct_typos(text):
    
    x = TextBlob(text)
    corrected_text = x.correct()
    
    return corrected_text
    
    