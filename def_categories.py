from bs4 import BeautifulSoup


# تصفية محتوى التصنيفات
def categories(product_author, post_category, product_category):

    split = ","
    phones = "هواتف"
    tablets = "تابلت"
    watches = "ساعات"
    folding_phones = "هواتف قابلة للطي"

    def brand_categories(p_s_v, t_s_v, w_s_v):
        if product_category == phones:
            post_category.append(phones + split + p_s_v)
        elif product_category == tablets:
            post_category.append(tablets + split + t_s_v)
        elif product_category == watches:
            post_category.append(watches + split + w_s_v)
        elif product_category == folding_phones:
            post_category.append(folding_phones + split + p_s_v)

    if product_author == "apple":
        brand_categories("أيفون", "أيباد", "ساعات أبل")
    elif product_author == "asus":
        brand_categories("هواتف أسوس", "", "")
    elif product_author == "infinix":
        brand_categories("هواتف انفينكس", "", "")
    elif product_author == "oppo":
        brand_categories("هواتف اوبو", "اوبو باد", "ساعات اوبو")
    elif product_author == "tecno":
        brand_categories("هواتف تكنو", "", "")
    elif product_author == "google":
        brand_categories("هواتف جوجل", "تابلت جوجل", "ساعات جوجل")
    elif product_author == "realme":
        brand_categories("هواتف ريلمي", "ريلمي باد", "ساعات ريلمي")
    elif product_author == "samsung":
        brand_categories("هواتف سامسونج", "تابلت سامسونج", "ساعات سامسونج")
    elif product_author == "sony":
        brand_categories("هواتف سوني", "تابلت سوني", "ساعات سوني")
    elif product_author == "xiaomi":
        brand_categories("هواتف شاومي", "شاومي باد", "ساعات شاومي")
    elif product_author == "vivo":
        brand_categories("هواتف فيفو", "فيفو باد", "ساعات فيفو")
    elif product_author == "lenovo":
        brand_categories("هواتف لينوفو", "تابلت لينوفو", "")
    elif product_author == "nokia":
        brand_categories("هواتف نوكيا", "تابلت نوكيا", "")
    elif product_author == "huawei":
        brand_categories("هواتف هواوي", "ميت باد", "ساعات هواوي")
    elif product_author == "honor":
        brand_categories("هواتف هونر", "هونر باد", "ساعات هونر")
    else:
        post_category.append("فارغ")
