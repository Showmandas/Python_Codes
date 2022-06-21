
likes=400
share=300
views=1000

conditions=[
    likes>100,
    share>100,
    views>140
]

if all(conditions):
    print("It's awsome video")
if any(conditions):
    print("Mmmm it's great")