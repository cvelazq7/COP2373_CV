import re

#list of common space words or phrases
spam_keywords = [
    'congratulations','limited time offer','free money','make money','once in a lifetime','guaranteed',
    'giveaway','prize','risk-free','click here','special promotion','apply now','urgent','while supplies last',
    'you have been selected','no cost','no purchase necessary','pre-approved','terms and conditions','offer',
    'message contains','discount','credit card offers','social security number','passwords','no hidden fees',
    'no questions asked','no catch','cancel at any time','you are a winner'
]

#creating a function and variables
def checking_for_spam(message):
    # convert message to lower case to make search case-insensitive
    message_lower = message.lower()

    #list to store matched keywords
    matched_keywords = []

    #spam score
    spam_score = 0

    #Checking phrases/keywords
    for keyword in spam_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', message_lower):
            matched_keywords.append(keyword)
            spam_score += 1

    #likelihood for spam
    if spam_score >= 10:
        spam_likelihood = 'Very likely to be spam'
    elif spam_score >= 5:
        spam_likelihood= 'Moderately likely to be spam'
    else:
        spam_likelihood = 'Unlikely to be spam'

    return spam_score, spam_likelihood, matched_keywords


# creating main function
def main():
    # getting user inputer/message
    message = input(f'Enter your message to check for spam:')

    # assigning variables from message and calling function checking_for_spam(message)
    spam_score, spam_likelihood, matched_keywords = checking_for_spam(message)

    #displaying results
    print(f'\nSpam Score: {spam_score}')
    print(f'\nLikelihood: {spam_likelihood}')
    if matched_keywords:
        print(f'Matched Scam Keywords/Phrases: {','.join(matched_keywords)}')
    else:
        print('No spam keywords/Phrases detected.')

if __name__ == '__main__':
    main()