#! python

import pandas as pd

house_number_list = [9430 + i for i in range(13)]
street_name = 'Carriage Hill St'

tax_list = [8187.69, 8127.9, 8569.05, 8393.27, 8053.32, 7431.18, 8475.8, 7085.69, 8174.25, 10556.1, 7967.15, 7313.47, 8461.17]
owner_list = ['BLESSING JENNIFER & BRYAN', 'WINTON MICHAEL', 'ARNSBERGER CHRISTOPHER;ARNSBERGER CARRIE', 'DIMA ALDEN A &;DIMA RANIA G', 'RIDGELY STEVEN J & FANCY M', 'CALLANDER THOMAS WILLIAM TRUSTEE;CALLANDER LEIGH ZANOWSKI TRUSTEE', 'VOGEL ALEXANDER C;VOGEL JESSICA A', 'ARRA SWETHA;PALWAI SUDHEENDRA REDDY', 'FENG YAN;YAN RU', 'STEIN LINDSAY;STEIN BRANDON', 'SCHWARZ CHRISTOPHER JOHN', 'SPANGLER TARL C SR &;SPANGLER TRACY GARFIELD', 'SHEEHY TIMOTHY;LONG KEITH']
above_grade_living_area_list = ['2880 SF', '2632 SF', '2892 SF', '2828 SF', '2892 SF', '2216 SF', '2894 SF', '2240 SF', '2832 SF', '3740 SF', '2820 SF', '2216 SF', '2832 SF']
finished_basement_area_list = ['572 SF', '700 SF', '1100 SF', '779 SF', '580 SF', '880 SF', '612 SF', '', '612 SF', '1296 SF', '574 SF', '515 SF', '1380 SF']

df = pd.DataFrame({'house number': house_number_list, 'owner': owner_list, 
                   'tax': tax_list,
                   'above area': above_grade_living_area_list,
                   'basement area': finished_basement_area_list})

df.to_csv('Carriage_Hill_St_tax.csv', sep=',', index = False)