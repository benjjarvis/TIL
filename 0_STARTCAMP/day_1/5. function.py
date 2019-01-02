first=[11.25, 18.0, 20.0]
second=[10.75, 9.50]

full=first+second
full
[11.25, 18.0, 20.0, 10.75, 9.5]

full_sorted=sorted(full) #기본적으로 reverse=False가 디폴트값으로 들어가 있음.
full_sorted
[9.5, 10.75, 11.25, 18.0, 20.0]

reverse_sorted=sorted(full, reverse=True)
reverse_sorted
[20.0, 18.0, 11.25, 10.75, 9.5]