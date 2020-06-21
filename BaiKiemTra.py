import pyodbc
import smtplib

server = "DESKTOP-9LPUIR9"
databaseName = "QUAN_LY_SAN_PHAM"

driver = '{SQL Server}' # Driver you need to connect to the database
port = '1433' #sql server configuration => TCP/IP (order =2)=>properties =>port
#connection string
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+databaseName+';Trusted_Connection=yes;')

cursor = connection.cursor()

try:
    file = open('C:/Python/hoc_vien1.txt','r')
    a = file.readlines()
    danhSach = []
    for i in range(len(a)):

        x = a[i].split(":")[1].strip()

        danhSach.append(x)

except FileNotFoundError:
    print("File Not Found")

cursor.execute("INSERT INTO HOC_VIEN VALUES (?,?,?,?,?,?,?)", (danhSach[0],danhSach[1],danhSach[2],danhSach[3],danhSach[4],danhSach[5],danhSach[6]))
cursor.commit()


FROM = 'truong.buido@gmail.com'

TO = ["tbtoanit@gmail.com"]

SUBJECT = "Khanh Bùi gửi file"
str1 = ''.join(str(i) for i in danhSach)
TEXT = danhSach[0]+'\n'+danhSach[1]+'\n'+danhSach[2]+'\n'+danhSach[3]+'\n'+danhSach[4]+'\n'+danhSach[5]+'\n'+danhSach[6]
# message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
# message = """\
# From: %s
# To: %s
# Subject: %s
#
# %s
# """ % (FROM, ", ".join(TO), SUBJECT, str(TEXT))
username = 'truong.buido@gmail.com'
password = ''
# Send the mail

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % FROM,
                    'Subject: %s' % SUBJECT,
                    '', str(TEXT)])
#try:
server.sendmail(FROM, TO, BODY)
print ('email sent')
#except:



