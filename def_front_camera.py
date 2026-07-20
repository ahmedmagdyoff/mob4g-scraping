from bs4 import BeautifulSoup

front_camera_main = []
number_of_front_cameras = []
front_camera_resolution = []
front_camera_lens_slot = []
other_in_front_camera = []
front_camera_video_shooting = []
front_flash = []


# تصفية محتوى الكاميرا الخلفية
def front_camera(p_s_value):

    # جلب محتوى الكاميرا الخلفية
    product_front_camera = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_front_camera_main = ""
    product_number_of_front_cameras = ""
    product_front_camera_resolution = ""
    product_front_camera_lens_slot = ""
    product_other_in_front_camera = ""
    product_front_camera_video_shooting = ""
    product_front_flash = "لا يدعم"

    # تصفية محتوى الكاميرا الخلفية
    for p_f_c_s in product_front_camera:

        # مكان العنوان
        p_f_c_s_title = p_f_c_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_f_c_s_value = p_f_c_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الكاميرا الخلفية
        if p_f_c_s_title == "عدد الكاميرات":
            if ":" in p_f_c_s_value:
                p_f_c_s_value = p_f_c_s_value.split(":")
                product_number_of_front_cameras = p_f_c_s_value[1]
            else:
                product_number_of_front_cameras = p_f_c_s_value
        if p_f_c_s_title == "-":
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
                p_f_c_s_value != "لا تدعم"
                and p_f_c_s_value != "لا يدعم"
                and p_f_c_s_value != "تدعم"
                and p_f_c_s_value != "يدعم"
            ):
                product_front_camera_resolution += "\n" + p_f_c_s_value
                for a_b_c_d_e_f in abcdef:
                    if a_b_c_d_e_f in product_front_camera_resolution:
                        p_f_c_r_split = product_front_camera_resolution.split(
                            a_b_c_d_e_f
                        )
                        product_front_camera_resolution = p_f_c_r_split[1]
        if p_f_c_s_title == "دقة الكاميرا":
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
                p_f_c_s_value != "لا تدعم"
                and p_f_c_s_value != "لا يدعم"
                and p_f_c_s_value != "تدعم"
                and p_f_c_s_value != "يدعم"
            ):
                product_front_camera_resolution += "\n" + p_f_c_s_value
                for a_b_c_d_e_f in abcdef:
                    if a_b_c_d_e_f in product_front_camera_resolution:
                        p_f_c_r_split = product_front_camera_resolution.split(
                            a_b_c_d_e_f
                        )
                        product_front_camera_resolution = p_f_c_r_split[1]
        if p_f_c_s_title == "حجم فتحة العدسة":
            product_front_camera_lens_slot = p_f_c_s_value
        if p_f_c_s_title == "مميزات الكاميرا":
            product_other_in_front_camera = p_f_c_s_value
        if p_f_c_s_title == "الفيديو":
            product_front_camera_video_shooting = p_f_c_s_value
        if p_f_c_s_title == "فلاش":
            if "لا تدعم" not in p_f_c_s_value and "لا يدعم" not in p_f_c_s_value:
                product_front_flash = "يدعم"

    if product_number_of_front_cameras == "":
        if "\n" in product_front_camera_resolution:
            p_f_c_r_split = product_front_camera_resolution.split("\n")
            product_front_camera_main = p_f_c_r_split[0]
        else:
            product_front_camera_main = product_front_camera_resolution
    else:
        product_front_camera_main = product_number_of_front_cameras

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

    emptying(product_front_camera_main, front_camera_main)
    emptying(product_number_of_front_cameras, number_of_front_cameras)
    emptying(product_front_camera_resolution, front_camera_resolution)
    emptying(product_front_camera_lens_slot, front_camera_lens_slot)
    emptying(product_other_in_front_camera, other_in_front_camera)
    emptying(product_front_camera_video_shooting, front_camera_video_shooting)
    front_flash.append(product_front_flash)
