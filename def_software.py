from bs4 import BeautifulSoup

# قوائم بيانات نظام التشغيل
operating_system = []
user_interface = []


# تصفية محتوى نظام التشغيل
def software(p_s_value):

    # جلب محتوى نظام التشغيل
    product_software = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_operating_system = ""
    product_user_interface = ""

    # تصفية محتوى نظام التشغيل
    for p_s_s in product_software:

        # مكان العنوان
        p_s_s_title = p_s_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_s_s_value = p_s_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى نظام التشغيل
        if p_s_s_title == "نظام التشغيل":
            product_operating_system = p_s_s_value
        if p_s_s_title == "واجهة المستخدم":
            product_user_interface = p_s_s_value

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

    emptying(product_operating_system, operating_system)
    emptying(product_user_interface, user_interface)
