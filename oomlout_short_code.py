



def get_oomlout_short_code(details):
    oomlout_short_code = ""
    deets_order = ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]
    deets = {}
    if details != None:
        for deet in deets_order:
            if deet in details:
                deets[deet] = details[deet]

        #bearing
                
        match_list = []
        match_list.append("bearing")

        typ = deets.get("type","")

        for match in match_list:
            if typ.startswith(match):
                oomlout_short_code = match_bearing(details, deets)
        
        # nut
        match_list = []
        match_list.append("nut")

        for match in match_list:
            if typ.startswith(match):
                oomlout_short_code = match_nut(details, deets)


        # packaging
        match_list = []
        match_list.append("takeaway")

        for match in match_list:
            if typ.startswith(match):
                oomlout_short_code = match_packaging(details, deets)

        # screw
        # bolt
        # set screw
        # spacer
        match_list = []
        match_list.append("bolt")
        match_list.append("screw_")
        match_list.append("set_screw")
        match_list.append("spacer")
        match_list.append("standoff")

        for match in match_list:
            if typ.startswith(match):
                oomlout_short_code = match_screw(details, deets)

                

        
    


    return oomlout_short_code

def match_bearing(details, deets):
    oomlout_short_code = ""
    ## type
    
    typ = "br"
    
    color = deets.get("color","")

    color = color.replace("_size","").replace("_","")


    oomlout_short_code = f"{typ}{color}"

    return oomlout_short_code


def match_packaging(details, deets):
    oomlout_short_code = ""

    oomlout_short_code = ""
    ## type
    
    typ_source = deets.get("type","")
    typ_match = []
    typ_match.append(["takeaway_container_circle","tcc"])
    typ_match.append(["takeaway_container_rectangle","tcr"])
    
    typ = ""
    for match in typ_match:
        if match[0] == typ_source:
            typ = match[1]

    
    size = ""

    size_source = deets.get("size","")
    size = size_source.replace("_ml","")

    description_main = ""
    description_main_source = description_main
    description_main_match = []
    description_main_match.append(["hinged_lid","hl"])

    for match in description_main_match:
        if match[0] == description_main_source:
            description_main = match[1]


    if typ != "":
        oomlout_short_code = f"{typ}{size}{description_main}"

    return oomlout_short_code




def match_nut(details, deets):
    oomlout_short_code = ""
    ## type
    
    typ_source = deets.get("type","")
    typ_match = []
    typ_match.append(["nut","n"])
    
    typ = ""
    for match in typ_match:
        if match[0] == typ_source:
            typ = match[1]

    size = ""
    color = ""
    if typ != "":
        #size       
        size = deets.get("size","")         
        size = size.replace("_mm","").replace("m","")
        size = size.replace("_","d") # deal with decimal points

        


        #color
        color_source = deets.get("color","")
        color_match = []
        color_match.append(["nylon_black","nb"])
        color_match.append(["black","b"])
        color_match.append(["brass","br"])
        color_match.append(["bright_zinc_plated","bz"])
        color_match.append(["stainless","s"])
        color_match.append(["nylon_white","nw"])
        color_match.append(["gold","g"])
        color = "m"
        for match in color_match:
            if match[0] == color_source:
                color = match[1]

    description_main = ""
    desc_main = deets.get("description_main","")
    description_main_source = desc_main
    description_main_match = []
    description_main_match.append(["flanged","fl"])
    description_main_match.append(["locking","lo"])
    description_main_match.append(["coupling","co"])
    description_main_match.append(["2020","2"])

    for match in description_main_match:
        if match[0] == description_main_source:
            description_main = match[1]
        
    description_extra = ""
    desc_extra = deets.get("description_extra","")
    description_extra_source = desc_extra
    description_extra_match = []
    description_extra_match.append(["t_nut","t"])
    description_extra_match.append(["ball_spring","w"])

    for match in description_extra_match:
        if match[0] == description_extra_source:
            description_extra = match[1]

    oomlout_short_code = f"{typ}{size}{color}{description_main}{description_extra}"

    return oomlout_short_code


    

def match_screw(details, deets):
    oomlout_short_code = ""
    ## type
    
    typ_source = deets.get("type","")
    typ_match = []
    typ_match.append(["bolt","b"])
    typ_match.append(["screw_machine_screw","ms"])
    typ_match.append(["screw_socket_cap","sc"])
    typ_match.append(["screw_countersunk","cs"])
    typ_match.append(["screw_flat_head","fh"])    
    typ_match.append(["set_screw","ss"])
    typ_match.append(["screw_self_tapping","st"])
    typ_match.append(["screw_thread_forming","tf"])
    typ_match.append(["spacer","sp"])
    typ_match.append(["standoff","so"])
    
    typ = ""
    for match in typ_match:
        if match[0] == typ_source:
            typ = match[1]

    size = ""
    color = ""
    if typ != "":
        #size
        size = deets.get("size","")
        if typ_source == "spacer":
            size = size.replace("_id_","x")
            size = size.replace("_mm_od","")
            pass
        else:
            size = deets.get("size","")
            size = size.replace("_mm","").replace("m","")
            size = size.replace("_","d") # deal with decimal points

        #if size i m and a number remove the m
        if size.startswith("m") and size[1].isdigit():
            size = size[1:]
        
        #color
        color = deets.get("color","")
        color_source = color
        color_match = []
        color_match.append(["nylon_black","nb"])
        color_match.append(["black","b"])
        color_match.append(["brass","br"])
        color_match.append(["bright_zinc_plated","bz"])
        color_match.append(["stainless","s"])
        color_match.append(["nylon_white","nw"])
        color_match.append(["gold","g"])
        color = "m"
        for match in color_match:
            if match[0] == color_source:
                color = match[1]

        # length
        desc_main = deets.get("description_main","")
        length = desc_main
        length = length.replace("_mm_length","").replace("_mm","")

        # head
        desc_extra = deets.get("description_extra","")
        head_source = desc_extra
        head_match = []
        head_match.append(["flat_head","f"])
        head_match.append(["phillips_head","p"])
        head_match.append(["pozidrive_head","pz"])
        head_match.append(["hex_head","h"])
        head_match.append(["nut_and_nut","nn"])
        head_match.append(["screw_and_nut","sn"])
        head_match.append(["screw_and_screw","ss"])

        head = ""
        for match in head_match:
            if match[0] == head_source:
                head = match[1]
        
        oomlout_short_code = f"{typ}{size}{color}{length}{head}"

    return oomlout_short_code
    
    
