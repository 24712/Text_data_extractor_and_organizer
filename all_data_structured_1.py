import os
import re

# دالة الترتيب الطبيعي للملفات (1, 2, 3...)
def natural_keys(text):
    return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text)]

output_file = "_all_.txt"
account_number = 1

# جلب الملفات وترتيبها
all_files = [f for f in os.listdir(".") if f.endswith(".txt") and f != output_file]
all_files.sort(key=natural_keys)

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in all_files:
        with open(filename, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
            
            if lines:
                # كتابة رقم الحساب في سطر لوحده
                outfile.write(f"{account_number}\n")
                
                for line in lines:
                    if ":" in line:
                        # فصل العنوان عن القيمة
                        parts = line.split(":", 1)
                        header = parts[0].strip() + ":"
                        value = parts[1].strip()
                        
                        # كتابة العنوان في سطر والقيمة في سطر
                        outfile.write(f"{header}\n")
                        outfile.write(f"{value}\n")
                
                # إضافة الفاصل وزيادة العداد
                outfile.write("_____________________________________________\n")
                account_number += 1

print(f"تم تجميع البيانات بنجاح! الإجمالي: {account_number - 1} حساب.")
