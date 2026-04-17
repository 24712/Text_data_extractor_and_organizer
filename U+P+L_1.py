import os
import re

# دالة الترتيب الطبيعي للملفات (1، 2، 10...)
def natural_keys(text):
    return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text)]

# الحقول المطلوب استخراج قيمها فقط
target_fields = ["Username:", "Password:", "Leveled by :"]

# اسم ملف المخرجات كما طلبت
output_file = "U+P+L.txt"
account_number = 1

# جلب الملفات وترتيبها
all_files = [f for f in os.listdir(".") if f.endswith(".txt") and f != output_file]
all_files.sort(key=natural_keys)

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in all_files:
        with open(filename, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
            
            extracted = []
            for field in target_fields:
                for line in lines:
                    if line.strip().startswith(field):
                        value = line.split(field)[1].strip()
                        extracted.append(value)
                        break
            
            # كتابة البيانات في الملف
            if extracted:
                outfile.write(f"{account_number}\n")
                for item in extracted:
                    outfile.write(f"{item}\n")
                outfile.write("_____________________________________________\n")
                account_number += 1

# رسالة التأكيد النهائية
print(f"تم الانتهاء بنجاح! تم تجميع {account_number - 1} ملف في {output_file}")
