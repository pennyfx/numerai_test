from flask import Flask, request, jsonify

def add(params):
    return params['a'] + params['b']

functions_list = [add]

app = Flask(__name__)

@app.route('/<func_name>', methods=['POST'])
def api_root(func_name):
    for function in functions_list:
        try:
            json_req_data = request.get_json()
            print json_req_data, "check"
            if json_req_data:
                res = function(json_req_data)
        except Exception as e:
            return jsonify({"error": "Something is wrong"+str(e)})
        return jsonify({"result": res})
    output_string = 'function: %s not found' % func_name
    return jsonify({"error": output_string})


if __name__ == '__main__':
    app.run(host='0.0.0.0')