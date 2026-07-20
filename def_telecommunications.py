from bs4 import BeautifulSoup

# قوائم بيانات الإتصالات
wifi = []
bluetooth = []
gps = []
nfc = []
ir_blaster = []
usb_port = []


# تصفية محتوى الإتصالات
def telecommunications(p_s_value):

    # جلب محتوى الإتصالات
    product_telecommunications = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_wifi = ""
    product_bluetooth = ""
    product_gps = "لا يدعم"
    product_nfc = "لا يدعم"
    product_ir_blaster = "لا يدعم"
    product_usb_port = ""

    # تصفية محتوى الإتصالات
    for p_t_s in product_telecommunications:

        # مكان العنوان
        p_t_s_title = p_t_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_t_s_value = p_t_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الإتصالات
        if p_t_s_title == "واي فاي Wi-Fi":
            if p_t_s_value == "لا تدعم" or p_t_s_value == "لا يدعم":
                product_wifi = "لا يدعم"
            elif p_t_s_value == "تدعم" or p_t_s_value == "يدعم":
                product_wifi = "يدعم"
            else:
                product_wifi = p_t_s_value
        if p_t_s_title == "البلوتوث":
            if p_t_s_value == "لا تدعم" or p_t_s_value == "لا يدعم":
                product_bluetooth = "لا يدعم"
            elif p_t_s_value == "تدعم" or p_t_s_value == "يدعم":
                product_bluetooth = "يدعم"
            else:
                product_bluetooth = p_t_s_value
        if p_t_s_title == "GPS":
            if "لا تدعم" not in p_t_s_value and "لا يدعم" not in p_t_s_value:
                product_gps = "يدعم"
        if p_t_s_title == "تقنية NFC":
            if "لا تدعم" not in p_t_s_value and "لا يدعم" not in p_t_s_value:
                product_nfc = "يدعم"
        if p_t_s_title == "IR blaster":
            if "لا تدعم" not in p_t_s_value and "لا يدعم" not in p_t_s_value:
                product_ir_blaster = "يدعم"
        if p_t_s_title == "منفذ USB":
            product_usb_port = p_t_s_value

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

    emptying(product_wifi, wifi)
    emptying(product_bluetooth, bluetooth)
    gps.append(product_gps)
    nfc.append(product_nfc)
    ir_blaster.append(product_ir_blaster)
    emptying(product_usb_port, usb_port)
