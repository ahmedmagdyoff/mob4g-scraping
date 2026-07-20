from bs4 import BeautifulSoup

# قوائم بيانات نظام التشغيل
number_of_speakers = []
mm35_port = []
fm_radio = []
other_in_sound = []


# تصفية محتوى الصوتيات
def sound(p_s_value):

    # جلب محتوى الصوتيات
    product_sound = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_number_of_speakers = ""
    product_mm35_port = "لا يدعم"
    product_fm_radio = "لا يدعم"
    product_other_in_sound = ""

    # تصفية محتوى الصوتيات
    for p_s_s in product_sound:

        # مكان العنوان
        p_s_s_title = p_s_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_s_s_value = p_s_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الصوتيات
        if p_s_s_title == "السماعات الخارجية":
            product_number_of_speakers = p_s_s_value
        if p_s_s_title == "منفذ 3.5mm":
            if "لا تدعم" not in p_s_s_value and "لا يدعم" not in p_s_s_value:
                product_mm35_port = "يدعم"
        if p_s_s_title == "راديو FM":
            if "لا تدعم" not in p_s_s_value and "لا يدعم" not in p_s_s_value:
                product_fm_radio = "يدعم"
        if p_s_s_title == "-":
            if (
                product_number_of_speakers == ""
                and "سماعات" in p_s_s_value
                and "عالي الدقة" not in p_s_s_value
            ):
                product_number_of_speakers = p_s_s_value
            else:
                product_other_in_sound = p_s_s_value

    if product_number_of_speakers.strip() == "تدعم":
        product_number_of_speakers = "يدعم"
    elif product_number_of_speakers.strip() == "لا تدعم":
        product_number_of_speakers = "لا يدعم"

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

    emptying(product_number_of_speakers, number_of_speakers)
    mm35_port.append(product_mm35_port)
    fm_radio.append(product_fm_radio)
    emptying(product_other_in_sound, other_in_sound)
