
import os

def group_rename_files(desired_name, digits, source_extension, target_extension, name_range):
    files = os.listdir('.')
 
    source_files = [file for file in files if file.endswith('.' + source_extension)]
 
    source_files.sort()

    counter = 1

    for source_file in source_files:
        original_name = os.path.splitext(source_file)[0]
 
        range_start = name_range[0] - 1
        range_end = name_range[1]
        selected_name = original_name[range_start:range_end]
 
        if desired_name:
            new_name = selected_name + '_' + desired_name
        else:
            new_name = selected_name

        new_file_name = new_name + '_' + str(counter).zfill(digits) + '.' + target_extension
 
        os.rename(source_file, new_file_name)
 
        counter += 1


