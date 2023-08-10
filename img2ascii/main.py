from PIL import Image

ASCII_CHARS = "@B%8WM#*oahkbdpwmZO0QCJYXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:,\^`'. "

def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)
    ascii_str = map_pixels_to_ascii(image)
    return ascii_str

def save_ascii_to_txt(ascii_str, txt_path):
    with open(txt_path, "w") as f:
        f.write(ascii_str)

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    ascii_str = convert_image_to_ascii(image, new_width)
    img_height = int(len(ascii_str) / new_width)
    ascii_str = "\n".join([ascii_str[i:i + new_width] for i in range(0, len(ascii_str), new_width)])

    print(ascii_str)

    save_path = input("File name to save art: ")
    save_ascii_to_txt(ascii_str, save_path + ".txt")
    print(f"ASCII art saved to {save_path}.txt")

if __name__ == "__main__":
    image_path = input("Path to img: ")
    new_width = int(input("Width: "))
    main(image_path, new_width)
