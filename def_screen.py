from bs4 import BeautifulSoup

# قوائم بيانات الشاشة
screen_type = []
screen_size = []
refresh_rate = []
screen_resolution = []
screen_dimensions = []
screen_ratio = []
pixel_density = []
screen_brightness = []
flicker_rate = []
touch_rate = []
screen_protection = []
other_in_screen = []


# تصفية محتوى الشاشة
def screen(p_s_value):

    # جلب محتوى الشاشة
    product_screen = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_screen_type = ""
    product_screen_size = ""
    product_refresh_rate = ""
    product_screen_resolution = ""
    product_screen_dimensions = ""
    product_screen_ratio = ""
    product_pixel_density = ""
    product_screen_brightness = ""
    product_flicker_rate = ""
    product_touch_rate = ""
    product_screen_protection = ""
    product_other_in_screen = ""

    # تصفية محتوى الشاشة
    for p_s_s in product_screen:

        # مكان العنوان
        p_s_s_title = p_s_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_s_s_value = p_s_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الشاشة
        if p_s_s_title == "نوع الشاشة":
            product_screen_type = p_s_s_value
        if p_s_s_title == "حجم الشاشة":
            product_screen_size = p_s_s_value
        if p_s_s_title == "معدل التحديث":
            p_r_r = []
            for p_r_r_split in p_s_s_value.split():
                if p_r_r_split.isdigit():
                    p_r_r.append(p_r_r_split)
            if len(p_r_r) != 0:
                product_refresh_rate = max(p_r_r) + " هرتز"
            else:
                product_refresh_rate = p_s_s_value
        if p_s_s_title == "دقة الشاشة":
            product_screen_resolution = p_s_s_value
        if p_s_s_title == "أبعاد الشاشة":
            product_screen_dimensions = p_s_s_value
        if p_s_s_title == "نسبة الشاشة":
            if "في المئة" not in p_s_s_value:
                product_screen_ratio = p_s_s_value + " في المئة"
            else:
                product_screen_ratio = p_s_s_value
        if p_s_s_title == "كثافة البيكسلات":
            product_pixel_density = p_s_s_value
        if p_s_s_title == "درجة السطوع":
            p_s_b = []
            for p_s_b_split in p_s_s_value.split():
                if p_s_b_split.isdigit():
                    p_s_b.append(p_s_b_split)
            if len(p_s_b) != 0:
                product_screen_brightness = max(p_s_b) + " شمعة"
            else:
                product_screen_brightness = p_s_s_value
        if p_s_s_title == "معدل الوميض":
            product_flicker_rate = p_s_s_value
        if p_s_s_title == "معدل اللمس":
            product_touch_rate = p_s_s_value
        if p_s_s_title == "طبقة حماية":
            product_screen_protection = p_s_s_value
        if p_s_s_title == "الوان الشاشة":
            product_other_in_screen += "\n" + p_s_s_value
        if p_s_s_title == "وظائف أخرى":
            product_other_in_screen += "\n" + p_s_s_value
        if p_s_s_title == "-":
            product_other_in_screen += "\n" + p_s_s_value

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

    emptying(product_screen_type, screen_type)
    emptying(product_screen_size, screen_size)
    emptying(product_refresh_rate, refresh_rate)
    emptying(product_screen_resolution, screen_resolution)
    emptying(product_screen_dimensions, screen_dimensions)
    emptying(product_screen_ratio, screen_ratio)
    emptying(product_pixel_density, pixel_density)
    emptying(product_screen_brightness, screen_brightness)
    flicker_rate.append(product_flicker_rate)
    touch_rate.append(product_touch_rate)
    emptying(product_screen_protection, screen_protection)
    emptying(product_other_in_screen, other_in_screen)
