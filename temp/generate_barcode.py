import barcode
from barcode.writer import ImageWriter

def generate_barcode(product_name, product_code):
    ean = barcode.get('ean13', product_code, writer=ImageWriter())
    filename = ean.save(f'{product_name}')
    print(f'Barcode saved as {filename}.png')

# Example usage
generate_barcode('abca', '123456789012')
