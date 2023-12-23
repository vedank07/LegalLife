from flask import Flask, request, jsonify
app = Flask(name)

@app.route("/api", methods = ["POST"])
def api():

    ##if request.method == "POST":
    data = request.get_json()
    prompt = data.get("Message", "")
    response = ask(prompt=prompt, id=testConvo)
    print(response)
    response = {"message": prompt, "Response": response}

    return jsonify(response), 201


@app.route("/")
def home():
    return "Home"

if name == "main":
    app.run(debug=True)