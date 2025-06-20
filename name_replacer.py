from pathlib import Path
import shutil

def directory_validator(root : str) -> str:
    if root[0] == '\"':
        root = root[1:]
    if root[len(root)-1] == '\"':
        root = root[:len(root)-1]
    return root

root : str = directory_validator(input("INPUT A DIRECTORY PATH: "))

if not (Path(root).exists()):
    print("\nINVALID DIRECTORY INPUT PATH")
    exit()
else:
    print("\nVALID DIRECTORY PATH\n")
    
out_root : str = directory_validator(input("INPUT AN OUTPUT PATH: "))
if not (Path(out_root).exists()):
    print("\nINVALID DIRECTORY OUTPUT PATH")
    exit()

old : str = input("\nINPUT TARGET STRING: ")
new : str = input("\nINPUT REPLACEMENT STRING: ")

def replacer(root_path: str, new_path: str, old: str, new: str):
    root_path = Path(root_path)
    new_path = Path(new_path)

    for item in root_path.rglob("*"):
        relative_path = item.relative_to(root_path) #getting the relative path from the root

        # Renaming file and folder names
        replaced_parts = [part.replace(old, new) for part in relative_path.parts]
        new_item_path = new_path.joinpath(*replaced_parts)

        # if item is directory
        if item.is_dir():
            new_item_path.mkdir(parents=True, exist_ok=True)
        # if item is file
        elif item.is_file():
            if item.suffix == ".sql":
                # read file and replace occurences of old with new
                with item.open("r", encoding="utf-8") as f:
                    content = f.read().replace(old, new)
                
                new_item_path.parent.mkdir(parents=True, exist_ok=True)
                # write new contents into a new file
                with new_item_path.open("w", encoding="utf-8") as f:
                    f.write(content)
                    
            # condition for non .sql files
            # just copies the file onto the new directory 
            else:
                new_item_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, new_item_path)

    print("\nCOPY AND REPLACEMENT COMPLETED. NEW DIRECTORY CREATED IN \"", new_path + "\"")

replacer(root, out_root, old, new)
