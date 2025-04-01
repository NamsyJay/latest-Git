import xml.etree.ElementTree as ET
from xml.dom import minidom

#Parse an XML file
#tree = ET.parse('books.xml')
#root = tree.getroot()


#for book in root.findall('book'):
#    title   = book.find('title').text
#    author  = book.find('author').text
#    
#    
#    print(f"Title: {title}, Author: {author}") 
    
# Pretty Print XML
def prettify_xml(elem):
    """Convert XML ElementTree object to a pretty-formatted XML string."""
    rough_string = ET.tostring(elem, encoding="utf-8")
    parsed = minidom.parseString(rough_string)
    return parsed.toprettyxml(indent="  ")

# Add New Books to the XML file
def add_book(xml_file, title, author, year):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Create A New Book
        new_book = ET.SubElement(root, 'book')
        ET.SubElement(new_book, 'title').text = title
        ET.SubElement(new_book, 'author').text = author
        ET.SubElement(new_book, 'year').text = str(year)
        
        # Formatted The XML Document Properly 
        formatted_xml = prettify_xml(root)
        
        # Save The Modified XML file
        with open(xml_file, 'w', encoding='utf-8') as f:
            f.write(formatted_xml)
        
        print(f"{title} Added Successfully!")
    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error: {e}")
        
# Add A New Book
add_book('books.xml', 'Observabilty & Telementry', 'Charity Majors ', "2022")