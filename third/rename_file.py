import os

# Mapping of previous file names (with .html) to JSON file names (without .html)
rename_mapping = {
    # Semester 1
    "./first/C_Programming_2074.html": "C_Programming_2074",
    "./first/C_Programming_2075.html": "C_Programming_2075",
    "./first/C_Programming_2077.html": "C_Programming_2077",
    "./first/C_Programming_2078.html": "C_Programming_2078",
    "./first/C_Programming_2079.html": "C_Programming_2079",
    "./first/C_Programming_2080.html": "C_Programming_2080",
    "./first/C_Programming_2081.html": "C_Programming_2081",
    "./first/Digital_Logic_2074.html": "Digital_Logic_2074",
    "./first/Digital_Logic_2075.html": "Digital_Logic_2075",
    "./first/Digital_Logic_2077.html": "Digital_Logic_2077",
    "./first/Digital_Logic_2078.html": "Digital_Logic_2078",
    "./first/Digital_Logic_2080.html": "Digital_Logic_2080",
    "./first/Digital_Logic_2081.html": "Digital_Logic_2081",
    "./first/Introduction_to_IT_2074.html": "Introduction_to_IT_2074",
    "./first/Introduction_to_IT_2075.html": "Introduction_to_IT_2075",
    "./first/Introduction_to_IT_2077.html": "Introduction_to_IT_2077",
    "./first/Introduction_to_IT_2078.html": "Introduction_to_IT_2078",
    "./first/Introduction_to_IT_2080.html": "Introduction_to_IT_2080",
    "./first/Introduction_to_IT_2081.html": "Introduction_to_IT_2081",
    "./first/Mathematics_I_2074.html": "Mathematics_I_2074",
    "./first/Mathematics_I_2075.html": "Mathematics_I_2075",
    "./first/Mathematics_I_2077.html": "Mathematics_I_2077",
    "./first/Mathematics_I_2078.html": "Mathematics_I_2078",
    "./first/Mathematics_I_2079.html": "Mathematics_I_2079",
    "./first/Mathematics_I_2080.html": "Mathematics_I_2080",
    "./first/Mathematics_I_2081.html": "Mathematics_I_2081",
    "./first/Physics_2074.html": "Physics_2074",
    "./first/Physics_2075.html": "Physics_2075",
    "./first/Physics_2077.html": "Physics_2077",
    "./first/Physics_2078.html": "Physics_2078",
    "./first/Physics_2079.html": "Physics_2079",
    "./first/Physics_2080.html": "Physics_2080",
    "./first/Physics_2081.html": "Physics_2081",
    # Semester 2
    "./second/Data_Structures_2075.html": "Data_Structures_2075",
    "./second/Data_Structures_2076.html": "Data_Structures_2076",
    "./second/Data_Structures_2078.html": "Data_Structures_2078",
    "./second/Data_Structures_2079.html": "Data_Structures_2079",
    "./second/Data_Structures_2080.html": "Data_Structures_2080",
    "./second/Data_Structures_2080_new.html": "Data_Structures_2080_new",
    "./second/Mathematics_II_2075.html": "Mathematics_II_2075",
    "./second/Mathematics_II_2076.html": "Mathematics_II_2076",
    "./second/Mathematics_II_2078.html": "Mathematics_II_2078",
    "./second/Mathematics_II_2079.html": "Mathematics_II_2079",
    "./second/Mathematics_II_2080.html": "Mathematics_II_2080",
    "./second/Mathematics_II_2080_new.html": "Mathematics_II_2080_new",
    "./second/Microprocessor_2075.html": "Microprocessor_2075",
    "./second/Microprocessor_2076.html": "Microprocessor_2076",
    "./second/Microprocessor_2078.html": "Microprocessor_2078",
    "./second/Microprocessor_2079.html": "Microprocessor_2079",
    "./second/Microprocessor_2080.html": "Microprocessor_2080",
    "./second/Microprocessor_2080_new.html": "Microprocessor_2080_new",
    "./second/OOPS_2075.html": "OOPS_2075",
    "./second/OOPS_2076.html": "OOPS_2076",
    "./second/OOPS_2078.html": "OOPS_2078",
    "./second/OOPS_2079.html": "OOPS_2079",
    "./second/OOPS_2080.html": "OOPS_2080",
    "./second/OOPS_2080_new.html": "OOPS_2080_new",
    "./second/Statistics_I_2075.html": "Statistics_I_2075",
    "./second/Statistics_I_2076.html": "Statistics_I_2076",
    "./second/Statistics_I_2078.html": "Statistics_I_2078",
    "./second/Statistics_I_2079.html": "Statistics_I_2079",
    "./second/Statistics_I_2080.html": "Statistics_I_2080",
    "./second/Statistics_I_2080_new.html": "Statistics_I_2080_new",
    # Semester 3
    "./third/Computer_Architecture_Model.html": "Computer_Architecture_Model",
    "./third/Computer_Architecture_2075_new.html": "Computer_Architecture_2075_new",
    "./third/Computer_Architecture_2075_old.html": "Computer_Architecture_2075_old",
    "./third/Computer_Architecture_2077.html": "Computer_Architecture_2077",
    "./third/Computer_Architecture_2078.html": "Computer_Architecture_2078",
    "./third/Computer_Architecture_2079.html": "Computer_Architecture_2079",
    "./third/Computer_Architecture_2080.html": "Computer_Architecture_2080",
    "./third/Computer_Graphics_Model.html": "Computer_Graphics_Model",
    "./third/Computer_Graphics_2075.html": "Computer_Graphics_2075",
    "./third/Computer_Graphics_2077.html": "Computer_Graphics_2077",
    "./third/Computer_Graphics_2078.html": "Computer_Graphics_2078",
    "./third/Computer_Graphics_2079.html": "Computer_Graphics_2079",
    "./third/Computer_Graphics_2080.html": "Computer_Graphics_2080",
    "./third/Data_Structures_and_Algorithms_Model_I.html": "Data_Structures_and_Algorithms_Model_I",
    "./third/Data_Structures_and_Algorithms_Model_II.html": "Data_Structures_and_Algorithms_Model_II",
    "./third/Data_Structures_and_Algorithms_2074.html": "Data_Structures_and_Algorithms_2074",
    "./third/Data_Structures_and_Algorithms_2075.html": "Data_Structures_and_Algorithms_2075",
    "./third/Data_Structures_and_Algorithms_2077.html": "Data_Structures_and_Algorithms_2077",
    "./third/Data_Structures_and_Algorithms_2078.html": "Data_Structures_and_Algorithms_2078",
    "./third/Data_Structures_and_Algorithms_2079.html": "Data_Structures_and_Algorithms_2079",
    "./third/Data_Structures_and_Algorithms_2080.html": "Data_Structures_and_Algorithms_2080",
    "./third/Data_Structures_and_Algorithms_2081.html": "Data_Structures_and_Algorithms_2081",
    "./third/Numerical_Methods_Model_I.html": "Numerical_Methods_Model_I",
    "./third/Numerical_Methods_Model_II.html": "Numerical_Methods_Model_II",
    "./third/Numerical_Methods_2075.html": "Numerical_Methods_2075",
    "./third/Numerical_Methods_2077.html": "Numerical_Methods_2077",
    "./third/Numerical_Methods_2078.html": "Numerical_Methods_2078",
    "./third/Numerical_Methods_2079.html": "Numerical_Methods_2079",
    "./third/Numerical_Methods_2080.html": "Numerical_Methods_2080",
    "./third/Statistics_II_Model_I.html": "Statistics_II_Model_I",
    "./third/Statistics_II_Model_II.html": "Statistics_II_Model_II",
    "./third/Statistics_II_2075.html": "Statistics_II_2075",
    "./third/Statistics_II_2077.html": "Statistics_II_2077",
    "./third/Statistics_II_2078.html": "Statistics_II_2078",
    "./third/Statistics_II_2079.html": "Statistics_II_2079",
    "./third/Statistics_II_2080.html": "Statistics_II_2080",
    # Semester 4
    "./fourth/Artificial_Intelligence_Model.html": "Artificial_Intelligence_Model",
    "./fourth/Artificial_Intelligence_2076.html": "Artificial_Intelligence_2076",
    "./fourth/Artificial_Intelligence_2078.html": "Artificial_Intelligence_2078",
    "./fourth/Artificial_Intelligence_2079.html": "Artificial_Intelligence_2079",
    "./fourth/Artificial_Intelligence_2080.html": "Artificial_Intelligence_2080",
    "./fourth/Artificial_Intelligence_2080_new.html": "Artificial_Intelligence_2080_new",
    "./fourth/Artificial_Intelligence_2081.html": "Artificial_Intelligence_2081",
    "./fourth/Computer_Networks_Model.html": "Computer_Networks_Model",
    "./fourth/Computer_Networks_2076.html": "Computer_Networks_2076",
    "./fourth/Computer_Networks_2078.html": "Computer_Networks_2078",
    "./fourth/Computer_Networks_2079.html": "Computer_Networks_2079",
    "./fourth/Computer_Networks_2080.html": "Computer_Networks_2080",
    "./fourth/Computer_Networks_2080_new.html": "Computer_Networks_2080_new",
    "./fourth/Computer_Networks_2081.html": "Computer_Networks_2081",
    "./fourth/Database_Management_Systems_Model.html": "Database_Management_Systems_Model",
    "./fourth/Database_Management_Systems_2076.html": "Database_Management_Systems_2076",
    "./fourth/Database_Management_Systems_2078.html": "Database_Management_Systems_2078",
    "./fourth/Database_Management_Systems_2079.html": "Database_Management_Systems_2079",
    "./fourth/Database_Management_Systems_2080.html": "Database_Management_Systems_2080",
    "./fourth/Database_Management_Systems_2080_new.html": "Database_Management_Systems_2080_new",
    "./fourth/Operating_Systems_Model.html": "Operating_Systems_Model",
    "./fourth/Operating_Systems_2076.html": "Operating_Systems_2076",
    "./fourth/Operating_Systems_2078.html": "Operating_Systems_2078",
    "./fourth/Operating_Systems_2079.html": "Operating_Systems_2079",
    "./fourth/Operating_Systems_2080.html": "Operating_Systems_2080",
    "./fourth/Operating_Systems_2080_new.html": "Operating_Systems_2080_new",
    "./fourth/Operating_Systems_2081.html": "Operating_Systems_2081",
    "./fourth/Theory_of_Computation_Model.html": "Theory_of_Computation_Model",
    "./fourth/Theory_of_Computation_2076.html": "Theory_of_Computation_2076",
    "./fourth/Theory_of_Computation_2078.html": "Theory_of_Computation_2078",
    "./fourth/Theory_of_Computation_2079.html": "Theory_of_Computation_2079",
    "./fourth/Theory_of_Computation_2080.html": "Theory_of_Computation_2080",
    "./fourth/Theory_of_Computation_2080_new.html": "Theory_of_Computation_2080_new",
    "./fourth/Theory_of_Computation_2081.html": "Theory_of_Computation_2081",
    # Semester 5
    "./fifth/Cryptography_Model.html": "Cryptography_Model",
    "./fifth/Cryptography_2076.html": "Cryptography_2076",
    "./fifth/Cryptography_2078.html": "Cryptography_2078",
    "./fifth/Cryptography_2079.html": "Cryptography_2079",
    "./fifth/Cryptography_2080.html": "Cryptography_2080",
    "./fifth/Cryptography_2081.html": "Cryptography_2081",
    "./fifth/Design_and_Analysis_of_Algorithms_Model.html": "Design_and_Analysis_of_Algorithms_Model",
    "./fifth/Design_and_Analysis_of_Algorithms_2076.html": "Design_and_Analysis_of_Algorithms_2076",
    "./fifth/Design_and_Analysis_of_Algorithms_2078.html": "Design_and_Analysis_of_Algorithms_2078",
    "./fifth/Design_and_Analysis_of_Algorithms_2079.html": "Design_and_Analysis_of_Algorithms_2079",
    "./fifth/Design_and_Analysis_of_Algorithms_2080.html": "Design_and_Analysis_of_Algorithms_2080",
    "./fifth/Design_and_Analysis_of_Algorithms_2081.html": "Design_and_Analysis_of_Algorithms_2081",
    "./fifth/Multimedia_Computing_2080.html": "Multimedia_Computing_2080",
    "./fifth/Multimedia_Computing_2081.html": "Multimedia_Computing_2081",
    "./fifth/System_Analysis_and_Design_Model.html": "System_Analysis_and_Design_Model",
    "./fifth/System_Analysis_and_Design_2076.html": "System_Analysis_and_Design_2076",
    "./fifth/System_Analysis_and_Design_2078.html": "System_Analysis_and_Design_2078",
    "./fifth/System_Analysis_and_Design_2079.html": "System_Analysis_and_Design_2079",
    "./fifth/System_Analysis_and_Design_2080.html": "System_Analysis_and_Design_2080",
    "./fifth/System_Analysis_and_Design_2081.html": "System_Analysis_and_Design_2081",
    "./fifth/Software_Architecture_and_Engineering_2076.html": "Software_Architecture_and_Engineering_2076",
    "./fifth/Software_Architecture_and_Engineering_2078.html": "Software_Architecture_and_Engineering_2078",
    "./fifth/Software_Architecture_and_Engineering_2079.html": "Software_Architecture_and_Engineering_2079",
    "./fifth/Simulation_and_Modeling_2076.html": "Simulation_and_Modeling_2076",
    "./fifth/Simulation_and_Modeling_2078.html": "Simulation_and_Modeling_2078",
    "./fifth/Simulation_and_Modeling_2079.html": "Simulation_and_Modeling_2079",
    "./fifth/Simulation_and_Modeling_2080.html": "Simulation_and_Modeling_2080",
    "./fifth/Simulation_and_Modeling_Model.html": "Simulation_and_Modeling_Model",
    "./fifth/Simulation_and_Modeling_2081.html": "Simulation_and_Modeling_2081",
    "./fifth/Web_Technology_Model.html": "Web_Technology_Model",
    "./fifth/Web_Technology_2076.html": "Web_Technology_2076",
    "./fifth/Web_Technology_2078.html": "Web_Technology_2078",
    "./fifth/Web_Technology_2079.html": "Web_Technology_2079",
    "./fifth/Web_Technology_2080.html": "Web_Technology_2080",
    "./fifth/Web_Technology_2081.html": "Web_Technology_2081",
    # Semester 6
    "./sixth/Compiler_Design_and_Construction_2075.html": "Compiler_Design_and_Construction_2075",
    "./sixth/Compiler_Design_and_Construction_2076.html": "Compiler_Design_and_Construction_2076",
    "./sixth/Compiler_Design_and_Construction_2078.html": "Compiler_Design_and_Construction_2078",
    "./sixth/Compiler_Design_and_Construction_2080.html": "Compiler_Design_and_Construction_2080",
    "./sixth/Compiler_Design_and_Construction_2081.html": "Compiler_Design_and_Construction_2081",
    "./sixth/Compiler_Design_and_Construction_2081_new.html": "Compiler_Design_and_Construction_2081_new",
    "./sixth/E_Commerce_2076.html": "E_Commerce_2076",
    "./sixth/E_Commerce_2078.html": "E_Commerce_2078",
    "./sixth/E_Commerce_2079.html": "E_Commerce_2079",
    "./sixth/E_Commerce_2080.html": "E_Commerce_2080",
    "./sixth/E_Commerce_2081.html": "E_Commerce_2081",
    "./sixth/E_Governance_2076.html": "E_Governance_2076",
    "./sixth/E_Governance_2078.html": "E_Governance_2078",
    "./sixth/E_Governance_2079.html": "E_Governance_2079",
    "./sixth/E_Governance_2080.html": "E_Governance_2080",
    "./sixth/E_Governance_2081.html": "E_Governance_2081",
    "./sixth/NET_Centric_Computing_2076.html": "NET_Centric_Computing_2076",
    "./sixth/NET_Centric_Computing_2078.html": "NET_Centric_Computing_2078",
    "./sixth/NET_Centric_Computing_2079.html": "NET_Centric_Computing_2079",
    "./sixth/NET_Centric_Computing_2080.html": "NET_Centric_Computing_2080",
    "./sixth/NET_Centric_Computing_2081.html": "NET_Centric_Computing_2081",
    "./sixth/Software_Engineering_Model.html": "Software_Engineering_Model",
    "./sixth/Software_Engineering_2076.html": "Software_Engineering_2076",
    "./sixth/Software_Engineering_2077.html": "Software_Engineering_2077",
    "./sixth/Software_Engineering_2079.html": "Software_Engineering_2079",
    "./sixth/Software_Engineering_2080.html": "Software_Engineering_2080",
    "./sixth/Software_Engineering_2081.html": "Software_Engineering_2081",
    "./sixth/Technical_Writing_2074.html": "Technical_Writing_2074",
    "./sixth/Technical_Writing_2075.html": "Technical_Writing_2075",
    "./sixth/Technical_Writing_2078.html": "Technical_Writing_2078",
    "./sixth/Technical_Writing_2079.html": "Technical_Writing_2079",
    "./sixth/Technical_Writing_2080.html": "Technical_Writing_2080",
    "./sixth/Technical_Writing_2081.html": "Technical_Writing_2081",
    # Semester 7
    "./seventh/Advanced_Java_Programming_2077.html": "Advanced_Java_Programming_2077",
    "./seventh/Advanced_Java_Programming_2078.html": "Advanced_Java_Programming_2078",
    "./seventh/Advanced_Java_Programming_2079.html": "Advanced_Java_Programming_2079",
    "./seventh/Advanced_Java_Programming_2080.html": "Advanced_Java_Programming_2080",
    "./seventh/Advanced_Java_Programming_Model.html": "Advanced_Java_Programming_Model",
    "./seventh/Data_Warehousing_and_Data_Mining_2078.html": "Data_Warehousing_and_Data_Mining_2078",
    "./seventh/Data_Warehousing_and_Data_Mining_2079.html": "Data_Warehousing_and_Data_Mining_2079",
    "./seventh/Data_Warehousing_and_Data_Mining_Model.html": "Data_Warehousing_and_Data_Mining_Model",
    "./seventh/Data_Warehousing_and_Data_Mining_2080.html": "Data_Warehousing_and_Data_Mining_2080",
    "./seventh/Principles_of_Management_2078.html": "Principles_of_Management_2078",
    "./seventh/Principles_of_Management_2079.html": "Principles_of_Management_2079",
    "./seventh/Principles_of_Management_2080.html": "Principles_of_Management_2080",
    "./seventh/Principles_of_Management_Model.html": "Principles_of_Management_Model",
    "./seventh/Software_Project_Management_2078.html": "Software_Project_Management_2078",
    "./seventh/Software_Project_Management_2079.html": "Software_Project_Management_2079",
    "./seventh/Software_Project_Management_2080.html": "Software_Project_Management_2080",
    # Semester 8
    "./eight/Advanced_Database_2079.html": "Advanced_Database_2079",
    "./eight/Advanced_Database_2080.html": "Advanced_Database_2080",
    "./eight/Advanced_Database_2081.html": "Advanced_Database_2081",
    "./eight/Cloud_Computing_2079.html": "Cloud_Computing_2079",
    "./eight/Cloud_Computing_2080.html": "Cloud_Computing_2080",
    "./eight/Cloud_Computing_2081.html": "Cloud_Computing_2081"
}

def rename_files():
    # Counter for tracking operations
    renamed_count = 0
    skipped_count = 0
    error_count = 0

    # Traverse all directories
    directories = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight"]
    for directory in directories:
        if not os.path.exists(directory):
            print(f"Directory {directory} does not exist, skipping...")
            continue

        for root, _, files in os.walk(directory):
            for file in files:
                if file == "index.html":  # Skip index.html
                    continue
                old_path = os.path.join(root, file)
                # Construct the expected old path as it appears in rename_mapping
                old_path_key = f"./{root}/{file}".replace("\\", "/")  # Normalize path for consistency
                if old_path_key in rename_mapping:
                    new_file_name = rename_mapping[old_path_key]
                    new_path = os.path.join(root, new_file_name)
                    try:
                        os.rename(old_path, new_path)
                        print(f"Renamed: {old_path} -> {new_path}")
                        renamed_count += 1
                    except FileNotFoundError:
                        print(f"File not found: {old_path}, skipping...")
                        error_count += 1
                    except OSError as e:
                        print(f"Error renaming {old_path}: {e}")
                        error_count += 1
                else:
                    print(f"No mapping found for {old_path}, skipping...")
                    skipped_count += 1

    # Summary
    print(f"\nSummary:")
    print(f"Files renamed: {renamed_count}")
    print(f"Files skipped (no mapping): {skipped_count}")
    print(f"Errors encountered: {error_count}")

if __name__ == "__main__":
    rename_files()