from bs4 import BeautifulSoup

# قوائم بيانات الشبكات والشرائح
networks = []
internet_speed = []
slide_type = []
number_of_slides = []
other_in_networks_and_segments = []


# تصفية محتوى الشبكات والشرائح
def networks_and_slides(p_s_value):

    # جلب محتوى الشبكات والشرائح
    product_networks_and_slides = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_networks = ""
    product_internet_speed = ""
    product_slide_type = ""
    product_number_of_slides = ""
    product_other_in_networks_and_segments = ""

    # تصفية محتوى الشبكات والشرائح
    for p_n_a_s_s in product_networks_and_slides:

        # مكان العنوان
        p_n_a_s_s_title = p_n_a_s_s.find(
            "td", {"class": "aps-attr-title"}
        ).span.strong.text

        # مكان القيمة
        p_n_a_s_s_value = p_n_a_s_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الشبكات والشرائح
        if "2G" in p_n_a_s_s_title:
            if "يدعم" in p_n_a_s_s_value:
                product_networks = "2G"
            elif p_n_a_s_s_value == "تدعم":
                product_networks = "2G"
        if "3G" in p_n_a_s_s_title:
            if "يدعم" in p_n_a_s_s_value:
                product_networks = "3G"
            elif p_n_a_s_s_value == "تدعم":
                product_networks = "3G"
        if "4G" in p_n_a_s_s_title:
            if "يدعم" in p_n_a_s_s_value:
                product_networks = "4G"
            elif p_n_a_s_s_value == "تدعم":
                product_networks = "4G"
        if "5G" in p_n_a_s_s_title:
            if "يدعم" in p_n_a_s_s_value:
                product_networks = "5G"
            elif p_n_a_s_s_value == "تدعم":
                product_networks = "5G"
        if p_n_a_s_s_title == "GPRS":
            if "يدعم" in p_n_a_s_s_value:
                if "<br>" in product_other_in_networks_and_segments:
                    product_other_in_networks_and_segments += "," + "GPRS<br>"
                else:
                    product_other_in_networks_and_segments += "GPRS<br>"
        if p_n_a_s_s_title == "EDGE":
            if "يدعم" in p_n_a_s_s_value:
                if "<br>" in product_other_in_networks_and_segments:
                    product_other_in_networks_and_segments += "," + "EDGE<br>"
                else:
                    product_other_in_networks_and_segments += "EDGE<br>"
        if p_n_a_s_s_title == "سرعة انترنت":
            product_internet_speed = p_n_a_s_s_value
        if p_n_a_s_s_title == "نوع الشريحة":
            product_slide_type_options = ["Micro", "Nano", "eSIM"]
            for p_s_t_o in product_slide_type_options:
                if p_s_t_o in p_n_a_s_s_value:
                    if "<br>" in product_slide_type:
                        if p_s_t_o == "eSIM":
                            product_slide_type += "," + p_s_t_o + "<br>"
                        else:
                            product_slide_type += "," + p_s_t_o + " SIM<br>"
                    else:
                        if p_s_t_o == "eSIM":
                            product_slide_type += p_s_t_o + "<br>"
                        else:
                            product_slide_type += p_s_t_o + " SIM<br>"
        if p_n_a_s_s_title == "الشريحة":
            product_slide_type_options = ["Micro", "Nano", "eSIM"]
            for p_s_t_o in product_slide_type_options:
                if p_s_t_o in p_n_a_s_s_value:
                    if "<br>" in product_slide_type:
                        if p_s_t_o == "eSIM":
                            product_slide_type += "," + p_s_t_o + "<br>"
                        else:
                            product_slide_type += "," + p_s_t_o + " SIM<br>"
                    else:
                        if p_s_t_o == "eSIM":
                            product_slide_type += p_s_t_o + "<br>"
                        else:
                            product_slide_type += p_s_t_o + " SIM<br>"
        if "Micro" in p_n_a_s_s_title:
            if "يدعم" in p_n_a_s_s_value:
                if "<br>" in product_slide_type:
                    product_slide_type += "," + "Micro SIM<br>"
                else:
                    product_slide_type += "Micro SIM<br>"
        if "Nano" in p_n_a_s_s_title:
            if "يدعم" in p_n_a_s_s_value:
                if "<br>" in product_slide_type:
                    product_slide_type += "," + "Nano SIM<br>"
                else:
                    product_slide_type += "Nano SIM<br>"
        if "eSIM" in p_n_a_s_s_title:
            if "يدعم" in p_n_a_s_s_value:
                if "<br>" in product_slide_type:
                    product_slide_type += "," + "eSIM<br>"
                else:
                    product_slide_type += "eSIM<br>"
        if p_n_a_s_s_title == "عدد الشرائح":
            if "شريحة واحدة" in p_n_a_s_s_value:
                product_number_of_slides = "شريحة واحدة"
            if "2 شرائح" in p_n_a_s_s_value:
                product_number_of_slides = "شريحتين"
            if "Hybrid" in p_n_a_s_s_value:
                product_number_of_slides = "شريحتين Hybrid SIM"
            if "MicroSD" in p_n_a_s_s_value:
                product_number_of_slides = "شريحتين + MicroSD"

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

    networks.append(product_networks)
    emptying(product_internet_speed, internet_speed)
    slide_type.append(product_slide_type)
    number_of_slides.append(product_number_of_slides)
    other_in_networks_and_segments.append(
        product_other_in_networks_and_segments.strip()
    )
