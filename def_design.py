from bs4 import BeautifulSoup

# قوائم بيانات التصميم
height = []
width = []
thickness = []
dimensions = []
dimensions_after_folding = []
weight = []
manufacturing_materials = []


# تصفية محتوى الصتميم
def design(p_s_value):

    # جلب محتوى التصميم
    product_design = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_height = ""
    product_width = ""
    product_thickness = ""
    product_dimensions = ""
    product_dimensions_after_folding = ""
    product_weight = ""
    product_manufacturing_materials = ""

    # تصفية محتوى التصميم
    for p_d_s in product_design:

        # مكان العنوان
        p_d_s_title = p_d_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_d_s_value = p_d_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى الصتميم
        if p_d_s_title == "الطول":
            if "ملليمتر" in p_d_s_value:
                product_height = p_d_s_value[:-7] + "مم"
            else:
                product_height = p_d_s_value
        if p_d_s_title == "العرض":
            if "ملليمتر" in p_d_s_value:
                product_width = p_d_s_value[:-7] + "مم"
            else:
                product_width = p_d_s_value
        if p_d_s_title == "السُمك":
            if "ملليمتر" in p_d_s_value:
                product_thickness = p_d_s_value[:-7] + "مم"
            else:
                product_thickness = p_d_s_value
        if p_d_s_title == "الأبعاد":
            product_dimensions = p_d_s_value
        if p_d_s_title == "الأبعاد بعد طي الجهاز":
            product_dimensions_after_folding = p_d_s_value
        if p_d_s_title == "وزن الجهاز":
            p_d_s = []
            for p_d_s_split in p_d_s_value.split():
                if p_d_s_split.replace(".", "").isdigit():
                    p_d_s.append(p_d_s_split)
            if len(p_d_s) != 0:
                try:
                    if int(max(p_d_s)) < 5:
                        product_weight = max(p_d_s) + " كيلوغرام"
                    else:
                        product_weight = max(p_d_s) + " غرام"
                except:
                    if float(max(p_d_s)) < 5:
                        product_weight = max(p_d_s) + " كيلوغرام"
                    else:
                        product_weight = max(p_d_s) + " غرام"
            else:
                product_weight = p_d_s_value
        if p_d_s_title == "وزن الساعة":
            p_d_s = []
            for p_d_s_split in p_d_s_value.split():
                if p_d_s_split.replace(".", "").isdigit():
                    p_d_s.append(p_d_s_split)
            if len(p_d_s) != 0:
                try:
                    if int(max(p_d_s)) < 5:
                        product_weight = max(p_d_s) + " كيلوغرام"
                    else:
                        product_weight = max(p_d_s) + " غرام"
                except:
                    if float(max(p_d_s)) < 5:
                        product_weight = max(p_d_s) + " كيلوغرام"
                    else:
                        product_weight = max(p_d_s) + " غرام"
            else:
                product_weight = p_d_s_value
        if p_d_s_title == "خامات التصنيع":
            product_manufacturing_materials = p_d_s_value
        if p_d_s_title == "-":
            product_manufacturing_materials = p_d_s_value

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

    emptying(product_height, height)
    emptying(product_width, width)
    emptying(product_thickness, thickness)
    emptying(product_dimensions, dimensions)
    emptying(product_dimensions_after_folding, dimensions_after_folding)
    emptying(product_weight, weight)
    emptying(product_manufacturing_materials, manufacturing_materials)
