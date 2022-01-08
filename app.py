import numpy as np;
from flask import Flask, request, jsonify, render_template;
import pickle;

app = Flask (__name__);
#model = pickle.load (open ('model.pkl', 'rb'));

@app.route ('/')
def home ():
    return "Hello Flask"


@app.route ('/pred/<p1>/<p2>', methods=['GET'])
def pred(p1="1", p2="2"):

    name= request.args.get ("user");

    returnObj = {
        "program": "prediction",
        "Params" : {
            "p1" : p1,
            "p2" : p2,
        },
        "user" : name 
    }
    return jsonify (returnObj);

if __name__ == "__main__":
    app.run (debug=True);
