import webbrowser

keywords=[
    'The Office US',
    'John Krasinski',
    'Emily Blunt',
    'The Strange Things'
]

for keyword in keywords:
    url='https://www.google.com/search?q='+keyword
    webbrowser.open_new(url)