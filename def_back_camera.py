from bs4 import BeautifulSoup

back_camera_main = []
number_of_back_cameras = []
back_camera_resolution = []
back_camera_lens_slot = []
back_camera_sensors = []
other_in_back_camera = []
back_camera_zoom = []
back_camera_stabilizing = []
back_camera_slow_motion = []
back_camera_video_shooting = []
back_flash = []
back_flash_type = []
front_camera_resolution_in_back = []
other_in_front_camera_in_back = []


# تصفية محتوى الكاميرا الخلفية
def back_camera(p_s_value):

    # جلب محتوى الكاميرا الخلفية
    product_back_camera = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_back_camera_main = ""
    product_number_of_back_cameras = ""
    product_back_camera_resolution = ""
    product_back_camera_lens_slot = ""
    product_back_camera_sensors = ""
    product_other_in_back_camera = ""
    product_back_camera_zoom = ""
    product_back_camera_stabilizing = ""
    product_back_camera_slow_motion = ""
    product_back_camera_video_shooting = ""
    product_back_flash = "لا يدعم"
    product_back_flash_type = ""
    product_front_camera_resolution_in_back = ""
    product_other_in_front_camera_in_back = ""

    # تصفية محتوى الكاميرا الخلفية
    for p_b_c_s in product_back_camera:

        # مكان العنوان
        p_b_c_s_title = p_b_c_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_b_c_s_value = p_b_c_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الكاميرا الخلفية
        if p_b_c_s_title == "عدد الكاميرات":
            if ":" in p_b_c_s_value:
                p_b_c_s_value = p_b_c_s_value.split(":")
                product_number_of_back_cameras = p_b_c_s_value[1]
            else:
                product_number_of_back_cameras = p_b_c_s_value
        if p_b_c_s_title == "الكاميرا":
            if (
                "لا تدعم" in p_b_c_s_value
                or "لا يدعم" in p_b_c_s_value
                or "غير موجودة" in p_b_c_s_value
            ):
                product_back_camera_resolution = "لا يدعم"
            else:
                product_back_camera_resolution = p_b_c_s_value
        if p_b_c_s_title == "دقة الكاميرا":
            abcdef = [
                "كاميرا مزدوجة:",
                "كاميرا مزدوجة",
                "كاميرا ثنائية:",
                "كاميرتأن مزدوجة",
                "ثلاث كاميرات:",
                "ثلاث كاميرات",
                "أربع كاميرات:",
                "اربع كاميرات:",
                "أربع كاميرات",
                "اربع كاميرات",
                "خمس كاميرات:",
            ]
            if (
                "لا تدعم" in p_b_c_s_value
                or "لا يدعم" in p_b_c_s_value
                or "غير موجودة" in p_b_c_s_value
            ):
                product_back_camera_resolution = "لا يدعم"
            else:
                product_back_camera_resolution = p_b_c_s_value
                for a_b_c_d_e_f in abcdef:
                    if a_b_c_d_e_f in product_back_camera_resolution:
                        p_b_c_r_split = product_back_camera_resolution.split(
                            a_b_c_d_e_f
                        )
                        product_back_camera_resolution = p_b_c_r_split[1]
        if p_b_c_s_title == "حجم فتحة العدسة":
            product_back_camera_lens_slot = p_b_c_s_value
        if "مستشعر" in p_b_c_s_title:
            product_back_camera_sensors = p_b_c_s_value
        if p_b_c_s_title == "مميزات الكاميرا":
            if (
                p_b_c_s_value != "لا تدعم"
                and p_b_c_s_value != "لا يدعم"
                and p_b_c_s_value != "تدعم"
                and p_b_c_s_value != "يدعم"
            ):
                product_other_in_back_camera += "\n" + p_b_c_s_value
        if p_b_c_s_title == "وظائف أخرى":
            if (
                p_b_c_s_value != "لا تدعم"
                and p_b_c_s_value != "لا يدعم"
                and p_b_c_s_value != "تدعم"
                and p_b_c_s_value != "يدعم"
            ):
                product_other_in_back_camera += "\n" + p_b_c_s_value
        if p_b_c_s_title == "التقريب":
            product_back_camera_zoom = p_b_c_s_value
        if p_b_c_s_title == "التثبيت":
            product_back_camera_stabilizing = p_b_c_s_value
        if p_b_c_s_title == "Slow Motion":
            product_back_camera_slow_motion = p_b_c_s_value
        if p_b_c_s_title == "الفيديو":
            product_back_camera_video_shooting = p_b_c_s_value
        if p_b_c_s_title == "فلاش":
            if "لا تدعم" not in p_b_c_s_value and "لا يدعم" not in p_b_c_s_value:
                product_back_flash = "يدعم"
        if p_b_c_s_title == "نوع الفلاش":
            product_back_flash_type = p_b_c_s_value
        if p_b_c_s_title == "الكاميرا الامامية":
            product_front_camera_resolution_in_back = p_b_c_s_value
        if p_b_c_s_title == "وظائف الكاميرا الأمامية":
            product_other_in_front_camera_in_back = p_b_c_s_value

    if product_number_of_back_cameras == "":
        if "\n" in product_back_camera_resolution:
            p_b_c_r_split = product_back_camera_resolution.split("\n")
            product_back_camera_main = p_b_c_r_split[0]
        else:
            product_back_camera_main = product_back_camera_resolution
    else:
        product_back_camera_main = product_number_of_back_cameras

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

    emptying(product_back_camera_main, back_camera_main)
    emptying(product_number_of_back_cameras, number_of_back_cameras)
    emptying(product_back_camera_resolution, back_camera_resolution)
    emptying(product_back_camera_lens_slot, back_camera_lens_slot)
    emptying(product_back_camera_sensors, back_camera_sensors)
    emptying(product_other_in_back_camera, other_in_back_camera)
    emptying(product_back_camera_zoom, back_camera_zoom)
    emptying(product_back_camera_stabilizing, back_camera_stabilizing)
    emptying(product_back_camera_slow_motion, back_camera_slow_motion)
    emptying(product_back_camera_video_shooting, back_camera_video_shooting)
    back_flash.append(product_back_flash)
    emptying(product_back_flash_type, back_flash_type)
    emptying(product_front_camera_resolution_in_back, front_camera_resolution_in_back)
    emptying(product_other_in_front_camera_in_back, other_in_front_camera_in_back)
