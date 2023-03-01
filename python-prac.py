trainingData = {
    "title" : "Lorem Ipsum",
    "paragraph" : "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ipsam ab illum earum eum omnis libero, laudantium iste est quas ratione fuga, temporibus, nam soluta suscipit itaque harum magnam saepe. Modi!",
    "color" : ["color_one", "color_two","color_three"]
}

for key, value in trainingData.items():
    if(key == "color"):
        for color in value:
            print(color)
    else:
        print(value)