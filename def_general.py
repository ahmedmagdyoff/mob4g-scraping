from bs4 import BeautifulSoup
import datetime

# قوائم بيانات عام
market = []
post_date = []
product_date_list = []
colors = []

one_m = [0]
two_m = [0]
three_m = [0]
four_m = [0]
five_m = [0]
six_m = [0]
seven_m = [0]
eight_m = [0]
nine_m = [0]
ten_m = [0]
eleven_m = [0]
twelve_m = [0]

one_h = [0]
two_h = [0]
three_h = [0]
four_h = [0]
five_h = [0]
six_h = [0]
seven_h = [0]
eight_h = [0]
nine_h = [0]
ten_h = [0]
eleven_h = [0]
twelve_h = [0]

one_d = [1]
two_d = [1]
three_d = [1]
four_d = [1]
five_d = [1]
six_d = [1]
seven_d = [1]
eight_d = [1]
nine_d = [1]
ten_d = [1]
eleven_d = [1]
twelve_d = [1]


# تصفية محتوى عام
def general(p_s_value):

    # جلب محتوى عام
    product_general = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_market = ""
    product_date = ""
    year_date = ""
    product_colors = ""

    # تصفية محتوى عام
    for p_g_s in product_general:

        # مكان العنوان
        p_g_s_title = p_g_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_g_s_value = p_g_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى عام
        if p_g_s_title == "الأسواق الموجه اليها":
            product_market = p_g_s_value
        if p_g_s_title == "تاريخ اعلان عن الجهاز":
            product_date = p_g_s_value
        if p_g_s_title == "تاريخ إعلان عن الساعة":
            product_date = p_g_s_value
        if p_g_s_title == "الوان الجهاز":
            product_colors = p_g_s_value
        if p_g_s_title == "الوان الساعة":
            product_colors = p_g_s_value

    # تعديل السوق
    if "عالم" in product_market:
        product_market = "العالمي"
    elif "صين" in product_market:
        product_market = "الصيني"
    elif "هند" in product_market:
        product_market = "الهندي"
    else:
        product_market = "العالمي"

    # تعديل التاريخ
    def dater(year_date, month_date, d, h, m):
        product_date_list.clear()
        product_date = f"{year_date}-{month_date}-{d[0]} {h[0]}:{m[0]}"
        product_date_list.append(product_date)
        m.append(m[0] + 1)
        del m[0]
        if m[0] == 60:
            h.append(h[0] + 1)
            del h[0]
            m.append(0)
            del m[0]
        if h == 24:
            d.append(d[0] + 1)
            del d[0]
            h.append(0)
            del h[0]

    for p_d_s in product_date.split():
        if p_d_s.isdigit():
            year_date = p_d_s

    if "يناير" in product_date:
        dater(year_date, "01", one_d, one_h, one_m)
        product_date = product_date_list[0]
    elif "فبراير" in product_date:
        dater(year_date, "02", two_d, two_h, two_m)
        product_date = product_date_list[0]
    elif "مارس" in product_date:
        dater(year_date, "03", three_d, three_h, three_m)
        product_date = product_date_list[0]
    elif "أبريل" in product_date or "ابريل" in product_date:
        dater(year_date, "04", four_d, four_h, four_m)
        product_date = product_date_list[0]
    elif "مايو" in product_date or "ماي" in product_date:
        dater(year_date, "05", five_d, five_h, five_m)
        product_date = product_date_list[0]
    elif "يونيو" in product_date:
        dater(year_date, "06", six_d, six_h, six_m)
        product_date = product_date_list[0]
    elif "يوليو" in product_date:
        dater(year_date, "07", seven_d, seven_h, seven_m)
        product_date = product_date_list[0]
    elif "اغسطس" in product_date or "أغسطس" in product_date:
        dater(year_date, "08", eight_d, eight_h, eight_m)
        product_date = product_date_list[0]
    elif "سبتمبر" in product_date:
        dater(year_date, "09", nine_d, nine_h, nine_m)
        product_date = product_date_list[0]
    elif "أكتوبر" in product_date or "اكتوبر" in product_date:
        dater(year_date, "10", ten_d, ten_h, ten_m)
        product_date = product_date_list[0]
    elif "نوفمبر" in product_date:
        dater(year_date, "11", eleven_d, eleven_h, eleven_m)
        product_date = product_date_list[0]
    elif "ديسمبر" in product_date:
        dater(year_date, "12", twelve_d, twelve_h, twelve_m)
        product_date = product_date_list[0]

    def emptying(product_content, list_content):
        if "\n" in product_content:
            p_c = ""
            for p_c_split in product_content.split("\n"):
                if "•" in p_c_split:
                    p_c_split = p_c_split[1:]
                if "\r" in p_c_split:
                    p_c_split = p_c_split[:-1]
                p_c += "\n" + p_c_split.strip()
            product_content = p_c.strip()
        if "•" in product_content:
            p_c = ""
            for p_c_split in product_content.split("•"):
                if "•" in p_c_split:
                    p_c_split = p_c_split[1:]
                if "\r" in p_c_split:
                    p_c_split = p_c_split[:-1]
                p_c += "\n" + p_c_split.strip()
            product_content = p_c.strip()
        list_content.append(product_content)

    market.append(product_market)
    post_date.append(product_date)
    emptying(product_colors, colors)
