"""Global errors python file containing some of the errrors and the appropriate responses
        to ensure non-technical users can get a response that they can easily comprehend"""

from flask import jsonify
from flask import current_app as app


# User inserts wrong url handle
@app.errorhandler(400)
def person_not_in_db(err):
    response = jsonify({'msg':"Check the API documentation for more information on this API's endpoint and how to use the API please"})
    return response, 400

#Problem with the API application
@app.errorhandler(500)
def api_fault(err):
    response = jsonify({'msg': "Sorry our service is experiencing a few issues. But our team are right on it"})
    return response , 500

#User types in the wrong url end point for a given method
@app.errorhandler(404)
def person_not_in_db(err):
    response = jsonify({'msg':"Check the your URL and method and make sure they correspond. For more information, check the API's documentation"})
    return response, 404

#User asks for a method or wrong url end point for a given method
@app.errorhandler(405)
def person_not_in_db(err):
    response = jsonify({'msg': "Please ensure that you have put the right url and that it matches with the appropriate method. For more information, check the API's documentation"})
    return response, 405