import pytest

from domain_actions import fix

@pytest.mark.parametrize("test_input,expected",[
  ("2018-04-22-161004.gpx",True),
  ("2020-10-21-173212.gpx",True),
  ("2018-08-14-060428.gpx",False),
  ("2019-03-02-155237.gpx",False),
  ("2019-08-03-191627.gpx",False),
  ("2020-01-02-101159.gpx",False),
  ("2020-05-18-092704.gpx",False),
  ("2020-10-06-172950.gpx",False),
  ("2018-08-14-173731.gpx",False),
  ("2019-03-03-134704.gpx",False),
  ("2019-08-03-202516.gpx",False),
  ("2020-01-02-171410.gpx",False),
  ("2020-05-18-151954.gpx",False),
  ("2020-10-08-062503.gpx",False),
  ("2018-08-15-174938.gpx",False),
  ("2019-03-03-151138.gpx",False),
  ("2019-08-04-074612.gpx",False),
  ("2020-01-03-073432.gpx",False),
  ("2020-05-19-093725.gpx",False),
  ("2020-10-08-063651.gpx",False),
  ("2018-08-16-055320.gpx",False),
  ("2019-03-04-174659.gpx",False),
  ("2019-08-04-155243.gpx",False),
  ("2020-01-03-075325.gpx",False),
  ("2020-05-19-161545.gpx",False),
  ("2020-10-08-120709.gpx",False),
  ("2018-08-16-055927.gpx",False),
  ("2019-03-04-192809.gpx",False),
  ("2019-08-04-171540.gpx",False),
  ("2020-01-03-100534.gpx",False),
  ("2020-05-20-093631.gpx",False),
  ("2020-10-08-150139.gpx",False),
  ("2018-08-16-065817.gpx",False),
  ("2019-03-04-214419.gpx",False),
  ("2019-08-05-062856.gpx",False),
  ("2020-01-03-111316.gpx",False),
  ("2020-05-20-150639.gpx",False),
  ("2020-10-08-170356.gpx",False),
  ("2018-08-17-062010.gpx",False),
  ("2019-03-06-174724.gpx",False),
  ("2019-08-05-063917.gpx",False),
  ("2020-01-04-083248.gpx",False),
  ("2020-05-21-065434.gpx",False),
  ("2020-10-09-113951.gpx",False),
  ("2018-08-17-062925.gpx",False),
  ("2019-03-07-055555.gpx",False),
  ("2019-08-05-070659.gpx",False),
  ("2020-01-04-083834.gpx",False),
  ("2020-05-21-094043.gpx",False),
  ("2020-10-10-075855.gpx",False),
  ("2018-08-18-191611.gpx",False),
  ("2019-03-07-195844.gpx",False),
  ("2019-08-05-173004.gpx",False),
  ("2020-01-04-085622.gpx",False),
  ("2020-05-22-094247.gpx",False),
  ("2020-10-10-082358.gpx",False),
  ("2018-08-19-063326.gpx",False),
  ("2019-03-07-212938.gpx",False),
  ("2019-08-06-173250.gpx",False),
  ("2020-01-04-103510.gpx",False),
  ("2020-05-22-153723.gpx",False),
  ("2020-10-10-095316.gpx",False),
  ("2018-08-19-064435.gpx",False),
  ("2019-03-08-173931.gpx",False),
  ("2019-08-06-174836.gpx",False),
  ("2020-01-04-112731.gpx",False),
  ("2020-05-23-073404.gpx",False),
  ("2020-10-10-100215.gpx",False),
  ("2018-08-19-080600.gpx",False),
  ("2019-03-08-210656.gpx",False),
  ("2019-08-07-062357.gpx",False),
  ("2020-01-04-131014.gpx",False),
  ("2020-05-23-152402.gpx",False),
  ("2020-10-11-092529.gpx",False),
  ("2018-08-20-172618.gpx",False),
  ("2019-03-09-070144.gpx",False),
  ("2019-08-07-063540.gpx",False),
  ("2020-01-04-140911.gpx",False),
  ("2020-05-23-154654.gpx",False),
  ("2020-10-11-093747.gpx",False),
  ("2018-08-21-055505.gpx",False),
  ("2019-03-09-093221.gpx",False),
  ("2019-08-07-173403.gpx",False)
])
def test_needs_fixing_parameterized(test_input, expected):
  path = f'../test_data/unzipped/corrupt/01-runkeeper-data-export-2022-08-23-031722/{test_input}'
  with open(path) as text_file:
    text_string = text_file.read()
  actual_output = fix.needs_fixing(text_string)
  assert actual_output == expected

@pytest.mark.parametrize("test_input,expected",[
  ("2018-04-22-161004.gpx",False),
  ("2020-10-21-173212.gpx",False)
])
def test_fix_parametrized(test_input, expected):
  path = f'../test_data/unzipped/corrupt/01-runkeeper-data-export-2022-08-23-031722/{test_input}'
  with open(path) as text_file:
    text_string = text_file.read()
  string_result = fix.fix(text_string)
  result = fix.needs_fixing(string_result)
  print(string_result)
  assert result == expected

def test_fix_1():
  input = "\n".join(["Something",r"<trkseg>", "Something"])
  expected_output = "\n".join(["Something",r"</trkseg>", "<trkseg>", "Something"])
  output = fix.fix(input)
  assert output == expected_output

def test_fix_2():
  input = "\n".join(["Something",r"</trkseg>",r"<trkpt>", "Something"])
  expected_output = "\n".join(["Something",r"</trkseg>","<trkseg>",r"<trkpt>", "Something"])
  output = fix.fix(input)
  assert output == expected_output


@pytest.mark.parametrize("test_input,expected",[
  ("<trkseg>",True),
  (r"</trkseg>",False),
  ("<time blah>",False),
  ("<trkpt>",False),
  (r'<?xml version="1.0" encoding="UTF-8"?>', False),
  (r"<gpx", False),
  (r'  version="1.1"', False),
  (r'  creator="Runkeeper - http://www.runkeeper.com"', False),
  (r'  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"', False),
  (r'  xmlns="http://www.topografix.com/GPX/1/1"', False),
  (r'  xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"', False),
  (r'  xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">', False),
  (r'<trk>', False),
  (r'  <name><![CDATA[Walking 10/21/20 5:32 pm]]></name>', False),
  (r'  <time>2020-10-21T21:32:12Z</time>', False),
  (r'<trkseg>', True),
  (r'<trkpt lat="38.848533000" lon="-77.090411000"><ele>56.0</ele><time>2020-10-21T21:32:12Z</time></trkpt>', False),
  (r'<trkpt lat="38.848533000" lon="-77.090411000"><ele>56.0</ele><time>2020-10-21T21:32:12Z</time></trkpt>', False),
  (r'</trkseg>', False),
  (r'<trkpt lat="38.848533000" lon="-77.090399000"><ele>56.0</ele><time>2020-10-21T21:32:38Z</time></trkpt>', False),
  (r'</trkseg>', False),
  (r'<trkseg>', True),
  (r'<trkpt lat="38.848487000" lon="-77.090504000"><ele>57.0</ele><time>2020-10-21T21:32:59Z</time></trkpt>', False),
  (r'<trkpt lat="38.848538000" lon="-77.090590000"><ele>57.0</ele><time>2020-10-21T21:33:10Z</time></trkpt>', False),
  (r'<trkpt lat="38.848518000" lon="-77.090606000"><ele>57.0</ele><time>2020-10-21T21:33:18Z</time></trkpt>', False),
  (r'</trkseg>', False),
  (r'<trkseg>', True)])
def test_line_is_trkseg(test_input,expected):
  assert fix.line_is_trkseg(test_input) == expected

@pytest.mark.parametrize("test_input,expected",[
  ("<trkseg>",False),
  (r"</trkseg>",True),
  ("<time blah>",False),
  ("<trkpt>",False),
  (r'<?xml version="1.0" encoding="UTF-8"?>', False),
  (r"<gpx", False),
  (r'  version="1.1"', False),
  (r'  creator="Runkeeper - http://www.runkeeper.com"', False),
  (r'  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"', False),
  (r'  xmlns="http://www.topografix.com/GPX/1/1"', False),
  (r'  xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"', False),
  (r'  xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">', False),
  (r'<trk>', False),
  (r'  <name><![CDATA[Walking 10/21/20 5:32 pm]]></name>', False),
  (r'  <time>2020-10-21T21:32:12Z</time>', False),
  (r'<trkseg>', False),
  (r'<trkpt lat="38.848533000" lon="-77.090411000"><ele>56.0</ele><time>2020-10-21T21:32:12Z</time></trkpt>', False),
  (r'<trkpt lat="38.848533000" lon="-77.090411000"><ele>56.0</ele><time>2020-10-21T21:32:12Z</time></trkpt>', False),
  (r'</trkseg>', True),
  (r'<trkpt lat="38.848533000" lon="-77.090399000"><ele>56.0</ele><time>2020-10-21T21:32:38Z</time></trkpt>', False),
  (r'</trkseg>', True),
  (r'<trkseg>', False),
  (r'<trkpt lat="38.848487000" lon="-77.090504000"><ele>57.0</ele><time>2020-10-21T21:32:59Z</time></trkpt>', False),
  (r'<trkpt lat="38.848538000" lon="-77.090590000"><ele>57.0</ele><time>2020-10-21T21:33:10Z</time></trkpt>', False),
  (r'<trkpt lat="38.848518000" lon="-77.090606000"><ele>57.0</ele><time>2020-10-21T21:33:18Z</time></trkpt>', False),
  (r'</trkseg>', True),
  (r'<trkseg>', False)])
def test_line_is_slashtrkseg(test_input,expected):
  assert fix.line_is_slashtrkseg(test_input) == expected

@pytest.mark.parametrize("test_input,expected",[
  ("<trkseg>",False),
  (r"</trkseg>",False),
  ("<time blah>",True),
  ("<trkpt>",False),
  (r'<?xml version="1.0" encoding="UTF-8"?>', False),
  (r"<gpx", False),
  (r'  version="1.1"', False),
  (r'  creator="Runkeeper - http://www.runkeeper.com"', False),
  (r'  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"', False),
  (r'  xmlns="http://www.topografix.com/GPX/1/1"', False),
  (r'  xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"', False),
  (r'  xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">', False),
  (r'<trk>', False),
  (r'  <name><![CDATA[Walking 10/21/20 5:32 pm]]></name>', False),
  (r'  <time>2020-10-21T21:32:12Z</time>', True),
  (r'<trkseg>', False),
  (r'<trkpt lat="38.848533000" lon="-77.090411000"><ele>56.0</ele><time>2020-10-21T21:32:12Z</time></trkpt>', True),
  (r'<trkpt lat="38.848533000" lon="-77.090411000"><ele>56.0</ele><time>2020-10-21T21:32:12Z</time></trkpt>', True),
  (r'</trkseg>', False),
  (r'<trkpt lat="38.848533000" lon="-77.090399000"><ele>56.0</ele><time>2020-10-21T21:32:38Z</time></trkpt>', True),
  (r'</trkseg>', False),
  (r'<trkseg>', False),
  (r'<trkpt lat="38.848487000" lon="-77.090504000"><ele>57.0</ele><time>2020-10-21T21:32:59Z</time></trkpt>', True),
  (r'<trkpt lat="38.848538000" lon="-77.090590000"><ele>57.0</ele><time>2020-10-21T21:33:10Z</time></trkpt>', True),
  (r'<trkpt lat="38.848518000" lon="-77.090606000"><ele>57.0</ele><time>2020-10-21T21:33:18Z</time></trkpt>', True),
  (r'</trkseg>', False),
  (r'<trkseg>', False)])
def test_line_is_time(test_input, expected):
  assert fix.line_is_time(test_input) == expected

@pytest.mark.parametrize("test_input,expected",[
  ("<trkseg>",False),
  (r"</trkseg>",False),
  ("<time blah>",False),
  ("<trkpt>",True),
  (r'<?xml version="1.0" encoding="UTF-8"?>', False),
  (r"<gpx", False),
  (r'  version="1.1"', False),
  (r'  creator="Runkeeper - http://www.runkeeper.com"', False),
  (r'  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"', False),
  (r'  xmlns="http://www.topografix.com/GPX/1/1"', False),
  (r'  xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"', False),
  (r'  xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1">', False),
  (r'<trk>', False),
  (r'  <name><![CDATA[Walking 10/21/20 5:32 pm]]></name>', False),
  (r'  <time>2020-10-21T21:32:12Z</time>', False),
  (r'<trkseg>', False),
  (r'<trkpt lat="38.848533000" lon="-77.090411000"><ele>56.0</ele><time>2020-10-21T21:32:12Z</time></trkpt>', True),
  (r'<trkpt lat="38.848533000" lon="-77.090411000"><ele>56.0</ele><time>2020-10-21T21:32:12Z</time></trkpt>', True),
  (r'</trkseg>', False),
  (r'<trkpt lat="38.848533000" lon="-77.090399000"><ele>56.0</ele><time>2020-10-21T21:32:38Z</time></trkpt>', True),
  (r'</trkseg>', False),
  (r'<trkseg>', False),
  (r'<trkpt lat="38.848487000" lon="-77.090504000"><ele>57.0</ele><time>2020-10-21T21:32:59Z</time></trkpt>', True),
  (r'<trkpt lat="38.848538000" lon="-77.090590000"><ele>57.0</ele><time>2020-10-21T21:33:10Z</time></trkpt>', True),
  (r'<trkpt lat="38.848518000" lon="-77.090606000"><ele>57.0</ele><time>2020-10-21T21:33:18Z</time></trkpt>', True),
  (r'</trkseg>', False),
  (r'<trkseg>', False)])
def test_line_is_trkpt(test_input, expected):
  assert fix.line_is_trkpt(test_input) == expected
