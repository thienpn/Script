"""
Convert label to Label Me format (.xml)
XML:

<annotation>
  <filename>09_05_image_20200515000803127_008.jpg</filename>
  <folder></folder>
  <source>
    <sourceImage></sourceImage>
    <sourceAnnotation>Datumaro</sourceAnnotation>
  </source>
  <imagesize>
    <nrows>540</nrows>
    <ncols>720</ncols>
  </imagesize>
  <object>
    <name>plate</name>
    <deleted>0</deleted>
    <verified>0</verified>
    <occluded>no</occluded>
    <date></date>
    <id>0</id>
    <parts>
      <hasparts></hasparts>
      <ispartof></ispartof>
    </parts>
    <polygon>
      <pt>
        <x>224.00</x>
        <y>342.00</y>
      </pt>
      <pt>
        <x>225.00</x>
        <y>381.00</y>
      </pt>
      <pt>
        <x>377.00</x>
        <y>383.00</y>
      </pt>
      <pt>
        <x>377.00</x>
        <y>344.00</y>
      </pt>
      <username></username>
    </polygon>
    <attributes>ocr=93A07015</attributes>
  </object>
</annotation>
"""

import sys
try:
    import lxml.builder
    import lxml.etree
except ImportError:
    print("Please install lxml:\n\n    pip install lxml\n")
    sys.exit(1)

maker = lxml.builder.ElementMaker()
xml = maker.annotation(
    maker.filename("09_05_image_20200515142559294_002.jpg"),
    maker.folder(""),
    maker.source(
        maker.sourceImage(""),
        maker.sourceAnnotation("Datumaro")
    ),
    maker.imagesize(
        maker.nrows(str(540)),
        maker.ncols(str(720))
    ),
)
xml.append(
    maker.object(
        maker.name("plate"),
        maker.deleted(str(0)),
        maker.verified(str(0)),
        maker.occluded("no"),
        maker.date(""),
        maker.id(str(0)),
        maker.parts(
            maker.hasparts(""),
            maker.ispartof("")
        ),
        maker.polygon(
            maker.pt(
                maker.x(str(224.00)),
                maker.y(str(342.00)),
            ),
            maker.pt(
                maker.x(str(225.00)),
                maker.y(str(381.00)),
            ),maker.pt(
                maker.x(str(377.00)),
                maker.y(str(383.00)),
            ),maker.pt(
                maker.x(str(377.00)),
                maker.y(str(344.00)),
            ),
            maker.username("")
        ),
        maker.attributes("ocr=93A07015")
    )
)
with open("09_05_image_20200515000803127_008.xml", "wb") as f:
    f.write(lxml.etree.tostring(xml, pretty_print=True))