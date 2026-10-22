from flask import Flask, render_template, request
app = Flask(__name__)

# ข้อมูลเมนู ราคา และคะแนนเป็นข้อมูลจำลองสำหรับสาธิต ต้องสำรวจจริงก่อนใช้เป็นผลวิจัย
RAW_MENU = [('Khao Krapao Moo', 'ข้าวกะเพราหมู', 'อาหารตามสั่ง', 50, 4, 4), ('Khao Krapao Gai', 'ข้าวกะเพราไก่', 'อาหารตามสั่ง', 45, 4, 4), ('Khao Krapao Nuea', 'ข้าวกะเพราเนื้อ', 'อาหารตามสั่ง', 65, 3, 5), ('Khao Krapao Moo Krob', 'ข้าวกะเพราหมูกรอบ', 'อาหารตามสั่ง', 60, 3, 5), ('Khao Krapao Thale', 'ข้าวกะเพราทะเล', 'อาหารตามสั่ง', 70, 3, 4), ('Khao Krapao Tofu', 'ข้าวกะเพราเต้าหู้', 'อาหารตามสั่ง', 45, 2, 3), ('Khao Pad Moo', 'ข้าวผัดหมู', 'ข้าวจานเดียว', 45, 1, 4), ('Khao Pad Gai', 'ข้าวผัดไก่', 'ข้าวจานเดียว', 45, 1, 4), ('Khao Pad Goong', 'ข้าวผัดกุ้ง', 'ข้าวจานเดียว', 60, 1, 4), ('Khao Pad Poo', 'ข้าวผัดปู', 'ข้าวจานเดียว', 80, 1, 4), ('Khao Pad Naem', 'ข้าวผัดแหนม', 'ข้าวจานเดียว', 50, 1, 4), ('Khao Pad Tom Yum Thale', 'ข้าวผัดต้มยำทะเล', 'ข้าวจานเดียว', 65, 4, 4), ('Khao Khai Jiao', 'ข้าวไข่เจียว', 'เมนูไข่', 35, 1, 3), ('Khao Khai Jiao Moo Sap', 'ข้าวไข่เจียวหมูสับ', 'เมนูไข่', 45, 1, 4), ('Khao Khai Khon', 'ข้าวไข่ข้น', 'เมนูไข่', 50, 1, 3), ('Khao Khai Khon Goong', 'ข้าวไข่ข้นกุ้ง', 'เมนูไข่', 65, 1, 4), ('Khao Moo Krathiam', 'ข้าวหมูกระเทียม', 'อาหารตามสั่ง', 50, 1, 4), ('Khao Gai Krathiam', 'ข้าวไก่กระเทียม', 'อาหารตามสั่ง', 45, 1, 4), ('Khao Moo Thot', 'ข้าวหมูทอด', 'ข้าวจานเดียว', 50, 1, 4), ('Khao Gai Thot', 'ข้าวไก่ทอด', 'ข้าวจานเดียว', 45, 1, 4), ('Khao Moo Daeng', 'ข้าวหมูแดง', 'ข้าวจานเดียว', 55, 1, 4), ('Khao Moo Krob', 'ข้าวหมูกรอบ', 'ข้าวจานเดียว', 60, 1, 5), ('Khao Na Ped', 'ข้าวหน้าเป็ด', 'ข้าวจานเดียว', 70, 1, 4), ('Khao Pad Phrik Kaeng', 'ข้าวผัดพริกแกง', 'อาหารตามสั่ง', 50, 4, 4), ('Khao Pad Khiaw Wan Gai', 'ข้าวผัดเขียวหวานไก่', 'ข้าวจานเดียว', 60, 3, 4), ('Khao Pad Kra Thiam', 'ข้าวผัดกระเทียม', 'ข้าวจานเดียว', 45, 1, 4), ('Khao Pad Nam Prik Pao', 'ข้าวผัดน้ำพริกเผา', 'ข้าวจานเดียว', 55, 3, 4), ('Khao Pad Pla Kem', 'ข้าวผัดปลาเค็ม', 'ข้าวจานเดียว', 50, 1, 4), ('Khao Khluk Kapi', 'ข้าวคลุกกะปิ', 'ข้าวจานเดียว', 60, 2, 5), ('Khao Man Gai', 'ข้าวมันไก่', 'ข้าวจานเดียว', 50, 1, 4), ('Khao Man Gai Tod', 'ข้าวมันไก่ทอด', 'ข้าวจานเดียว', 55, 1, 4), ('Khao Moo Tun', 'ข้าวหมูตุ๋น', 'ข้าวจานเดียว', 60, 1, 4), ('Khao Moo Palo', 'ข้าวหมูพะโล้', 'ข้าวจานเดียว', 55, 1, 4), ('Khao Kai Yang', 'ข้าวไก่ย่าง', 'ข้าวจานเดียว', 55, 1, 4), ('Khao Ok Kai', 'ข้าวอกไก่', 'อาหารสุขภาพ', 60, 1, 4), ('Som Tam Thai', 'ส้มตำไทย', 'ส้มตำและยำ', 50, 4, 4), ('Som Tam Poo Pla Ra', 'ส้มตำปูปลาร้า', 'ส้มตำและยำ', 50, 5, 4), ('Yam Woon Sen', 'ยำวุ้นเส้น', 'ส้มตำและยำ', 60, 4, 4), ('Larb Moo', 'ลาบหมู', 'ส้มตำและยำ', 60, 4, 4), ('Nam Tok Moo', 'น้ำตกหมู', 'ส้มตำและยำ', 65, 4, 4), ('Pad See Ew', 'ผัดซีอิ๊ว', 'ก๋วยเตี๋ยวและเส้น', 50, 1, 4), ('Pad Thai Goong', 'ผัดไทยกุ้ง', 'ก๋วยเตี๋ยวและเส้น', 70, 2, 5), ('Rad Na Moo', 'ราดหน้าหมู', 'ก๋วยเตี๋ยวและเส้น', 55, 1, 4), ('Suki Haeng Moo', 'สุกี้แห้งหมู', 'ก๋วยเตี๋ยวและเส้น', 60, 2, 4), ('Suki Nam Gai', 'สุกี้น้ำไก่', 'ก๋วยเตี๋ยวและเส้น', 60, 1, 4), ('Kuay Tiew Tom Yum Moo', 'ก๋วยเตี๋ยวต้มยำหมู', 'ก๋วยเตี๋ยวและเส้น', 55, 4, 4), ('Khao Soi Gai', 'ข้าวซอยไก่', 'ก๋วยเตี๋ยวและเส้น', 70, 2, 5), ('Tom Kha Gai', 'ต้มข่าไก่', 'แกงและซุป', 70, 1, 4), ('Tom Yum Goong', 'ต้มยำกุ้ง', 'แกงและซุป', 80, 5, 5), ('Green Curry Gai', 'แกงเขียวหวานไก่', 'แกงและซุป', 65, 3, 4)]

MENU = [
    {"id": i + 1, "name_en": row[0], "name": row[1], "category": row[2],
     "price": row[3], "spicy": row[4], "taste": row[5],
     "image": f"{i+1:02d}_food.jpg"}
    for i, row in enumerate(RAW_MENU)
]

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    budget = 60
    mood = "spicy"
    category = "all"
    query = ""
    if request.method == "POST":
        try:
            budget = int(request.form.get("budget", 60))
        except ValueError:
            budget = 60
        mood = request.form.get("mood", "spicy")
        category = request.form.get("category", "all")
        query = request.form.get("query", "").strip().lower()

        candidates = []
        for dish in MENU:
            if category != "all" and dish["category"] != category:
                continue
            if query and query not in dish["name"].lower() and query not in dish["name_en"].lower():
                continue
            # Weighted Scoring Model: งบประมาณ 40%, ความชอบรสชาติ 35%, ความเผ็ด 25%
            budget_score = max(0, 100 - abs(dish["price"] - budget) * 2)
            taste_score = dish["taste"] * 20
            if mood == "spicy":
                spice_score = dish["spicy"] * 20
            elif mood == "mild":
                spice_score = (6 - dish["spicy"]) * 20
            else:
                spice_score = 60
            score = 0.40 * budget_score + 0.35 * taste_score + 0.25 * spice_score
            candidates.append({**dish, "score": round(score, 1)})
        results = sorted(candidates, key=lambda d: d["score"], reverse=True)[:3]
    return render_template("index.html", menu=MENU, results=results,
                           budget=budget, mood=mood, category=category, query=query)

if __name__ == "__main__":
    app.run(debug=True)
