# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   seats_count = 0
   for row in seats:
      seats_count += len(row)
   return seats_count

def seats_available(seats):
   for row in seats:
      if 'A' in row:
         available_count = row.count('A')
   return available_count

def seats_booked(seats):
    for row in seats:
       if 'B' in row:
          booked_count = row.count('B')
    return booked_count

def seat_status(seats, row, place):
   for row_index in range(len(seats)):
      for col_index in range(len(seats[row_index])):
        status = seats[row_index][col_index]
        return status

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))