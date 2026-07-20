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

# تسهيل تغيير رابط الصفحة
brand_name = "samsung"
page_number = 1

# جلب محتوى الصفحة
soup = BeautifulSoup(
    requests.get("https://mob4g.com/specs/samsung-galaxy-s24-ultra").content, "lxml"
)

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
categories(brand_name, post_category, product_category)

# تعديل النوع
if product_category == "هواتف":
    product_type = "هاتف"
if product_category == "تابلت":
    product_type = "تابلت"
if product_category == "ساعات":
    product_type = "ساعة"
if product_category == "هواتف قابلة للطي":
    product_type = "هاتف قابل للطي"

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
