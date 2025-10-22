import xml.etree.ElementTree as ET


def needs_fixing(xml_string):
  try:
    ET.fromstring(xml_string)
    return False
  except:
    return True

def fix(xml_string):
  output_lines = []
  first_line = True
  for line in xml_string.splitlines():
    if first_line:
      output_lines.append(line)
      previous_line = line
      first_line = False
      continue
    if line_is_trkseg(line):
      if (not line_is_slashtrkseg(previous_line)) and not (line_is_time(previous_line) and not line_is_trkpt(previous_line)):
        print(r"A new </trkseg> line needs to be added.")
        output_lines.append(r"</trkseg>")
    if line_is_trkpt(line):
      if line_is_slashtrkseg(previous_line):
        output_lines.append(r'<trkseg>')
    output_lines.append(line)
    previous_line = line
  output_string = "\n".join(output_lines)
  return output_string

def line_is_trkseg(line):
  return r"<trkseg>" in line

def line_is_slashtrkseg(line):
  return r"</trkseg>" in line

def line_is_time(line):
  return r"time" in line

def line_is_trkpt(line):
  return r"trkpt" in line
