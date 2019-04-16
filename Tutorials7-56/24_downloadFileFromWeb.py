from urllib import request


def download_test_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\r")
    dest_url = r'test.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


sample_url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
download_test_data(sample_url)

