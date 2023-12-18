



def get_oomlout_short_code(details):
    oomlout_short_code = ""
    deets_order = ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]
    deets = {}
    for deet in deets_order:
        if deet in details:
            deets[deet] = details[deet]
    
    # get for screw
    match = deets["type"].startswith("screw_")
    if match:
        oomlout_short_code = match_screw(details, deets)


    return oomlout_short_code


def match_screw(details, deets):
    oomlout_short_code = ""
    ## type
    typ = ""
    if deets["type"] == "screw_socket_cap":
        typ = "sc"

    size = ""
    if typ != "":
        size = deets["size"].replace("_mm","")
        size.replace("_","d") # deal with decimal points
        size = f"{size}m"
        length = deets["description_main"]
        length = length.replace("_mm","")
        size = f"{size}{length}"
        oomlout_short_code = f"{typ}{size}"

    return oomlout_short_code
    
    
