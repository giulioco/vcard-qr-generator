"""
File: vcard_qr_code_gen.py

Desc: 
Script for generating a QR Code from a vCard input.

Author: Giulio Colleluori <gcollelu@ucsc.edu>
"""

import urllib

vcard_file_name = raw_input("vCard File name (e.g. 'john.vcf'): ")
with open(vcard_file_name, 'r') as myfile:
	vcard = myfile.read()

QR_CODE_TEMPLATE = "http://api.qrserver.com/v1/create-qr-code/?data=%s&size=300x300"
vcard_url = QR_CODE_TEMPLATE % (vcard)
cnxn = urllib.urlopen(vcard_url)
qr_code = cnxn.read()
cnxn.close()
qr_filename = "qr_code.png"
with open(qr_filename, 'w') as qr_file_hdl:
	qr_file_hdl.write(qr_code)
print "Created QR-code %s file." %(qr_filename)