import heapq
import re
from collections import defaultdict

# Read the chat log file and extract the messages sent by each user
chat_log_file = 'chat_log.txt'
user_messages = defaultdict(list)
with open(chat_log_file, 'r') as f:
    for line in f:
        # Extract the username and message text from each line
        match = re.match(r'(\w+)\s*:\s*(.*)', line)
        if match:
            username, message = match.groups()
            # Split the message text into words and add them to the user's message list
            words = message.split()
            user_messages[username].extend(words)

# Count the number of words in each user's messages
user_word_counts = {}
for username, messages in user_messages.items():
    word_count = len(messages)
    user_word_counts[username] = word_count

# Find the top K chatty users using a heap
K = 5  # Replace with desired value
top_users = heapq.nlargest(K, user_word_counts.items(), key=lambda x: x[1])

# Print the top K chatty users and their word counts
for user, count in top_users:
    print(f'{user}: {count} words')
