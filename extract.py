from pdfminer.high_level import extract_text

DOCUMENT = 'otpow.pdf'


def get_longest_tweet(index_start, sentence_list):
    tweet = None
    cutoff = len(sentence_list)
    while cutoff > index_start:
        segment = ". ".join(sentence_list[index_start:cutoff])
        if len(segment) > 280:
            cutoff = cutoff - 1
        else:
            tweet = segment
            break
    return tweet


def extract_tweets(min_tweet_length, pdf):
    text = extract_text(pdf)
    tweets = []
    lines = text.splitlines()
    for line in lines:
        sentence_list = line.split(".")
        for i in range(len(sentence_list)):
            tweet = get_longest_tweet(i, sentence_list)
            if tweet and len(tweet) > min_tweet_length:
                tweets.append(tweet)
    return tweets


tweets = extract_tweets(
    min_tweet_length=80,
    pdf=DOCUMENT
)

with open('tweets.txt', 'w') as file:
    for tweet in tweets:
        file.write(tweet)
        file.write('\n')