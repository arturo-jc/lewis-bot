from pdfminer.high_level import extract_text

sample_passage = 'When running the above example, you can stop the program by pressing ctrl+c at the same time. As you can see, these loop constructs serve different purposes. The for loop runs for a fixed amount of times, while the while loop runs until the loop condition changes. In this example, the condition is the boolean True which will never change, so it will run forever.'
sample_sentences = sample_passage.split('.')

def find_longest_tweet(index_start, sentence_list):
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

text = extract_text('sample.pdf')
lines = text.splitlines()
tweets = []
for line in lines:
    sentence_list = line.split(".")
    for i in range(len(sentence_list)):
        tweet = find_longest_tweet(i, sentence_list)
        if (len(tweet) > 0):
            tweets.append(tweet)

with open('tweets.txt', 'w') as file:
    for count, tweet in enumerate(tweets):
        file.write(f'{count}. {tweet}')
        file.write('\n')