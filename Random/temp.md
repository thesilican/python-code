## Description

Your task is to implement a simple UNIX command parser and file system. Your program will have to implement a file system that can be modified via commands.

The starting directory of your file system is an empty root directory `/`, with no subdirectories or files. Your program must be capable of handling the following commands:

## Commands

`cd <dirpath>` - Change the current directory

- `<dirpath>` will be a list of directory names or "..", seperated by "/"
- e.g. `cd ../folder1/folder2` means to navigate up one directory level, then descend into `folder1`, then descend into `folder2`
- If the directory path is not valid, then the command will do nothing

`touch <filename>` - Create a new file

- e.g. `touch me.txt` creates a file called `me.txt` in the current directory
- Filenames will only contain characters a-z and "."
  - Filenames will contain "." at least once
  - "." will never be the first or last character in a file name
- If a file already exists with the same name in the current directory, nothing happens

`mkdir <dirname>` - Create a new directory

- e.g. `mkdir photos` creates a new `photos` directory in the current directory
- Directory names will only contan characters a-z
- If a directory already exists with the same name in the current directory, nothing happens

`rm [-r] <filename-or-dirname>` - Remove a file or directory

- e.g. `rm hello.mp3` removes a file named `hello.mp3` in the current directory
- e.g. `rm -r documents` removes a folder named `documents` in the current directory, and all of its contents
- If `rm` tries to delete a directory without the `-r` flag, nothing will happen
  - However `rm` will delete a file even with the `-r` flag
- If the specified directory or file cannot be found, nothing happens

## Tree output

Your program will output the following tree-like representation of the current file system using spaces as indentation. For example:

```
/
  documents/
    document.docx
  downloads/
    zippedfile/
      notavirus.exe
    coolgoats.mp3
    zippedfile.zip
  pictures/
    myvacation.png
```

- All directories names must end with a "/"
- Use 2 spaces to indent each nested tree level
- Directories must be listed before files in the same directory
- Directories and files should be listed in lexographical alphabetical order
  - The character "." lexographically comes before any alphabetical character

## Challenge

Create a program that accepts a series of commands, and outputs a tree-like representation of the current file system.

Inputs are a list of commands seperated by newlines.

You must output the contents of the file system in a tree-like representation as shown above.

## Test Cases

Input 1: Simple example from earlier

```
mkdir documents
cd documents
touch document.docx
cd ..
mkdir downloads
cd downloads
touch coolgoats.mp3
touch zippedfile.zip
mkdir zippedfile
cd zippedfile
touch notavirus.exe
cd ../..
mkdir pictures
cd pictures
touch myvacation.png
```

Output 1:

```
/
  documents/
    document.docx
  downloads/
    zippedfile/
      notavirus.exe
    coolgoats.mp3
    zippedfile.zip
  pictures/
    myvacation.png
```

Input 2:
Incorrect commands and edge cases

```
mkdir folder1
mkdir folder1
mkdir folder2
rm folder1
rm -r folder2
cd ..
cd ../folder1
cd folder1/folder2
touch file.txt
touch file.txt
touch file2.txt
rm -r file2.txt
```

Output 2:

```
/
  folder1
  file.txt
```

Input 3:
Alphabetical listing of directories and files

```
mkdir b
mkdir c
mkdir a
touch c.txt
touch aa.txt
touch b.txt
touch a.txt
touch ab.txt
```

Output 3:

```
/
  a/
  b/
  c/
  a.txt
  aa.txt
  ab.txt
  b.txt
  c.txt
```

Standard loopholes apply.

**This is [tag:code-golf], shortest code in each language wins.**
