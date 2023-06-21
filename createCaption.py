import replicate

# replicate.run(
#   "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
#   input={"prompt": "a 19th century portrait of a wombat gentleman"}
# )


image = open("testImages/people.webp", "rb")

def get_details(image):
    output = replicate.run(
            "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
            input={"image": image}
                )
    return output

def getImage(prompt):
    import replicate
    output = replicate.run(
        "ai-forever/kandinsky-2:601eea49d49003e6ea75a11527209c4f510a93e2112c969d548fbb45b9c4f19f",
        input={"prompt": prompt +  "720 p"}
    )
    return output[0]


def getImage2(prompt):
    output = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": prompt}
        )
    return output[0]

if __name__ == "__main__":
    # print(get_details(image)) 
    # output = getImage("a 19th century portrait of a wombat gentleman")
    # output = getImage("Automated museum entrance - effortless exploration.")
    output = getImage2('a 19th century portrait of a wombat gentleman')
    print(output)

