# Django-Inventory-System
This application is meant for China Spring ISD to be able to easily catalogue educational development devices, print QR-code labels, and scan/access the records based on those labels

This program is intended for use with the [Zebra Browser Print](https://www.zebra.com/us/en/products/software/barcode-printers/link-os/browser-print.html) application to make use of the Zebra ZD410 thermal label printer

## Features
- Integration with Zebra Printing Language (ZPL) for full range compatibility with the Zebra ZD410 thermal printer
- SQL-based report generation and creation for generating mass records on devices
- Elastic search functionality, full or partial word
- QR code functionality for easy label scanning and record editing
- User authentication
- Designed for ease of use and quick integration into current school district IT environments

## Technologies Used
- PostgreSQL
- Python3
- Haystack
- Whoosh
- Smart_selects
- Zebra Printing Language (ZPL)
- [django-qr-code](https://github.com/dprog-philippe-docourt/django-qr-code)
- [django-sql-explorer](https://github.com/groveco/django-sql-explorer)


## Screenshots
![screen-shot-2019-02-04-at-4 59 38-pm](https://user-images.githubusercontent.com/9206287/52243475-5f94a900-289f-11e9-84dc-35ff65b518e6.png)
![screen-shot-2019-02-04-at-5 00 06-pm](https://user-images.githubusercontent.com/9206287/52243483-66232080-289f-11e9-8f7f-8bc1aa9d7c41.png)
<img width="1665" alt="screen shot 2019-02-04 at 4 59 51 pm" src="https://user-images.githubusercontent.com/9206287/52243487-6a4f3e00-289f-11e9-99be-b667d062de82.png">
<img width="1675" alt="screen shot 2019-02-04 at 5 00 17 pm" src="https://user-images.githubusercontent.com/9206287/52243494-70ddb580-289f-11e9-9f72-f03353e58378.png">
