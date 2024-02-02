import barcode
from barcode.writer import ImageWriter

data = '123456789'
code128 = barcode.get_barcode_class('code128')
code128_instance = code128(data, writer=ImageWriter())

filename = 'barcode'
code128_instance.save(filename)
