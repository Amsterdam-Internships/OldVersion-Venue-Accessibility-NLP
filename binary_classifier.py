def rule_based_classification(text):
    
    query_terms = ["wheelchair", "disability", "disabled", "handicap", "handicapped", "mobility",
               "entrance", "door",
               "toilet", "bathroom", "restroom",
               "parking",
               "elevator", "ramp", "steps", "stair",
               "cramped", "steep", "spacious", "narrow",
               "service", "staff", "waiter", "waitress"]
    
    # Includes query terms:
    # stairs, staircase, downstairs, upstairs, rampage
    
    
    if any(word in text for word in query_terms):
        bin_class = 1
    else:
        bin_class = 0

    return bin_class

#def rule_based_classification_sent(text):
#    
#    query_terms = ["wheelchair", "disability", "disabled", "handicap", "handicapped", "mobility",
#               "entrance", "door",
#               "toilet", "bathroom", "restroom",
#               "parking",
#               "elevator", "ramp", "steps", "stair",
#               "cramped", "steep", "spacious", "narrow",
#               "service", "staff", "waiter", "waitress"]
#    
#    class_list = []
#    
#    for sentence in text:
#        if any(word in sentence for word in query_terms):
#            class_list.append(1)
#        else:
#            class_list.append(0)
#        
#    return class_list

#def sentence_split(data):
#    '''Iterates over df sentences in review
#    Returns a new df with reviews separated per sentence and corresponding class.'''
#    
#    data_sentences = pd.DataFrame()
#    
#    for i in data.index:
#        ind = i                        # Index
#        name = data.iloc[i][1]         # Name 1
#        date = data.iloc[i][2]         # Date 2
#        sentiment = data.iloc[i][4]    # Rating sentiment 4
#        sentences = data.iloc[i][7]    # Sentences list 7
#        classes = data.iloc[i][9]      # Classes list 9
#        
#        for s in range(len(sentences)):
#            data_sentences = data_sentences.append(
#                            {'DataIndex': i,
#                            'Name': name,
#                            'Date': date,
#                            'RatingSentiment': sentiment,
#                            'Sentence': sentences[s],
#                            'Class': classes[s]}, ignore_index=True)
#    
#    return data_sentences

def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in the list- listOfElements.'''
    
    index_pos_list = []
    index_pos = 0
    
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
            
        except ValueError as e:
            break
            
    return index_pos_list

def count_sentences(text):
    '''Count the number of sentences in the data set.'''
    
    sentence_count = 0
    
    for row in text:
        for sentence in row:
            sentence_count += 1
    
    return sentence_count