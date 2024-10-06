

def get_bip_39_word(details):
    file_word_list = "source\\bip_39_wordlist.txt"
    #load word list into an array strip white space and new line
    word_list = []
    with open(file_word_list, 'r') as file:
        for line in file:
            word_list.append(line.strip())
        

    return_value = []
    md5 = details.get("md5", "")
    if md5 != "":
        #md5 to base 2048
        base_2048 = md5_hex_to_base_2048(md5)
        #go through return array, first element is the first word, second is the first and second and so on
        current_part_word_list = []

        #return_value.append(word_list)
        return_value.append("")
        for i in range(len(base_2048)):
            current_part_word_list.append(word_list[base_2048[i]].strip())
            current_part_word_string = " ".join(current_part_word_list)
            return_value.append(current_part_word_string)
        return_value[0] = current_part_word_list
    return return_value 


def md5_hex_to_base_2048(md5_hex):
    md5_int = int(md5_hex, 16)
    base_2048 = []
    while md5_int > 0:
        base_2048.append(md5_int % 2048)
        md5_int = md5_int // 2048
    return base_2048