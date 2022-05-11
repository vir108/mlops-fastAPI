# Sentiment Analysis HuggingFace 

Use this code to create your own endpoint for sentiment analysis of a sentence using a default model from HF with the help of Fast API

You can get results like these 
Sentiment test: It is a sad news === [{'label': 'NEGATIVE', 'score': 0.9970881342887878}]
INFO:     127.0.0.1:45290 - "POST /performSentimentAnalysis HTTP/1.1" 200 OK
Sentiment test: You reap what you sow === [{'label': 'POSITIVE', 'score': 0.9976106882095337}]
INFO:     127.0.0.1:45292 - "POST /performSentimentAnalysis HTTP/1.1" 200 OK
Sentiment test: night is darkest before dawn === [{'label': 'NEGATIVE', 'score': 0.8983059525489807}]
INFO:     127.0.0.1:45294 - "POST /performSentimentAnalysis HTTP/1.1" 200 OK


