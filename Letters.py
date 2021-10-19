import matplotlib.pyplot as plt 

class_data_array = []

class data:
    def __init__(self, char, num):
        self.char = char
        self.num = num


def delete(STRING):
    new_array = []
    for i in sorted(STRING):
        if i not in new_array:
            new_array.append(i)
    return new_array

def append_data_class(string, original):
    for i in range(0, len(string)):
        cc = original.count(string[i])
        print(string[i] + " " + str(cc))
        class_data_array.append(data(string[i], cc))

def print_grap():

    for x in range(len(class_data_array)):
        plt.bar(class_data_array[x].char, class_data_array[x].num)
        
    plt.title('test') 
    plt.draw() 
    plt.show() 


def main():
    TEST_STRING = input("input text: ")
    short_array = delete(TEST_STRING)
    append_data_class(short_array, TEST_STRING) 
    print_grap()


if __name__ == '__main__':
    main()
