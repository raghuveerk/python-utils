import urllib2 
import json
import csv
import time


mapsurl = 'https://maps.googleapis.com/maps/api/geocode/json'
addressParam = 'address='
apikey = 'key=AIzaSyBI-EVtuke9dQRW801flBzA7-kMC7G58Zg'
filename = 'CSV-WestRegionLMS.csv'
ifile  = open(filename, "rU")
reader = csv.reader(ifile, delimiter=',', quotechar='"', dialect=csv.excel_tab)
state = 'CA'
fourty9thDistrictZips = ['92003','92007','92008','92009','92010','92011','92014','92024','92028','92029','92037','92054','92055','92056','92057','92058','92067','92075','92078','92081','92083','92084','92091','92121','92127','92130','92624','92629','92651','92672','92673','92675','92677','92679','92688','92691','92692','92694']

ts = time.time()
outputFilename = './python-output-'+str(ts)+'.txt'
f1=open(outputFilename, 'w+')

print >>f1, 'Now processing input from file: %s' % (filename) 
print >>f1, 'LEGEND FN:FirstName, LN:LastName, SN: SpouseName, SA: StreetAddress, C: City, T: Telephone' 
rownum = 0
for row in reader:
	if rownum == 0:
        	header = row
	else:
		if row:
			firstName = row[0]
			lastName = row[1]
			spouseName = row[2]
			streetAddress = row[3]
			city = row[4]
			telephone = row[5]
			streetAddress = streetAddress.replace('#', '.')

			address = addressParam + streetAddress + ' ' + city + ' ' + state
			address = address.replace(' ', '+')	
			
			data = address + '&' + apikey
			reqUrl = url=mapsurl+'?'+data
			req = urllib2.Request(reqUrl)
			f = urllib2.urlopen(req)

			j = json.loads(f.read())
			
			if j['status'] == 'OK':
				fourDigitZip = ''
				zipSuffix = ''
				for entry in j['results'][0]['address_components']:
    					if "postal_code" in entry['types']:
						fourDigitZip = entry['long_name']
					
					if "postal_code_suffix" in entry['types']:
						zipSuffix = entry['long_name']							


				if fourDigitZip in fourty9thDistrictZips:	
					print >>f1, '-------------------Row %s ----------------------------' % (rownum)
                        		print >>f1, 'FN:%s LN:%s SN:%s SA:%s C:%s T:%s' % (firstName, lastName, spouseName, streetAddress, city, telephone)
                        		print >>f1, '%s' % (reqUrl)
					print >>f1, '49th district of CA member found with Zipcode: %s-%s' % (fourDigitZip, zipSuffix)
					if zipSuffix == '':
						print >>f1, 'Last 4 digits of zip is missing'
					
					print >>f1, '------------------End of Row %s-----------------------------' % (rownum)
				#else:
					#print >>f1, 'This member doesn\'t belong to 49th district of CA, Zipcode: %s' % (fourDigitZip)
			else:
				print >>f1, 'Invalid address/response:%s' % (j)
        	else:
			print >>f1, '#### Row %s is empty #####' %s (rownum)            
	rownum += 1

ifile.close()
