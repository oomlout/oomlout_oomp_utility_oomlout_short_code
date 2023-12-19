



def get_oomlout_short_code(details):
    oomlout_short_code = ""
    deets_order = ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]
    deets = {}
    if details != None:
        for deet in deets_order:
            if deet in details:
                deets[deet] = details[deet]
        
        # get for screw bolt set screw
        match = deets["type"].startswith("bolt")
        if match:
            oomlout_short_code = match_screw(details, deets)
        match = deets["type"].startswith("screw_")
        if match:
            oomlout_short_code = match_screw(details, deets)
        match = deets["type"].startswith("set_screw")
        if match:
            oomlout_short_code = match_screw(details, deets)
    


    return oomlout_short_code


def match_screw(details, deets):
    oomlout_short_code = ""
    ## type
    
    typ_source = deets["type"]
    typ_match = []
    typ_match.append(["bolt","b"])
    typ_match.append(["screw_machine_screw","ms"])
    typ_match.append(["screw_socket_cap","sc"])
    typ_match.append(["screw_countersunk","cs"])
    typ_match.append(["set_screw","ss"])
    
    typ = ""
    for match in typ_match:
        if match[0] == typ_source:
            typ = match[1]

    size = ""
    color = ""
    if typ != "":
        #size
        size = deets["size"].replace("_mm","")
        size.replace("_","d") # deal with decimal points
        
        #color
        color_source = deets["color"]
        color_match = []
        color_match.append(["black","b"])
        color_match.append(["stainless","s"])
        color_match.append(["gold","g"])
        color = "m"
        for match in color_match:
            if match[0] == color_source:
                color = match[1]

        # length
        length = deets["description_main"]
        length = length.replace("_mm","")

        # head
        head_source = deets["description_extra"]
        head_match = []
        head_match.append(["flat_head","f"])
        head_match.append(["phillips_head","p"])
        head_match.append(["pozidrive_head","pz"])
        head_match.append(["hex_head","h"])
        head = ""
        for match in head_match:
            if match[0] == head_source:
                head = match[1]
        
        oomlout_short_code = f"{typ}{size}{color}{length}{head}"

    return oomlout_short_code
    
    
