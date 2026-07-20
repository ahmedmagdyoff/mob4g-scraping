from bs4 import BeautifulSoup

# قوائم بيانات نظام التشغيل
sensors = []
security = []
protection = []
box_contents = []
other_in_other = []


# تصفية محتوى مواصفات اخرى
def others(p_s_value):

    # جلب محتوى مواصفات اخرى
    product_others = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_sensors = ""
    product_security = ""
    product_protection = ""
    product_box_contents = ""
    product_other_in_other = ""

    # تصفية محتوى مواصفات اخرى
    for p_o_s in product_others:

        # مكان العنوان
        p_o_s_title = p_o_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_o_s_value = p_o_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى مواصفات اخرى
        if p_o_s_title == "المستشعرات":
            product_sensors = p_o_s_value
        if p_o_s_title == "انواع الحماية":
            product_security = p_o_s_value
        if "مقاومة" in p_o_s_title:
            if p_o_s_value != "لا يدعم":
                product_protection += p_o_s_value + "\n"
        if p_o_s_title == "-":
            if "مقاوم" in p_o_s_value:
                product_protection += p_o_s_value + "\n"
            else:
                product_other_in_other += p_o_s_value + "\n"
        if p_o_s_title == "القلم":
            product_box_contents = p_o_s_value
        if p_o_s_title == "محتويات علبة الجهاز":
            product_box_contents = p_o_s_value + "\n" + product_box_contents
        if p_o_s_title == "وظائف أخرى":
            product_other_in_other += p_o_s_value + "\n"

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

    emptying(product_sensors, sensors)
    emptying(product_security, security)
    emptying(product_protection, protection)
    emptying(product_box_contents, box_contents)
    emptying(product_other_in_other, other_in_other)
