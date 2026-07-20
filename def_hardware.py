from bs4 import BeautifulSoup

# قوائم بيانات العتاد
processor = []
manufacturing_precision = []
number_of_cores = []
processor_frequency = []
graphics_processor = []
ram = []
internal_memory = []
storage_memory_type = []
ram_type = []
external_memory = []
antutu_score = []


# تصفية محتوى العتاد
def hardware(p_s_value, product_category):

    # جلب محتوى العتاد
    product_hardware = p_s_value.find_all("tr")

    # تعريف الجوالب
    product_processor = ""
    product_manufacturing_precision = ""
    product_number_of_cores = ""
    product_processor_frequency = ""
    product_graphics_processor = ""
    product_ram = ""
    product_internal_memory = ""
    product_storage_memory_type = ""
    product_ram_type = ""
    product_external_memory = "لا يدعم"
    product_antutu_score = ""

    # تصفية محتوى العتاد
    for p_h_s in product_hardware:

        # مكان العنوان
        p_h_s_title = p_h_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_h_s_value = p_h_s.find("td", {"class": "aps-attr-value"}).span.text

        # تصفية محتوى العتاد
        if p_h_s_title == "اسم المعالج":
            if p_h_s_value != "غير معروف":
                product_processor = p_h_s_value
        if p_h_s_title == "دقة التصنيع":
            product_manufacturing_precision = p_h_s_value
        if p_h_s_title == "عدد الأنوية":
            product_number_of_cores = p_h_s_value
        if p_h_s_title == "تردد المعالج":
            if ":" in p_h_s_value:
                p_h_s_value = p_h_s_value.split(":")
                product_processor_frequency = p_h_s_value[1]
            else:
                product_processor_frequency = p_h_s_value
        if p_h_s_title == "معالج الرسومات":
            if p_h_s_value != "غير معروف":
                product_graphics_processor = p_h_s_value
        if p_h_s_title == "الرام":
            for p_r_o in p_h_s_value.split():
                if p_r_o.isdigit():
                    if "تيرابايت" in p_h_s_value:
                        if int(p_r_o) != 1 and int(p_r_o) != 2:
                            if "ميجابايت" in p_h_s_value and int(p_r_o) > 16:
                                if p_r_o not in product_ram:
                                    product_ram += "," + p_r_o + " ميجابايت<br>"
                            elif int(p_r_o) < 16:
                                if p_r_o not in product_ram:
                                    product_ram += "," + p_r_o + " جيجابايت<br>"
                    else:
                        if "ميجابايت" in p_h_s_value and int(p_r_o) > 16:
                            if p_r_o not in product_ram:
                                product_ram += "," + p_r_o + " ميجابايت<br>"
                        elif int(p_r_o) < 16:
                            if p_r_o not in product_ram:
                                product_ram += "," + p_r_o + " جيجابايت<br>"
            product_ram = product_ram[1:]
        if p_h_s_title == "الذاكرة الداخلية":
            for p_i_m_o in p_h_s_value.split():
                if p_i_m_o.isdigit():
                    if p_i_m_o in ["1", "2"]:
                        product_internal_memory += "," + p_i_m_o + " تيرابايت<br>"
                    else:
                        product_internal_memory += "," + p_i_m_o + " جيجابايت<br>"
            product_internal_memory = product_internal_memory[1:]
        if p_h_s_title == "نوع ذاكرة التخزين":
            product_storage_memory_type = p_h_s_value
        if p_h_s_title == "نوع ذاكرة الرام":
            product_ram_type = p_h_s_value
        if p_h_s_title == "الذاكرة الخارجية":
            if "لا تدعم" not in p_h_s_value and "لا يدعم" not in p_h_s_value:
                product_external_memory = "يدعم"
        if p_h_s_title == "نقاط AnTuTu":
            product_antutu_score = p_h_s_value

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

    emptying(product_processor, processor)
    emptying(product_manufacturing_precision, manufacturing_precision)
    emptying(product_number_of_cores, number_of_cores)
    emptying(product_processor_frequency, processor_frequency)
    emptying(product_graphics_processor, graphics_processor)
    ram.append(product_ram)
    internal_memory.append(product_internal_memory)
    emptying(product_storage_memory_type, storage_memory_type)
    emptying(product_ram_type, ram_type)
    external_memory.append(product_external_memory)
    emptying(product_antutu_score, antutu_score)
