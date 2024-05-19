import glob

import inquirer
from rembg import remove
from PIL import Image


def get_images() -> list[str]:
    """Return a list with the filenames of all '.jpg', '.jpeg' and '.png' files
    in the current dir"""
    patterns = ['*.jpg', '*.jpeg', '*.png']
    image_files = []
    for pattern in patterns:
        image_files.extend(glob.glob(pattern))
    return image_files


def remoge_background(image_file:str) -> None:
    file_name = image_file.split(".")[0]
    output_file = f"{file_name}_removed_bg.png"

    input = Image.open(image_file)
    output = remove(input)
    output.save(output_file) # type: ignore


def main():
    images_files = get_images()

    questions = [
        inquirer.List(
            'image_file',
            message="Remove background of which image?",
            choices=images_files
        )
    ]

    answer:dict = inquirer.prompt(questions) or {}

    image_file:str = answer.get("image_file", "")

    remoge_background(image_file)


if __name__ == "__main__":
    main()
