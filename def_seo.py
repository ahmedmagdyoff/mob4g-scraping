from bs4 import BeautifulSoup

# قوائم بيانات نظام التشغيل
rank_math_focus_keyword = []
focus_keyword = ["", "مواصفات ", "سعر ", "مميزات ", "عيوب "]


# تصفية محتوى SEO
def seo(soup, p_s_value):

    # جلب الاسم English
    product_title = (
        soup.find("div", {"id": "aps-specs"})
        .find_all("div", {"class": "aps-column"})[0]
        .h2.text[8:]
    )
    # جلب الاسم عربي
    product_seo = p_s_value.find_all("tr")

    # تعريف الجوالب
    p_c = ""
    product_name = ""
    product_rank_math_focus_keyword = ""

    # جلب الاسم عربي
    for p_s_s in product_seo:

        # مكان العنوان
        p_s_s_title = p_s_s.find("td", {"class": "aps-attr-title"}).span.strong.text

        # مكان القيمة
        p_s_s_value = p_s_s.find("td", {"class": "aps-attr-value"}).span.text

        # جلب الاسم عربي
        if p_s_s_title == "اسم الجهاز":
            product_name = p_s_s_value

    # تصفية الاسم عربي
    for p_c_split in product_name.split("\n"):
        if "• " in p_c_split:
            p_c_split = p_c_split[2:]
        if "\r" in p_c_split:
            p_c_split = p_c_split[:-1]
        p_c += "\n" + p_c_split
    product_name = p_c.strip()

    # تصفية الاسم عربي
    if len(product_name.split("\n")) > 1:
        product_name = product_name.split("\n")[-1]

    # انشاء SEO English - عربي
    for f_k in focus_keyword:
        product_rank_math_focus_keyword += "," + f_k + product_title.lower()
        product_rank_math_focus_keyword += "," + f_k + product_name.lower()

    rank_math_focus_keyword.append(product_rank_math_focus_keyword[1:])
