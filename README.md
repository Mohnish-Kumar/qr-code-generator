# QR Code Generator

This is a simple Python script that allows you to generate QR codes using the `qrcode` library. The generated QR code can encode various types of data, including text, URLs, or contact information.

## Prerequisites

Before running this script, you need to ensure that you have the following:

1. Python installed on your system.
2. The `qrcode` library, which can be installed using the following command:
   ```
   pip install qrcode[pil]
   ```

## How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script by executing the following command:
   ```
   python qrcodegenerator.py
   ```

4. You will be prompted to enter the data that you want to encode into the QR code. Please note that the input should not contain spaces.

5. The script will generate a QR code using the provided data and save it as "output.png" in the same directory.

## Customization Options

You can customize the QR code's appearance by modifying the following parameters in the script:

- `version`: This represents the version of the QR code. Higher versions produce larger and more complex QR code images. The valid range is from 1 to 40.

- `box_size`: The size of each box (pixel) that makes up the QR code image.

- `border`: The width of the white border around the QR code image.

You can adjust these values to get QR codes of different sizes and complexities.

## Example

Let's say you want to create a QR code for a URL. You would run the script, enter the URL when prompted, and the script will generate the QR code image for that URL.

## Contributing

If you find any issues with the script or want to suggest improvements, feel free to create an issue or submit a pull request. Your contributions are welcome!

Happy QR code generating! 😄
