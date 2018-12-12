from kaola_flash_sale import FKaola
from kaola_hot_spider import HKaola
from kaola_nine_nine import NKaola
import os
import shutil
import time


hkaola = HKaola()
nkaola = NKaola()
fkaola = FKaola()

hkaola.main()
nkaola.main()
fkaola.main()


if not os.path.exists(os.getcwd()+'/kaola'):
    os.mkdir(os.getcwd()+'/kaola')

old_path = os.getcwd()
new_path = os.getcwd()+'/kaola'
timee = time.strftime('%m%d',time.localtime(time.time()))

try:
    shutil.move(old_path+'/'+timee+'_hot.json',new_path)
except:
    os.remove(new_path+'/'+timee+'_hot.json')
    shutil.move(old_path + '/' + timee + '_hot.json', new_path)

try:
    shutil.move(old_path+'/'+timee+'_hot.xls',new_path)
except:
    os.remove(new_path + '/' + timee + '_hot.xls')
    shutil.move(old_path + '/' + timee + '_hot.xls', new_path)

try:
    shutil.move(old_path+'/'+timee+'_nine_nine.json',new_path)
except:
    os.remove(new_path + '/' + timee + '_nine_nine.json')
    shutil.move(old_path + '/' + timee + '_nine_nine.json', new_path)

try:
    shutil.move(old_path+'/'+timee+'_nine_nine.xls',new_path)
except:
    os.remove(new_path + '/' + timee + '_nine_nine.xls')
    shutil.move(old_path + '/' + timee + '_nine_nine.xls', new_path)

try:
    shutil.move(old_path+'/'+timee+'_flash_sale.json',new_path)
except:
    os.remove(new_path + '/' + timee + '_flash_sale.json')
    shutil.move(old_path + '/' + timee + '_flash_sale.json', new_path)

try:
    shutil.move(old_path+'/'+timee+'_flash_sale.xls',new_path)
except:
    os.remove(new_path + '/' + timee + '_flash_sale.xls')
    shutil.move(old_path + '/' + timee + '_flash_sale.xls', new_path)

print('-'*100)
print('SUCCESS')

