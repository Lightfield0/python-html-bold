import re
import os
import traceback
if not os.path.exists('kalın_olacak_metinler.txt'):
    # Dosya yoksa, boş bir dosya oluştur
    with open('kalın_olacak_metinler.txt', 'w', encoding='utf-8'):
        pass
try:
    os.startfile('kalın_olacak_metinler.txt')
    input("Eğer txt dosyasına metinleri kaydettiyseniz kalınlaştırmak için bir tuşa basın(klasörü inceleyin)>> ")
    with open('kalın_olacak_metinler.txt', 'r', encoding='utf-8') as normal:
        with open('kalınlar.txt', 'w', encoding='utf-8') as bold:
            for line in normal:
                # <p> ve : arasındaki metni yakala
                pattern = r'(<p>)(.*?)( )'

                # <p> ve : arasındaki metni <strong> etiketleri ile sar
                replacement = r'\1<strong>\2</strong>\3'

                bold_text = re.sub(pattern, replacement, line)

                bold.write(bold_text)

except Exception as e:
    # Hata günlüğü oluştur ve hatayı yaz
    with open('error_log.txt', 'w') as error_log:
        error_log.write(traceback.format_exc())