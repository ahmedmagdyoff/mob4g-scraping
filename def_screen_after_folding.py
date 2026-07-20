from bs4 import BeautifulSoup

# قوائم بيانات الشاشة الخارجية
screen_type_after_folding = []
screen_size_after_folding = []
refresh_rate_after_folding = []
screen_resolution_after_folding = []
screen_dimensions_after_folding = []
pixel_density_after_folding = []
screen_brightness_after_folding = []
flicker_rate_after_folding = []
touch_rate_after_folding = []
screen_protection_after_folding = []
other_in_screen_after_folding = []


# تصفية محتوى الشاشة الخارجية
def screen_after_folding(p_s_value):

    # جلب محتوى الشاشة الخارجية
    product_screen_after_folding = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_screen_type_after_folding = ""
    product_screen_size_after_folding = ""
    product_refresh_rate_after_folding = ""
    product_screen_resolution_after_folding = ""
    product_screen_dimensions_after_folding = ""
    product_pixel_density_after_folding = ""
    product_screen_brightness_after_folding = ""
    product_flicker_rate_after_folding = ""
    product_touch_rate_after_folding = ""
    product_screen_protection_after_folding = ""
    product_other_in_screen_after_folding = ""

    # تصفية محتوى الشاشة الخارجية
    for p_s_a_f_s in product_screen_after_folding:

        # مكان العنوان
        p_s_a_f_s_title = p_s_a_f_s.find(
            "td", {"class": "aps-attr-title"}
        ).span.strong.text

        # مكان القيمة
        p_s_a_f_s_value = p_s_a_f_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الشاشة الخارجية
        if p_s_a_f_s_title == "نوع الشاشة":
            product_screen_type_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "حجم الشاشة":
            product_screen_size_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "معدل التحديث":
            p_r_r_a_f = []
            for p_r_r_a_f_split in p_s_a_f_s_value.split():
                if p_r_r_a_f_split.isdigit():
                    p_r_r_a_f.append(p_r_r_a_f_split)
            if len(p_r_r_a_f) != 0:
                product_refresh_rate_after_folding = max(p_r_r_a_f) + " هرتز"
            else:
                product_refresh_rate_after_folding = p_s_a_f_s_value
            if "144" in p_s_a_f_s_value:
                product_refresh_rate_after_folding = "144 هرتز"
            elif "120" in p_s_a_f_s_value:
                product_refresh_rate_after_folding = "120 هرتز"
            elif "90" in p_s_a_f_s_value:
                product_refresh_rate_after_folding = "90 هرتز"
            elif "60" in p_s_a_f_s_value:
                product_refresh_rate_after_folding = "60 هرتز"
            elif "30" in p_s_a_f_s_value:
                product_refresh_rate_after_folding = "30 هرتز"
            else:
                product_refresh_rate_after_folding = "معدل التحديث"
        if p_s_a_f_s_title == "دقة الشاشة":
            product_screen_resolution_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "أبعاد الشاشة":
            product_screen_dimensions_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "كثافة البيكسلات":
            product_pixel_density_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "درجة السطوع":
            p_s_b_a_f = []
            for p_s_b_a_f_split in p_s_a_f_s_value.split():
                if p_s_b_a_f_split.isdigit():
                    p_s_b_a_f.append(p_s_b_a_f_split)
            if len(p_s_b_a_f) != 0:
                product_screen_brightness_after_folding = max(p_s_b_a_f) + " شمعة"
            else:
                product_screen_brightness_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "معدل الوميض":
            product_flicker_rate_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "معدل اللمس":
            product_touch_rate_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "طبقة حماية":
            product_screen_protection_after_folding = p_s_a_f_s_value
        if p_s_a_f_s_title == "الوان الشاشة":
            product_other_in_screen_after_folding += "\n" + p_s_a_f_s_value
        if p_s_a_f_s_title == "وظائف أخرى":
            product_other_in_screen_after_folding += "\n" + p_s_a_f_s_value
        if p_s_a_f_s_title == "-":
            product_other_in_screen_after_folding += "\n" + p_s_a_f_s_value

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

    emptying(product_screen_type_after_folding, screen_type_after_folding)
    emptying(product_screen_size_after_folding, screen_size_after_folding)
    emptying(product_refresh_rate_after_folding, refresh_rate_after_folding)
    emptying(product_screen_resolution_after_folding, screen_resolution_after_folding)
    emptying(product_screen_dimensions_after_folding, screen_dimensions_after_folding)
    emptying(product_pixel_density_after_folding, pixel_density_after_folding)
    emptying(product_screen_brightness_after_folding, screen_brightness_after_folding)
    flicker_rate_after_folding.append(product_flicker_rate_after_folding)
    touch_rate_after_folding.append(product_touch_rate_after_folding)
    emptying(product_screen_protection_after_folding, screen_protection_after_folding)
    emptying(product_other_in_screen_after_folding, other_in_screen_after_folding)
