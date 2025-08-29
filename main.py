# main.py
# Nanthan S Nair
from flask import Flask, request, jsonify
import os
app = Flask(__name__)
@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        d = request.get_json()
        a = d.get("data", [])
        e = []
        o = []
        x = []
        s = []
        t = 0
        for i in a:
            if i.isdigit():
                if int(i) % 2 == 0:
                    e.append(i)
                else:
                    o.append(i)
                t += int(i)
            elif i.isalpha():
                x.append(i.upper())
            else:
                s.append(i)
        c = "".join(x)[::-1]
        r = ""
        for j, k in enumerate(c):
            r += k.upper() if j % 2 == 0 else k.lower()
        res = {
            "is_success": True,
            "user_id": "nanthan_nair_06012003",
            "email": "nanthansnair4@gmail.com",
            "roll_number": "22BRS1070",
            "odd_numbers": o,
            "even_numbers": e,
            "alphabets": x,
            "special_characters": s,
            "sum": str(t),
            "concat_string": r
        }
        return jsonify(res), 200
    except Exception as f:
        return jsonify({"is_success": False, "error": str(f)}), 400
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)