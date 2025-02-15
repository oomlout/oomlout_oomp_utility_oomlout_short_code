import os
import yaml
import glob
import copy
import pickle
import io

folder_configuration = "configuration"
folder_configuration = os.path.join(os.path.dirname(__file__), folder_configuration)
file_configuration = os.path.join(folder_configuration, "configuration.yaml")
#check if exists
if not os.path.exists(file_configuration):
    print(f"no configuration.yaml found in {folder_configuration} using default")
    file_configuration = os.path.join(folder_configuration, "configuration_default.yaml")


cnt_short = 1
#import configuration
configuration = {}
with open(file_configuration, 'r') as stream:
    try:
        configuration = yaml.load(stream, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:   
        print(exc)


def main(**kwargs):
    folder = kwargs.get("folder", f"{os.path.dirname(__file__)}/parts")
    folder = folder.replace("\\","/")
    
    kwargs["configuration"] = configuration
    print(f"running utility oomlout_short_coe for: {folder}")
    create_recursive(**kwargs)

def create_recursive(**kwargs):
    folder = kwargs.get("folder", os.path.dirname(__file__))
    kwargs["folder"] = folder
    filter = kwargs.get("filter", "")
    #if folder exists
    import threading
    semaphore = threading.Semaphore(100)
    threads = []

    #def create_thread(**kwargs):
    def create_thread(item, **kwargs):
        with semaphore:
            create_recursive_thread(item,**kwargs)
            #create_recursive_thread(**kwargs)
    
    for item in os.listdir(folder):
        kwargs["filter"] = filter
        kwargs["folder"] = folder
        kwargs["item"] = item
        #thread = threading.Thread(target=create_thread, kwargs=pickle.loads(pickle.dumps(kwargs,-1)))
        thread = threading.Thread(target=create_thread, kwargs={"iten":item, **kwargs})
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
            
            
            
            
#def create_recursive_thread(**kwargs):      
def create_recursive_thread(item, **kwargs):      
    global cnt_short      
    filter = kwargs.get("filter", "")
    folder = kwargs.get("folder","")
    #item = kwargs.get("item", "")
    if filter in item:
        directory_absolute = os.path.join(folder, item)
        directory_absolute = directory_absolute.replace("\\","/")
        if os.path.isdir(directory_absolute):
            #if working.yaml exists in the folder
            if os.path.exists(os.path.join(directory_absolute, "working.yaml")):
                #kwargs["directory_absolute"] = directory_absolute
                #create(**kwargs)
                create(directory_absolute, **kwargs)
                cnt_short += 1
                if cnt_short % 100 == 0:
                    print(f".", end="")
    else:
        #print(f"no folder found at {folder}")
        pass

#def create(**kwargs):
def create(directory_absolute, **kwargs):
    #directory_absolute = kwargs.get("directory_absolute", os.getcwd())    
    #kwargs["directory_absolute"] = directory_absolute    
    #generate(**kwargs)
    generate(directory_absolute, **kwargs)
    

#def generate(**kwargs):    
def generate(directory_absolute, **kwargs):    
    save_file = kwargs.get("save_file", True)
    #directory_absolute = kwargs.get("directory_absolute", os.getcwd())
    folder = kwargs.get("folder", os.getcwd())
    yaml_file = os.path.join(directory_absolute, "working.yaml")
    kwargs["yaml_file"] = yaml_file
    #load the yaml file
    details = {}

    mode = "open"
    #mode = "buffer"

    if mode == "open":
        with open(yaml_file, 'r') as stream:
            try:
                details = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:   
                print(exc)
    elif mode == "buffer":
        with open(yaml_file, 'r') as file:
            buffer = io.StringIO(file.read())
            details = yaml.load(buffer, Loader=yaml.FullLoader)
    #kwargs["details"] = details

    if details != {} and details != None:                
        #import from this folder
        # impotoomp_word from this files directory even if that isn't the cwd
        import sys
        sys.path.append(os.path.dirname(__file__))
        import oomlout_short_code
        import oomlout_bip_39_word
        
        if True:
            ##### process part here
            oomlout_short_code_result = oomlout_short_code.get_oomlout_short_code(details)
            if oomlout_short_code_result != "":
                #print(f"    generating for {directory_absolute}")
                #print(f"        oomlout_short_code: {oomlout_short_code_result}")
                details["oomlout_short_code"] = oomlout_short_code_result
                details["oomlout_short_code_upper"] = oomlout_short_code_result.upper()
                #write back to yaml file
                if save_file:
                    with open(yaml_file, 'w') as outfile:
                        yaml.dump(details, outfile, default_flow_style=False)
        
        ###### add bip 39 word combos
        bip_39_word = oomlout_bip_39_word.get_bip_39_word(details)
        if bip_39_word != []:
            #for i in range(0,len(bip_39_word)):
            bips = [2,3,len(bip_39_word)-1]
            for i in bips:
                details[f"bip_39_word_space_{i}"] = bip_39_word[i]
                if i > 0:
                    details[f"bip_39_word_new_line_{i}"] = bip_39_word[i].replace(" ","\n")
                    details[f"bip_39_word_new_br_{i}"] = bip_39_word[i].replace(" ","<br>")
                    details[f"bip_39_word_no_space_{i}"] = bip_39_word[i].replace(" ","")
                    details[f"bip_39_word_underscore_{i}"] = bip_39_word[i].replace(" ","_")
                    details[f"bip_39_word_dash_{i}"] = bip_39_word[i].replace(" ","-")


            
            #write back to yaml file
            #mode = "open"
            mode = "buffer"
            if mode == "open":
                with open(yaml_file, 'w') as outfile:
                    yaml.dump(details, outfile, default_flow_style=False)
            elif mode == "buffer":
                import io
                with open(yaml_file, 'w') as file:
                    buffer = io.StringIO()
                    yaml.dump(details, buffer, default_flow_style=False)
                    file.write(buffer.getvalue())
                    buffer.close() 
                    



    else:
        print(f"no yaml file found in {directory_absolute}")    



if __name__ == '__main__':
    #folder is the path it was launched from
    
    kwargs = {}
    folder = os.path.dirname(__file__)
    #folder = "C:/gh/oomlout_oomp_builder/parts"
    #folder = "C:/gh/oomlout_oomp_part_generation_version_1/parts"
    #folder = "C:/gh/oomlout_oobb_version_4/things"
    #folder = "C:/gh/oomlout_oomp_current_version"
    folder = "Z:\\oomlout_oomp_current_version_fast_test\\parts"
    kwargs["folder"] = folder
    overwrite = False
    kwargs["overwrite"] = overwrite
    main(**kwargs)