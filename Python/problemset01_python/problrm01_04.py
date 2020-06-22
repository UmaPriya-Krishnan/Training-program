###B###
import math
price = 24.95
discount =  0.6
total_price = 24.95 * 0.6
initShipping_cost = 3
afterShipping_cost = 0.75
tc = total_price + initShipping_cost + (total_price + afterShipping_cost) * 59
print("Cost of 60 copies ${0:.2f}" .format(tc))

###C###
start_time = (6*60 + 52)*60
easy_pace = (8*60 + 15)*2
tempo = (7*60 + 12) *3
bf_h = (start_time + easy_pace +tempo)/(60*60)
bf_ih = int(bf_h)
bf_m = (bf_h - bf_ih)*60
bf_im = int(bf_m)
print("Breakfast is at {}:{} am" .format(bf_ih,bf_im))

