def relabel(predicted : int) -> str:

    labels = {0: "Artifical Intelligence",
              1: "Computer Vision",
              2: "Machine Learning",
              3: "Robotics"}

    return labels[predicted]