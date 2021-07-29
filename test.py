import ezdxf

# Create a new DXF document.
doc = ezdxf.new(dxfversion='R2010')

# Create new table entries (layers, linetypes, text styles, ...).
doc.layers.new('TEXTLAYER', dxfattribs={'color': 2})

# DXF entities (LINE, TEXT, ...) reside in a layout (modelspace, 
# paperspace layout or block definition).  
msp = doc.modelspace()

# Add entities to a layout by factory methods: layout.add_...() 
msp.add_line((0, 0), (2000, 0), dxfattribs={'color': 7})
msp.add_line((2000, 0), (0, 100), dxfattribs={'color': 7})
msp.add_line((100, 0), (100, 100), dxfattribs={'color': 7})
msp.add_line((0, 100), (100, 100), dxfattribs={'color': 7})


msp2 = doc.modelspace()

# Add entities to a layout by factory methods: layout.add_...() 
msp2.add_line((230, 0), (100,230), dxfattribs={'color':17})
msp2.add_line((0,230), (0, 12300), dxfattribs={'color': 17})
msp2.add_line((10230, 0), (100, 12300), dxfattribs={'color': 17})
msp2.add_line((0, 10230), (100, 1000), dxfattribs={'color': 17})

# msp.add_text(
#     'Test', 
#     dxfattribs={
#         'layer': 'TEXTLAYER'
#     }).set_pos((0, 0.2), align='CENTER')

# Save DXF document.
doc.saveas('test.dxf')

