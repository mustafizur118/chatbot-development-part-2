from flask import request, app, jsonify


@app.route('/personalize', methods=['POST'])
def personalize_response(get_customer_profile=None):
    customer_id = request.json['customer_id']

    customer_profile = get_customer_profile(customer_id)

    personalized_response = f"Hello, {customer_profile['name']}. How can I assist you today?"

    return jsonify({'personalized_response': personalized_response})
