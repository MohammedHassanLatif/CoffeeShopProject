import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from jose import jwt
from werkzeug.datastructures import ImmutableMultiDict
from collections.abc import Mapping

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

def get_error_message(error, default_text):
    '''Returns default error text or custom error message (if applicable)

    Args:
        error: System-generated error message which contains a description message.
        default_text: Default text to be used as an error message if no specific message is given.

    Returns:
        Specific error message or default text (if no specific message is given).
    '''
    try:
        return error.description
    except AttributeError:
        return default_text


def get_all_drinks(recipe_format):
    '''Queries a formatted list of drinks with long or short recipe description

    Args:
        recipe_format: "long" or "short", depending on how detailed the information is needed.

    Returns:
        Formatted instances of Drinks as a list.

    If no drinks could be found, raises a 404 error.
    '''
    all_drinks = Drink.query.order_by(Drink.id).all()

    if recipe_format.lower() == 'short':
        all_drinks_formatted = [drink.short() for drink in all_drinks]
    elif recipe_format.lower() == 'long':
        all_drinks_formatted = [drink.long() for drink in all_drinks]
    else:
        raise ValueError('Bad formatted function call. recipe_format needs to be "short" or "long".')

    if len(all_drinks_formatted) == 0:
        raise ValueError('No drinks found in the database.')

    return all_drinks_formatted


# ROUTES

# TODO implement endpoint GET /drinks

@app.route('/drinks', methods=['GET'])
def drinks():
    """Returns all drinks"""
    try:
        drinks = get_all_drinks('short')
        return jsonify({
            'success': True,
            'drinks': drinks
        })
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

# TODO implement endpoint GET /drinks-detail
@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def drinks_detail(payload):
    """Returns all drinks with Info"""
    try:
        drinks = get_all_drinks('long')
        return jsonify({
            'success': True,
            'drinks': drinks
        })
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })


# TODO implement endpoint POST /drinks
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    """Create new drinks and return to client"""
    try:
        body = request.get_json()
        new_drink = Drink(title=body['title'], recipe=json.dumps(body['recipe']))
        new_drink.insert()
        return jsonify({
            'success': True,
            'drink': [new_drink.long()]
        })
    except (KeyError, TypeError) as e:
        return jsonify({
            'success': False,
            'error': 'Invalid request body. Please provide a valid title and recipe.'
        })


# TODO implement endpoint PATCH /drinks/<id>
@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):
    """Updates an existing drink and returns it to the client"""
    try:
        # Get the body from the request
        body = request.get_json()

        if not body:
            abort(400, {'message': 'Request doesnt have valid JSON body.'})

        # Find the drink to update by ID
        drink_to_update = Drink.query.filter(Drink.id == drink_id).one_or_none()

        if not drink_to_update:
            abort(404, {'message': 'No drink found with the specified ID.'})

        # Check which fields should be updated
        updated_title = body.get('title', None)
        updated_recipe = body.get('recipe', None)

        # Update the drink fields if they are provided
        if updated_title:
            drink_to_update.title = updated_title

        if updated_recipe:
            drink_to_update.recipe = json.dumps(updated_recipe)

        drink_to_update.update()

        return jsonify({
            'success': True,
            'drink': [drink_to_update.long()]
        })
    except (KeyError, TypeError):
        abort(400, {'message': 'Invalid request body. Please provide a valid title or recipe.'})




# TODO implement endpoint DELETE /drinks/<id>
@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    """Deletes a drink with the given ID"""
    try:
        if not drink_id:
            abort(422, {'message': 'Please provide a valid drink ID.'})

        # Find the drink to delete by ID
        drink_to_delete = Drink.query.get(drink_id)

        if not drink_to_delete:
            abort(404, {'message': 'Drink with ID {} not found in the database.'.format(drink_id)})

        drink_to_delete.delete()

        return jsonify({
            'success': True,
            'delete': drink_id
        })
    except Exception as e:
        abort(500, {'message': 'An error occurred while deleting the drink.'})


# Error Handling

# TODO implement error handlers using the @app.errorhandler(error) decorator
@app.errorhandler(422)
def unprocessable(error):
    """Handles unprocessable entity error (422)"""
    return jsonify({
        "success": False,
        "error": 422,
        "message": get_error_message(error, "Unprocessable Entity")
    }), 422

@app.errorhandler(400)
def bad_request(error):
    """Handles bad request error (400)"""
    return jsonify({
        "success": False,
        "error": 400,
        "message": get_error_message(error, "Bad Request")
    }), 400

# TODO implement error handler for 404
@app.errorhandler(404)
def resource_not_found(error):
    """Handles resource not found error (404)"""
    return jsonify({
        "success": False,
        "error": 404,
        "message": get_error_message(error, "Resource Not Found")
    }), 404



# TODO implement error handler for AuthError
@app.errorhandler(AuthError)
def authentication_failed(error):
    """Handles authentication failed error (401)"""
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": get_error_message(error.error, "Authentication Failed")
    }), 401