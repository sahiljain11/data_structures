
import os


# RECURSIVE FUNCTION
def helper(directory: str, goal: str) -> str:

    print(directory)

    # BASE CONDITION
    for item in os.listdir(directory):
        file_path = directory + '/' + item
        print(file_path)

        if os.path.isfile(file_path):
            if item == goal:
                return file_path


    for item in os.listdir(directory):

        # "CHOOSE"
        total_path = directory + '/' + item

        # do recursive call
        if os.path.isdir(total_path):
            result = helper(total_path, goal)

            if result != '':
                return result

        # "UNCHOOSE"
        total_path = ''


    return ''

def main() -> None:

    FILE_DIRECTORY = "B"
    GOAL = "gunicorn.conf"

    result = helper(FILE_DIRECTORY, GOAL)
    print(result)

    pass

if __name__ == '__main__':
    main()