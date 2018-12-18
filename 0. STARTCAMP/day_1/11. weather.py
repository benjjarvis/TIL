from darksky import forecast

Multicampus = forecast('954d6d09819bbaa5f95fa0ac10837211', 37.501562, 127.039660)

print(Multicampus['currently']['summary'])
print(Multicampus['currently']['temperature'])