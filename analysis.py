qual_words = ["feel","i am","i'm","makes me","going to"]
positive_words = {"buy": 1,"good": 1,"undervalued":2,"buying":1,"good value":2,"buying now":2}
negative_words = {"sell":1,"overvalued":1,"rip off":2,"terrible":2,"bad":1}


def qualify(tweet):
    qualified = False
    for word in qual_words:
        if word in tweet:
            qualified = True
    return qualified

def analysis(word):
    print(word)
    score = 0
    if word in positive_words:
        score = score + positive_words[word]
        print(word,positive_words[word])
    if word in negative_words:
        score = score - negative_words[word]
        print(word,negative_words[word])
    print("Word Score: ",score)
    return score
    

def total_score(tweet):
    print(qualify(tweet))
    split = tweet.split()
    sentiment = 0
    for word in split:
        score = analysis(word)
        print(score)
        sentiment = sentiment + score
        print("current total score: ",sentiment)
    print("Overall Score: ",sentiment)
    return sentiment
    
def tweet_splitter(tweet):
    lower = tweet.lower()
    split = lower.split()
    punctuation = [",","."]
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
        print("appended ", word, " to list")
    return split_words
                
        

#tweet1 = "i AM buying buy buy TLRY it is undervalued, you have to be insane to sell"
#tweet2 = "bu.y buy buy sell"
#tweet3 = "stock is oveRvalued, sell. now"
#
#
#print(tweet_splitter(tweet1))
#print(tweet_splitter(tweet2))
#print(tweet_splitter(tweet3))