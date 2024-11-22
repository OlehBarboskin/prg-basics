polish_license_plates = [
   'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
   'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
   'KK54985', 'LU4864U'
]
counter = 1
for car_number in polish_license_plates:
   if car_number[0] == "K" and car_number [1] == "K" or car_number [1] == "R" :
      print(counter, car_number)
      counter += 1