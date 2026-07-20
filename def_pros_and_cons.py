from bs4 import BeautifulSoup

pros = []
cons = []
post_excerpt = []
line_split = "\n\n"


# تصفية محتوى مميزات و عيوب
def pros_and_cons(soup, pros, cons):

    product_pros_and_cons = (
        soup.find("div", {"id": "aps-specs"})
        .find_all("div", {"class": "aps-column"})[1]
        .contents
    )

    list_pros_and_cons = []
    list_pros = []
    list_cons = []

    cons_h2 = ""
    for p_p_a_c in range(len(product_pros_and_cons)):
        list_pros_and_cons.append(product_pros_and_cons[p_p_a_c])

    for l_p_a_c in list_pros_and_cons:
        l_p_a_c_text = l_p_a_c.text
        if "h2" in str(l_p_a_c):
            cons_h2 += l_p_a_c_text
        else:
            if "عيوب" not in cons_h2:
                if ":" in l_p_a_c_text:
                    l_p_a_c_split = l_p_a_c_text.split(":")
                    l_p_a_c = l_p_a_c_split[1].strip()
                list_pros.append(l_p_a_c)
            else:
                if ":" in l_p_a_c_text:
                    l_p_a_c_split = l_p_a_c_text.split(":")
                    l_p_a_c = l_p_a_c_split[1].strip()
                list_cons.append(l_p_a_c)

    new_line_status = True
    while new_line_status == True:
        try:
            list_pros.remove("\n")
        except:
            new_line_status = False

    new_line_status = True
    while new_line_status == True:
        try:
            list_cons.remove("\n")
        except:
            new_line_status = False

    list_cons_pop_status = []
    list_cons_pop = list_cons[-1]
    try:
        list_cons_pop_split = list_cons_pop.split()
    except:
        list_cons_pop_split = list_cons_pop.text.split()
    for l_c_p_s in list_cons_pop_split:
        if l_c_p_s.isdigit():
            l_c_p_s = True
        else:
            l_c_p_s = False
        list_cons_pop_status.append(l_c_p_s)
    if False not in list_cons_pop_status:
        list_cons.remove(list_cons_pop)

    pros_result = ""
    for l_p in list_pros:
        try:
            pros_result += l_p + line_split
        except:
            pros_result += l_p.text + line_split

    cons_result = ""
    for l_c in list_cons:
        try:
            cons_result += l_c + line_split
        except:
            cons_result += l_c.text + line_split

    pros.append(pros_result.strip())
    cons.append(cons_result.strip())

    p_r = []
    for p_r_split in pros_result.split("\n"):
        p_r.append(len(p_r_split))
    product_excerpt = pros_result.split("\n")[p_r.index(max(p_r))]
    post_excerpt.append(product_excerpt)


# تصفية محتوى مميزات
def def_pros(p_s_value, pros):

    # جلب محتوى مميزات
    product_pros = p_s_value.find_all("tr")

    # تصفية محتوى مميزات
    pros_result = ""
    for p_p in product_pros:

        # مكان القيمة
        p_p_value = p_p.find("td", {"class": "aps-attr-value"}).span.text

        pros_result += p_p_value + line_split

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
        p_c = []
        for p_c_split in product_content.split("\n"):
            p_c.append(len(p_c_split))
        product_excerpt = product_content.split("\n")[p_c.index(max(p_c))]
        post_excerpt.append(product_excerpt)

    emptying(pros_result, pros)


# تصفية محتوى عيوب
def def_cons(p_s_value, cons):

    # جلب محتوى عيوب
    product_cons = p_s_value.find_all("tr")

    # تصفية محتوى عيوب
    cons_result = ""
    for p_c in product_cons:

        # مكان القيمة
        p_c_value = p_c.find("td", {"class": "aps-attr-value"}).span.text

        cons_result += p_c_value + line_split

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

    emptying(cons_result, cons)
