qual_words = ["feel","i am","im","makes me","going to","buy","sell"]
positive_words = {"buy": 1,"good": 1,"undervalued":2,"buying":1,"good value":2,"buying now":2,"epic":1,"gains":1,"buy this now":3,"best":2,"hot":1,"thrilled":2,"happy":1}
negative_words = {"sell":1,"overvalued":1,"rip-off":2,"terrible":2,"bad":1,"short":1,"put":1,"suicide":3,"drop":1,"worst":2,"mistake":1,"cooler":1,"caution":1,"afraid":1}
neg_inflection = ["dont","negative","not"]
pos_inflection = ["do","positive"]

def qualify(tweet):
    qualified = False
    for word in qual_words:
        if word in tweet:
            qualified = True
    return qualified

def analysis(word):
#    print(word)
    score = 0
    if word in positive_words:
        score = score + positive_words[word]
#        print(word,positive_words[word])
    if word in negative_words:
        score = score - negative_words[word]
#        print(word,negative_words[word])
#    print("Word Score: ",score)
    return score
    

def total_score(split_tweet):
    sentiment = 0
    prev_word = ""
    for word in split_tweet:
        score = analysis(word)
#        print(score)
        if score != 0:
            if prev_word in pos_inflection:
                score = score + 2
#                print("added 2 to score because of pos inflection, new score is: ", score)
            elif prev_word in neg_inflection:
                score = score - 2
#                print("took 2 score off due to neg inflection, new score is: ",score)
        sentiment = sentiment + score
#        print("current total score: ",sentiment)
        prev_word = word
    print("Overall Score: ",sentiment)
    return sentiment
    
def tweet_splitter(tweet):
    lower = tweet.lower()
    split = lower.split()
    punctuation = [",",".","'"]
    split_words = []
    for word in split:
        for char in punctuation:
            if char in word:
                rebuild = ""
                for letter in word:
                    if letter not in punctuation:
                        rebuild = rebuild + letter
                        word = rebuild
        split_words.append(word)
#        print("appended ", word, " to list")
    return split_words
                
        

#tweet1 = "i AM buying buy buy TLRY it is undervalued, you have to be insane to sell"
#tweet2 = "bu.y buy buy sell"
#tweet3 = "stock is oveRvalued, sell. now"
#
#
#print(tweet_splitter(tweet1))
#print(tweet_splitter(tweet2))
#print(tweet_splitter(tweet3))

#split_tweet = ["dont","buy","this","stock"]
#split_tweet2 = ["this","is","a","positive","buy"]
#split_tweet3 = ["dont","forget","to","buy","good","stocks"]
#split_tweet4 = ["dont","forget","to","buy","good","stocks","not","terrible","ones"]
#print(total_score(split_tweet))
#print(total_score(split_tweet2))
#print(total_score(split_tweet3))
#print(total_score(split_tweet4))