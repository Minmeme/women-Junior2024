import base64

input_file = "output.txt"
output_file = "outpu.txt"
res = ""
i = 0

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        try:
            # Add padding if needed and decode
            decoded_line = base64.b64decode(line.strip() + "==").decode()
            res += "".join(decoded_line.split("-")[1:])
            print(decoded_line)
            i = i + 1
            if i == 85549:
                break
            outfile.write(decoded_line + "\n")
        except Exception as e:
            print(f"Error decoding line {i}: {e}")

try:
    # Try to decode the accumulated result into image data
    image_data = base64.b64decode(res)
    # Write the binary data to an image file
    with open("output_image", "wb") as image_file:
        image_file.write(image_data)
except Exception as e:
    print(f"Error creating image: {e}")