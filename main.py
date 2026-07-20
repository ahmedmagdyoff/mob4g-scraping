import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
from def_pros_and_cons import *
from def_general import *
from def_design import *
from def_networks_and_slides import *
from def_screen import *
from def_screen_after_folding import *
from def_hardware import *
from def_software import *
from def_back_camera import *
from def_front_camera import *
from def_sound import *
from def_telecommunications import *
from def_charging_and_battery import *
from def_others import *
from def_seo import *
from def_categories import *

# قوائم البيانات الاساسية
post_title = []
purchase = []
price = []
link = []
featured_image = []
post_author = []
post_category = []
post_type = []
rating = []

log_file = open("log.text", "w")
log_file.close()


# تصفية محتوى عمود مواصفات
def specification():

    global p_s_titles
    p_s_titles = []

    # جلب محتوى عمود المواصفات
    product_specification = (
        soup.find("div", {"id": "aps-specs"})
        .find_all("div", {"class": "aps-column"})[0]
        .find_all("div", {"class": "aps-group"})
    )

    # تصفية محتوى عمود مواصفات
    for p_s in product_specification:

        # مكان العنوان
        p_s_title = p_s.find("h3", {"class": "aps-group-title"}).text.strip()

        # تسجيل العناوين
        p_s_titles.append(p_s_title)

        # مكان القيمة
        p_s_value = p_s.find("table", {"class": "aps-specs-table"}).tbody

        if p_s_title == "مواصفات عامة":
            # تصفية محتوى عام
            general(p_s_value)
            # تصفية محتوى SEO
            seo(soup, p_s_value)
        if p_s_title == "أبعاد وهيكل الجهاز":
            # تصفية محتوى الصتميم
            design(p_s_value)
        if p_s_title == "ابعاد وهيكل الجهاز":
            # تصفية محتوى الصتميم
            design(p_s_value)
        if p_s_title == "الوزن وأبعاد الساعة":
            # تصفية محتوى الصتميم
            design(p_s_value)
        if p_s_title == "الشبكات والشرائح":
            # تصفية محتوى الشبكات والشرائح
            networks_and_slides(p_s_value)
        if p_s_title == "الشريحة والشبكات":
            # تصفية محتوى الشبكات والشرائح
            networks_and_slides(p_s_value)
        if p_s_title == "الشاشة":
            # تصفية محتوى الشاشة
            screen(p_s_value)
        if p_s_title == "الشاشة الخارجية":
            # تصفية محتوى الشاشة الخارجية
            screen_after_folding(p_s_value)
        if p_s_title == "العتاد":
            # تصفية محتوى العتاد
            hardware(p_s_value, product_category)
        if p_s_title == "نظام التشغيل":
            # تصفية محتوى نظام التشغيل
            software(p_s_value)
        if p_s_title == "الكاميرا الخلفية":
            # تصفية محتوى الكاميرا الخلفية
            back_camera(p_s_value)
        if p_s_title == "كاميرا الساعة":
            # تصفية محتوى كاميرا الساعة
            back_camera(p_s_value)
        if p_s_title == "كاميرا السيلفي":
            # تصفية محتوى كاميرا السيلفي
            front_camera(p_s_value)
        if p_s_title == "الصوتيات":
            # تصفية محتوى الصوتيات
            sound(p_s_value)
        if p_s_title == "الإتصالات":
            # تصفية محتوى الإتصالات
            telecommunications(p_s_value)
        if p_s_title == "مواصفات اخرى":
            # تصفية محتوى مواصفات اخرى
            others(p_s_value)
        if p_s_title == "الشحن والبطارية":
            # تصفية محتوى الشحن والبطارية
            charging_and_battery(p_s_value)
        if p_s_title == "عيوب الجهاز":
            # تصفية محتوى عيوب
            def_cons(p_s_value, cons)
        if p_s_title == "عيوب الساعة":
            # تصفية محتوى عيوب
            def_cons(p_s_value, cons)
        if p_s_title == "مُميزات الجهاز":
            # تصفية محتوى مميزات
            def_pros(p_s_value, pros)
        if p_s_title == "مُميزات الساعة":
            # تصفية محتوى مميزات
            def_pros(p_s_value, pros)

    if "مواصفات عامة" not in p_s_titles:
        # سد الفراغ
        market.append("")
        post_date.append("")
        colors.append("")
        # سد الفراغ
        rank_math_focus_keyword.append("")
    if (
        "أبعاد وهيكل الجهاز" not in p_s_titles
        and "ابعاد وهيكل الجهاز" not in p_s_titles
        and "الوزن وأبعاد الساعة" not in p_s_titles
    ):
        # سد الفراغ
        height.append("")
        width.append("")
        thickness.append("")
        dimensions.append("")
        dimensions_after_folding.append("")
        weight.append("")
        manufacturing_materials.append("")
    if "الشبكات والشرائح" not in p_s_titles and "الشريحة والشبكات" not in p_s_titles:
        # سد الفراغ
        networks.append("")
        internet_speed.append("")
        slide_type.append("")
        number_of_slides.append("")
        other_in_networks_and_segments.append("")
    if "الشاشة" not in p_s_titles:
        # سد الفراغ
        screen_type.append("")
        screen_size.append("")
        refresh_rate.append("")
        screen_resolution.append("")
        screen_dimensions.append("")
        screen_ratio.append("")
        pixel_density.append("")
        screen_brightness.append("")
        flicker_rate.append("")
        touch_rate.append("")
        screen_protection.append("")
        other_in_screen.append("")
    if "الشاشة الخارجية" not in p_s_titles:
        # سد الفراغ
        screen_type_after_folding.append("")
        screen_size_after_folding.append("")
        refresh_rate_after_folding.append("")
        screen_resolution_after_folding.append("")
        screen_dimensions_after_folding.append("")
        pixel_density_after_folding.append("")
        screen_brightness_after_folding.append("")
        flicker_rate_after_folding.append("")
        touch_rate_after_folding.append("")
        screen_protection_after_folding.append("")
        other_in_screen_after_folding.append("")
    if "العتاد" not in p_s_titles:
        # سد الفراغ
        processor.append("")
        manufacturing_precision.append("")
        number_of_cores.append("")
        processor_frequency.append("")
        graphics_processor.append("")
        ram.append("")
        internal_memory.append("")
        storage_memory_type.append("")
        ram_type.append("")
        external_memory.append("")
        antutu_score.append("")
    if "نظام التشغيل" not in p_s_titles:
        # سد الفراغ
        operating_system.append("")
        user_interface.append("")
    if "الكاميرا الخلفية" not in p_s_titles and "كاميرا الساعة" not in p_s_titles:
        # سد الفراغ
        back_camera_main.append("")
        number_of_back_cameras.append("")
        back_camera_resolution.append("")
        back_camera_lens_slot.append("")
        back_camera_sensors.append("")
        other_in_back_camera.append("")
        back_camera_zoom.append("")
        back_camera_stabilizing.append("")
        back_camera_slow_motion.append("")
        back_camera_video_shooting.append("")
        back_flash.append("")
        back_flash_type.append("")
        front_camera_resolution_in_back.append("")
        other_in_front_camera_in_back.append("")
    if "كاميرا السيلفي" not in p_s_titles:
        # سد الفراغ
        front_camera_main.append("")
        number_of_front_cameras.append("")
        front_camera_resolution.append("")
        front_camera_lens_slot.append("")
        other_in_front_camera.append("")
        front_camera_video_shooting.append("")
        front_flash.append("")
    if "الصوتيات" not in p_s_titles:
        # سد الفراغ
        number_of_speakers.append("")
        mm35_port.append("")
        fm_radio.append("")
        other_in_sound.append("")
    if "الإتصالات" not in p_s_titles:
        # سد الفراغ
        wifi.append("")
        bluetooth.append("")
        gps.append("")
        nfc.append("")
        ir_blaster.append("")
        usb_port.append("")
    if "مواصفات اخرى" not in p_s_titles:
        # سد الفراغ
        sensors.append("")
        security.append("")
        protection.append("")
        box_contents.append("")
        other_in_other.append("")
    if "الشحن والبطارية" not in p_s_titles:
        # سد الفراغ
        fast_charging.append("")
        battery_charging_duration.append("")
        wireless_charging.append("")
        reverse_wireless_charging.append("")
        battery_capacity.append("")
        battery_type.append("")
        battery_removability.append("")


b_n = "all"
posts = ["0000"]
if b_n != "all":
    posts = ["0000"]
if b_n == "all":
    brand_names = [["all", 1, 161]]
elif b_n == "samsung":
    brand_names = [["samsung", 1, 21]]
elif b_n == "xiaomi":
    brand_names = [["xiaomi", 1, 17]]
elif b_n == "apple":
    brand_names = [["apple", 1, 6]]
elif b_n == "realme":
    brand_names = [["realme", 1, 9]]
elif b_n == "oppo":
    brand_names = [["oppo", 1, 13]]
elif b_n == "vivo":
    brand_names = [["vivo", 1, 12]]
elif b_n == "honor":
    brand_names = [["honor", 1, 8]]
elif b_n == "infinix":
    brand_names = [["infinix", 1, 7]]
elif b_n == "tecno":
    brand_names = [["tecno", 1, 4]]
elif b_n == "huawei":
    brand_names = [["huawei", 1, 18]]
else:
    brand_names = [
        ["samsung", 1, 21],
        ["xiaomi", 1, 16],
        ["apple", 1, 5],
        ["realme", 1, 8],
        ["oppo", 1, 12],
        ["vivo", 1, 12],
        ["honor", 1, 8],
        ["infinix", 1, 7],
        ["tecno", 1, 4],
        ["huawei", 1, 18],
    ]

for b_n in brand_names:

    # تسهيل تغيير رابط الصفحة
    post_conter = 0
    brand_name = b_n[0]
    page_number = b_n[1]
    end_page = b_n[2]

    while page_number <= end_page:

        # جلب محتوى الصفحة
        if brand_name == "all":
            soup = BeautifulSoup(
                requests.get(f"https://mob4g.com/page/{page_number}").content, "lxml"
            )
        elif brand_name in ["smrtphone", "tablet", "smartwach", "folding-phones"]:
            soup = BeautifulSoup(
                requests.get(f"https://mob4g.com/cat/{brand_name}").content, "lxml"
            )
        else:
            soup = BeautifulSoup(
                requests.get(
                    f"https://mob4g.com/brand/{brand_name}/page/{page_number}"
                ).content,
                "lxml",
            )

        page_number += 1

        # جلب عناوين و روابط المنتجات
        product_title = soup.find_all("h2", {"class": "aps-product-title"})

        # جلب اسعار المنتجات
        product_price = soup.find_all("span", {"class": "aps-price-value"})

        # جلب صور المنتجات
        product_image = soup.find_all("div", {"class": "aps-product-thumb"})

        # تصفية الصور
        f_p_i_len = 0
        for f_p_i in product_image:

            if str(f_p_i_len) in posts or "0000" in posts:

                # جلب صورة المنتج
                p_i_height = 300
                p_i_status = False
                while p_i_status == False:
                    try:
                        try:
                            p_i = f_p_i.find("img", {"height": p_i_height}).attrs[
                                "data-lazy-src"
                            ]
                            p_i_status = True
                        except:
                            p_i = f_p_i.find("img", {"height": p_i_height}).attrs["src"]
                            p_i_status = True
                    except:
                        p_i_height += -1
                        p_i_status = False

                # حذف المقاس
                if ".webp" in p_i:
                    p_i = p_i[:-13] + p_i[-5:]
                elif ".jpeg" in p_i:
                    p_i = p_i[:-13] + p_i[-5:]
                elif ".jpg" in p_i:
                    p_i = p_i[:-12] + p_i[-4:]
                elif ".png" in p_i:
                    p_i = p_i[:-12] + p_i[-4:]
                else:
                    p_i = "صيغة صورة غريبة"

                featured_image.append(p_i)

            f_p_i_len += 1

        # تصفية البيانات الخارجية
        for f_p_t in range(len(product_title)):

            if str(f_p_t) in posts or "0000" in posts:

                # جلب عنوان المنتج
                post_title.append(product_title[f_p_t].text)

                # جلب رابط الشراء
                p_t_split = product_title[f_p_t].text.split()
                product_purchase = "https://www.amazon.eg/s?k="
                for p_t_s in p_t_split:
                    product_purchase += p_t_s + "+"
                purchase.append(product_purchase[:-1])

                # جلب سعر المنتج
                p_p = product_price[f_p_t].text
                p_p = p_p[:-2]
                p_p_split = p_p.split(",")
                p_p = ""
                for p_p_s in p_p_split:
                    p_p += p_p_s
                price.append(p_p)

                # جلب رابط المنتج
                link.append(product_title[f_p_t].find("a").attrs["href"])

# الدخول الى كل منتج
featured_image = list(reversed(featured_image))
post_title = list(reversed(post_title))
purchase = list(reversed(purchase))
price = list(reversed(price))
link = list(reversed(link))

l_number = 0
l_counter = 0
page_counter = 0
print(f"Page Number : ({str(end_page)})")
log_file = open("log.text", "a")
log_file.write(f"Page Number : ({str(end_page)})\n")
log_file.close()
for l in link:

    l_counter += 1
    print(f"{l[:-1]} : ({str(l_counter)})")
    log_file = open("log.text", "a")
    log_file.write(f"{l[:-1]} : ({str(l_counter)})\n")
    log_file.close()

        # الدخول
        soup = BeautifulSoup(requests.get(l).content, "lxml")

        # جلب الشركة
        product_author = soup.find("span", {"class": "aps-product-brand"}).a.text
    if product_author == "آبل":
        product_author = "apple"
    elif product_author == "أسوس":
        product_author = "asus"
    elif product_author == "انفينيكس":
        product_author = "infinix"
    elif product_author == "اوبو":
        product_author = "oppo"
    elif product_author == "تكنو":
        product_author = "tecno"
    elif product_author == "جوجل":
        product_author = "google"
    elif product_author == "ريلمي":
        product_author = "realme"
    elif product_author == "سامسونج":
        product_author = "samsung"
    elif product_author == "سوني":
        product_author = "sony"
    elif product_author == "شاومي":
        product_author = "xiaomi"
    elif product_author == "فيفو":
        product_author = "vivo"
    elif product_author == "لينوفو":
        product_author = "lenovo"
    elif product_author == "نوكيا":
        product_author = "nokia"
    elif product_author == "هواوي":
        product_author = "huawei"
    elif product_author == "هونر":
        product_author = "honor"

    post_author.append(product_author)

    # جلب التصنيفات
    product_category = soup.find("span", {"class": "aps-product-cat"}).a.text
    if "هواتف ذكية" in product_category:
        product_category = "هواتف"
    elif "أجهزة لوحية" in product_category:
        product_category = "تابلت"
    elif "ساعات ذكية" in product_category:
        product_category = "ساعات"
    elif "هواتف قابلة للطي" in product_category:
        product_category = "هواتف قابلة للطي"
    categories(product_author, post_category, product_category)

    # تعديل النوع
    product_type = ""
    if product_category == "هواتف":
        product_type = "هاتف"
    if product_category == "تابلت":
        product_type = "تابلت"
    if product_category == "ساعات":
        product_type = "ساعة"
    if product_category == "هواتف قابلة للطي":
        product_type = "هاتف قابل للطي"
    post_type.append(product_type)

    # جلب التقييم
    product_rating = soup.find("span", {"class": "aps-rating-total"}).text
    p_t = str(float(product_rating) / 2)[:3]
    rating.append(p_t)

    # تصفية محتوى عمود مواصفات
    specification()

    pros_and_cons_status = ""
    if (
        "عيوب الجهاز" in p_s_titles
        or "عيوب الساعة" in p_s_titles
        or "مُميزات الساعة" in p_s_titles
        or "مُميزات الجهاز" in p_s_titles
    ):
        pros_and_cons_status = False
    if pros_and_cons_status != False:
        # تصفية محتوى مميزات و عيوب
        pros_and_cons(soup, pros, cons)

    post_conter += 1

    if l_counter - l_number == 24:
        page_counter += 1
        l_number += 24
        if end_page - page_counter != 0:
            print(f"Page Number : ({str(end_page - page_counter)})")
            log_file = open("log.text", "a")
            log_file.write(f"Page Number : ({str(end_page - page_counter)})\n")
            log_file.close()

# ظبط صفوف الملف
file_list = [
    post_title,
    post_excerpt,
    featured_image,
    post_author,
    post_type,
    purchase,
    price,
    rating,
    pros,
    cons,
    market,
    post_date,
    colors,
    height,
    width,
    thickness,
    dimensions,
    dimensions_after_folding,
    weight,
    manufacturing_materials,
    networks,
    internet_speed,
    slide_type,
    number_of_slides,
    other_in_networks_and_segments,
    screen_type,
    screen_size,
    refresh_rate,
    screen_resolution,
    screen_dimensions,
    screen_ratio,
    pixel_density,
    screen_brightness,
    flicker_rate,
    touch_rate,
    screen_protection,
    other_in_screen,
    screen_type_after_folding,
    screen_size_after_folding,
    refresh_rate_after_folding,
    screen_resolution_after_folding,
    screen_dimensions_after_folding,
    pixel_density_after_folding,
    screen_brightness_after_folding,
    flicker_rate_after_folding,
    touch_rate_after_folding,
    screen_protection_after_folding,
    other_in_screen_after_folding,
    processor,
    manufacturing_precision,
    number_of_cores,
    processor_frequency,
    graphics_processor,
    ram,
    internal_memory,
    storage_memory_type,
    ram_type,
    external_memory,
    antutu_score,
    operating_system,
    user_interface,
    back_camera_main,
    number_of_back_cameras,
    back_camera_resolution,
    back_camera_lens_slot,
    back_camera_sensors,
    other_in_back_camera,
    back_camera_zoom,
    back_camera_stabilizing,
    back_camera_slow_motion,
    back_camera_video_shooting,
    back_flash,
    back_flash_type,
    front_camera_resolution_in_back,
    other_in_front_camera_in_back,
    front_camera_main,
    number_of_front_cameras,
    front_camera_resolution,
    front_camera_lens_slot,
    other_in_front_camera,
    front_camera_video_shooting,
    front_flash,
    number_of_speakers,
    mm35_port,
    fm_radio,
    other_in_sound,
    wifi,
    bluetooth,
    gps,
    nfc,
    ir_blaster,
    usb_port,
    fast_charging,
    battery_charging_duration,
    wireless_charging,
    reverse_wireless_charging,
    battery_capacity,
    battery_type,
    battery_removability,
    sensors,
    security,
    protection,
    box_contents,
    other_in_other,
    rank_math_focus_keyword,
    post_category,
]

# قيمة من كل List
exported = zip_longest(*file_list)

# فتح ملف ال CSV
with open(f"{brand_name}.csv", "w", encoding="utf-8") as myfile:
    wr = csv.writer(myfile)
    # عناوين العواميد
    wr.writerow(
        [
            "post_title",
            "post_excerpt",
            "featured_image",
            "post_author",
            "post_type",
            "purchase",
            "price",
            "rating",
            "pros",
            "cons",
            "market",
            "post_date",
            "colors",
            "height",
            "width",
            "thickness",
            "dimensions",
            "dimensions_after_folding",
            "weight",
            "manufacturing_materials",
            "networks",
            "internet_speed",
            "slide_type",
            "number_of_slides",
            "other_in_networks_and_segments",
            "screen_type",
            "screen_size",
            "refresh_rate",
            "screen_resolution",
            "screen_dimensions",
            "screen_ratio",
            "pixel_density",
            "screen_brightness",
            "flicker_rate",
            "touch_rate",
            "screen_protection",
            "other_in_screen",
            "screen_type_after_folding",
            "screen_size_after_folding",
            "refresh_rate_after_folding",
            "screen_resolution_after_folding",
            "screen_dimensions_after_folding",
            "pixel_density_after_folding",
            "screen_brightness_after_folding",
            "flicker_rate_after_folding",
            "touch_rate_after_folding",
            "screen_protection_after_folding",
            "other_in_screen_after_folding",
            "processor",
            "manufacturing_precision",
            "number_of_cores",
            "processor_frequency",
            "graphics_processor",
            "ram",
            "internal_memory",
            "storage_memory_type",
            "ram_type",
            "external_memory",
            "antutu_score",
            "operating_system",
            "user_interface",
            "back_camera_main",
            "number_of_back_cameras",
            "back_camera_resolution",
            "back_camera_lens_slot",
            "back_camera_sensors",
            "other_in_back_camera",
            "back_camera_zoom",
            "back_camera_stabilizing",
            "back_camera_slow_motion",
            "back_camera_video_shooting",
            "back_flash",
            "back_flash_type",
            "front_camera_resolution_in_back",
            "other_in_front_camera_in_back",
            "front_camera_main",
            "number_of_front_cameras",
            "front_camera_resolution",
            "front_camera_lens_slot",
            "other_in_front_camera",
            "front_camera_video_shooting",
            "front_flash",
            "number_of_speakers",
            "mm35_port",
            "fm_radio",
            "other_in_sound",
            "wifi",
            "bluetooth",
            "gps",
            "nfc",
            "ir_blaster",
            "usb_port",
            "fast_charging",
            "battery_charging_duration",
            "wireless_charging",
            "reverse_wireless_charging",
            "battery_capacity",
            "battery_type",
            "battery_removability",
            "sensors",
            "security",
            "protection",
            "box_contents",
            "other_in_other",
            "rank_math_focus_keyword",
            "post_category",
        ]
    )
    # القيم في الصفوف
    wr.writerows(exported)

# النهاية
print(f"{b_n[0].upper()} Pages {end_page} Done")
log_file = open("log.text", "a")
log_file.write(f"{b_n[0].upper()} Pages {end_page} Done")
log_file.close()
