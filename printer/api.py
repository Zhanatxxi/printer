import random

from printer.apps.client.usb_connection import get_usb_object


if __name__ == '__main__':
    printer = get_usb_object()
    # printer.text("test123")
    # printer.barcode('ABC-abc-1234', 'CODE128', 255, 5, 'BELOW', 'A',
    #                 function_type='B', align_ct=False, )
    # printer.barcode('111111111112', 'EAN13', 155, 4, '', '')
    # printer.barcode("{B012ABCDabcd", "CODE128", function_type="B")
    # for i in range(0, 4):
    #     printer.qr(f"zhanat{i}", size=15, native=False, ec=0)
    #     printer.cut()
    random_range = list([str(random.randrange(0, 9)) for i in range(10)])
    random_range.append("KG09544ATF")
    data = "".join(random_range)
    printer.qr(data, size=10, ec=0, model=2)
    # printer.line_spacing()
    printer.text(f"thi's your code in {data}")
    printer.cut()
