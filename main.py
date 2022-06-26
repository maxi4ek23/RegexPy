import re
def main():
    file = open('D:/pycharm/lab3/resourses/con267.tweetie.799608879', 'r')
    lines = file.readlines()
    count = 0
    regex = "Games/mines.*gif"
    print("Output of all queries:")
    for line in lines:
        if re.search(regex, line):
            count = count + 1
            print("Query: {}".format(line.strip()))
    print("Number of all queries:", count)
if __name__ == "__main__":
    main()

