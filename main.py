from flask import Flask, render_template, jsonify, request
import openaiAPI

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    # 當是POST的時後，就去呼叫Open AI的API，然後把問題送出去
    # 把答案拿回來在送給前端
    if request.method == "POST":
        prompt = request.form["prompt"]
        ai_answer = openaiAPI.get_open_ai_api_chat_response(prompt)
        result = {}
        result["ai_answer"] = ai_answer

        with open("txt.txt", "w", encoding="utf-8") as file:
            file.write(ai_answer)

        return jsonify(result)
    return render_template("home.html", **locals())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
