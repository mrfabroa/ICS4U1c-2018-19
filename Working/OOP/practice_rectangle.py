

class Rectangle():

    def __init__(self):
        self.width = 0
        self.height = 0


def get_area(rec):
    '''
    Computes the area of a given rectangle
    :param rec: a Rectangle Object
    :return: area of the rec
    '''

    return rec.width * rec.height


def main():

    print("***** Rectangle Class Demo ******")

    # get a width height from user input
    user_width = float(input("Enter the width of the rectangle: "))
    user_height = float(input("Enter the height of the rectangle: "))

    #  create an instance of a Rectangle
    rect1 = Rectangle()

    rect1.width = user_width
    rect1.height = user_height

    print("rectangle width:", rect1.width)
    print("rectangle height:", rect1.height)

    area = get_area(rect1)

    print("The area of the rectangle is", area)

main()




