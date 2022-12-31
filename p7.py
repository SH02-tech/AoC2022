import sys

class DirInfo:
    def __init__(self):
        self.mapping = dict() # Dir: value
        self.is_dir = dict() # Dir: Determines if it's a folder.

    def updateadd_elem(self, dirlist, size):
        depth = 0

        for i in range(1, int(len(dirlist))+1):
            path = "/" + "/".join(dirlist[1:i])
            
            if path in self.mapping:
                self.mapping[path] += size
            else:
                self.mapping[path] = size

                if size > 0:
                    self.is_dir[path] = False
                else:
                    self.is_dir[path] = True


    def get_under(self, max_size):
        solution = dict()
        
        for dirpath, size in self.mapping.items():
            if size <= max_size and self.is_dir[dirpath]:
                solution[dirpath] = size

        return solution

    def get_over(self, min_size):
        solution = dict()

        for dirpath, size in self.mapping.items():
            if size >= min_size and self.is_dir[dirpath]:
                solution[dirpath] = size

        return solution

    def get_liberate(self, total_size, wanted_size):
        used_size = self.mapping["/"]

        min_size_reduce = wanted_size - (total_size - used_size)
        return self.get_over(min_size_reduce)

def get_sum(mapvalues):
    sum = 0

    for dirpath, size in mapvalues.items():
        sum += size

    return sum

def min_size(mapvalues):
    min = sys.maxsize 

    for dirpath, size in mapvalues.items():
        if size < min:
            min = size

    return min

def p7a():
    dir_info = DirInfo()
    dirpath = list()
    f = open(sys.argv[1], 'r')

    for line in f:
        if line[2:4] == "cd":
            new_dir = line[5:-1]
            
            if new_dir[0:2] != "..":
                dirpath.append(new_dir)
            else:
                dirpath.pop(len(dirpath)-1)
        elif line[0:3] == "dir":
            dir_name = line.split()[1]
            dir_info.updateadd_elem(dirpath + [dir_name], 0)
        elif line[0].isnumeric():
            size, file_name = line.split()
            size = int(size)
            dir_info.updateadd_elem(dirpath + [file_name], size)

    solution = dir_info.get_under(100000)

    for key, value in solution.items(): 
        print(key, value)

    print("Total sum:", get_sum(solution))

def p7b():
    dir_info = DirInfo()
    dirpath = list()
    f = open(sys.argv[1], 'r')

    for line in f:
        if line[2:4] == "cd":
            new_dir = line[5:-1]
            
            if new_dir[0:2] != "..":
                dirpath.append(new_dir)
            else:
                dirpath.pop(len(dirpath)-1)
        elif line[0:3] == "dir":
            dir_name = line.split()[1]
            dir_info.updateadd_elem(dirpath + [dir_name], 0)
        elif line[0].isnumeric():
            size, file_name = line.split()
            size = int(size)
            dir_info.updateadd_elem(dirpath + [file_name], size)

    solution = dir_info.get_liberate(70000000, 30000000)

    for key, value in solution.items(): 
        print(key, value)

    print("Min directory size:", min_size(solution))


def main():
    p7b()

if __name__ == '__main__':
    main()
