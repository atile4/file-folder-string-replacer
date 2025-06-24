from pathlib import Path
import shutil

def directory_validator(root : str) -> str:
    if root[0] == '\"':
        root = root[1:]
    if root[len(root)-1] == '\"':
        root = root[:len(root)-1]

    if not (Path(root).exists()):
        print("\nINVALID DIRECTORY INPUT PATH")
        exit()
    else : return root

root : str = directory_validator(input("INPUT A DIRECTORY PATH: "))
out_root : str = directory_validator(input("INPUT AN OUTPUT PATH: "))

old : str = input("\nINPUT TARGET STRING: ")
new : str = input("\nINPUT REPLACEMENT STRING: ")

filetype : str = input("\nINPUT FILE TYPE YOU WANT MODIFIED (sql, txt): ").lower()

if filetype not in ("sql", "txt"):
    print("\nINVALID FILE TYPE.")
    exit()

def replacer(root_path: str, new_path: str, old: str, new: str, filetype : str):
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
            if item.suffix == "."+filetype:
                # read file and replace occurences of old with new
                with item.open("r", encoding="utf-8") as f:
                    content = f.read().replace(old, new)
                
                new_item_path.parent.mkdir(parents=True, exist_ok=True)
                # write new contents into a new file
                with new_item_path.open("w", encoding="utf-8") as f:
                    f.write(content)
                    
            # just copies the file onto the new directory 
            else:
                new_item_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, new_item_path)

    print("\nCOPY AND REPLACEMENT COMPLETED. NEW DIRECTORY CREATED IN \""+ str(new_path) + "\"")

replacer(root, out_root, old, new, filetype)
