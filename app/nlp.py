from flask import request, jsonify
from nltk import app
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))


def process_query(query):
    # Tokenize query
    tokens = word_tokenize(query)
    # Remove stop words
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    # Perform additional processing as needed
    # For demonstration, let's return the filtered tokens
    return filtered_tokens


@app.route('/process_query', methods=['POST'])
def process_user_query():
    # Retrieve user query from request
    user_query = request.json['query']

    # Process user query using NLP
    processed_query = process_query(user_query)

    return jsonify({'processed_query': processed_query})
