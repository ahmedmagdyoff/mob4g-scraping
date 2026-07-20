from bs4 import BeautifulSoup

# قوائم بيانات نظام التشغيل
fast_charging = []
battery_charging_duration = []
wireless_charging = []
reverse_wireless_charging = []
battery_capacity = []
battery_type = []
battery_removability = []


# تصفية محتوى الشحن والبطارية
def charging_and_battery(p_s_value):

    # جلب محتوى الشحن والبطارية
    product_charging_and_battery = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_fast_charging = "لا يدعم"
    product_battery_charging_duration = ""
    product_wireless_charging = "لا يدعم"
    product_reverse_wireless_charging = "لا يدعم"
    product_battery_capacity = ""
    product_battery_type = ""
    product_battery_removability = ""

    # تصفية محتوى الشحن والبطارية
    for p_c_a_b_s in product_charging_and_battery:

        # مكان العنوان
        p_c_a_b_s_title = p_c_a_b_s.find(
            "td", {"class": "aps-attr-title"}
        ).span.strong.text

        # مكان القيمة
        p_c_a_b_s_value = p_c_a_b_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الشحن والبطارية
        if p_c_a_b_s_title == "الشحن السريع":
            if p_c_a_b_s_value != "لا يدعم":
                if " واط" in p_c_a_b_s_value:
                    for p_c_a_b_o in p_c_a_b_s_value.split():
                        if p_c_a_b_o.replace(".", "").isdigit():
                            product_fast_charging = p_c_a_b_o + " واط"
                else:
                    product_fast_charging = "يدعم"
            else:
                product_fast_charging = "لا يدعم"
        if p_c_a_b_s_title == "مدة شحن البطارية":
            if "يمكن" in p_c_a_b_s_value:
                product_battery_charging_duration = p_c_a_b_s_value[4:]
            else:
                product_battery_charging_duration = p_c_a_b_s_value
        if p_c_a_b_s_title == "الشحن اللاسلكي":
            if p_c_a_b_s_value != "لا يدعم":
                if " واط" in p_c_a_b_s_value:
                    for p_c_a_b_o in p_c_a_b_s_value.split():
                        if p_c_a_b_o.replace(".", "").isdigit():
                            product_wireless_charging = p_c_a_b_o + " واط"
                else:
                    product_wireless_charging = "يدعم"
            else:
                product_wireless_charging = "لا يدعم"
        if p_c_a_b_s_title == "الشحن اللاسلكي العكسي":
            if p_c_a_b_s_value != "لا يدعم":
                if " واط" in p_c_a_b_s_value:
                    for p_c_a_b_o in p_c_a_b_s_value.split():
                        if p_c_a_b_o.replace(".", "").isdigit():
                            product_reverse_wireless_charging = p_c_a_b_o + " واط"
                else:
                    product_reverse_wireless_charging = "يدعم"
            else:
                product_reverse_wireless_charging = "لا يدعم"
        if p_c_a_b_s_title == "سعة البطارية":
            product_battery_capacity = p_c_a_b_s_value
        if p_c_a_b_s_title == "نوع البطارية":
            if "بطارية " in p_c_a_b_s_value:
                product_battery_type = p_c_a_b_s_value[7:]
            else:
                print(p_c_a_b_s_title)
        if p_c_a_b_s_title == "قابلية إزالة":
            product_battery_removability = p_c_a_b_s_value

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

    emptying(product_fast_charging, fast_charging)
    emptying(product_battery_charging_duration, battery_charging_duration)
    emptying(product_wireless_charging, wireless_charging)
    emptying(product_reverse_wireless_charging, reverse_wireless_charging)
    emptying(product_battery_capacity, battery_capacity)
    emptying(product_battery_type, battery_type)
    emptying(product_battery_removability, battery_removability)
