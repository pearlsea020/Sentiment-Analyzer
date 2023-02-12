from flask import Flask, redirect, url_for, render_template, request, flash 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

app = Flask(__name__)
app.secret_key = "hello"

# function that returns a dictionary of scores
def dictionary(sentence): 
    #instantiate sentinment object
    sent_obj = SentimentIntensityAnalyzer() 
    
    # dict has 'neg', 'pos', 'neu', and 'compound'
    return sent_obj.polarity_scores(sentence) 

    # if compound is >= 0.05, then it's positive 
    # if compound is <= -0.05, then it's negative
    # else it's neutral

# takes in a compound score and outputs a string of positive, negative, or neutral
def sentiment(score):
    if score >= 0.05:
        return "positive xD"
    elif score <= -0.05:
        return "negative poo poo"
    return "neutral"


#home page
@app.route("/")
def home():
    #use post to get the sentence in the form 
    # if request.method == "POST":
     # get the data that was put into the input box 
        # data = request.form["data"]
        # score = dictionary(data)["compound"]
        # sent = sentiment(score)
        # return render_template("index.html", sent=sent)
    #use modal to show the results 
    return render_template("index.html")

#results page 
# @app.route("/results", methods=["POST"])
# def results():
#     if request.method == "POST": 
#         data = request.form["data"]
#         sentiment = classify(data)
#         return render_template("results.html")
#     else:
#         return render_template("index.html")

#run the app 
if __name__ == "__main__":
    app.run(debug=True)
